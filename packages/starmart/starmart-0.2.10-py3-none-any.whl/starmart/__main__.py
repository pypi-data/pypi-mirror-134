import _thread
import argparse
import logging
import os
import time
import webbrowser
from threading import Thread

from cryptography.hazmat.backends import default_backend as crypto_default_backend
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from git import Repo, InvalidGitRepositoryError
from halo import Halo
from sshconf import read_ssh_config, empty_ssh_config_file
from waitress import serve

from starmart.config.config import Config


class Action(object):
    def __init__(self, args):
        self.config = Config.default_config()
        self.args = args

    def act(self):
        raise NotImplementedError(f'act not implemented in {type(self).__name__}')

    @classmethod
    def get_action(cls):
        actions = dict({
            'deploy': DeployAction,
            'init': InitAction,
            'clone': CloneAction
        })

        args = cls.__parse_arguments__()
        action = actions.get(args.action[0])
        if action is None:
            raise ValueError('Action should be deploy, init or clone')

        return action(args)

    @classmethod
    def __parse_arguments__(cls):
        # configuring arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('action', nargs=1, type=str, default='None',
                            help='Run init on a new project, deploy to push the code or clone <project_id> to retrieve an existing project')
        parser.add_argument('project_id', nargs='?', help='The project id', default=None)
        return parser.parse_args()


class InitAction(Action):

    def act(self):
        self.__auth_with_web_browser__()

    def __auth_with_web_browser__(self):
        webbrowser.open(f'{self.config.authentication_host()}/development/login')
        self.__start_server__()

    def __start_server__(self):
        """
            This method blocks but all requests end using the `exit_after_seconds()` function
        """
        app = Flask(__name__)
        CORS(app)
        app.config['CORS_HEADERS'] = 'Content-Type'

        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        spinner = Halo(text='Waiting for browser authorization', spinner='dots')
        spinner.start()

        @app.route('/set-remote', methods=['POST'])
        @cross_origin()
        def set_remote():
            public_key = self.__get_or_create_ssh_public_key__()
            spinner.stop()
            self.__clone_after_webbrowser_auth__(request.json['remote'])
            return jsonify({'publicKey': public_key})

        @app.route('/set-clone', methods=['POST'])
        @cross_origin()
        def set_clone():
            spinner.stop()
            print(f'You already have an existing empty repository. Try calling',
                  bold(f'starmart clone {request.json["repo_id"]}'))
            exit_after_seconds()
            return jsonify({'status': 'ok'})

        serve(app, host="127.0.0.1", port=4999)

    def __clone_after_webbrowser_auth__(self, url: str):
        remote_host = self.config.git_remote_host()
        if not url.startswith(remote_host):
            raise ValueError(f'URL does not match the authentication host: {remote_host}')
        repo = self.__do_clone_default_code__()
        repo.create_remote('starmart', url=url)
        print('Happy coding!')

        # this is needed to exit flask server -> first it needs to return and then exit
        exit_after_seconds()

    @Halo(text='Cloning starter code repo', spinner='dots')
    def __do_clone_default_code__(self):
        cloned = Repo.clone_from(self.config.github_repo(), 'starter_code')
        for r in cloned.remotes:
            if r.name == 'origin':
                cloned.delete_remote(r)
                break
        return cloned

    def __get_or_create_ssh_public_key__(self):
        home = os.path.expanduser('~')
        ssh_dir = os.path.join(home, '.ssh')
        config_path = os.path.join(home, '.ssh', 'config')

        if not os.path.exists(ssh_dir):
            os.mkdir(ssh_dir)

        if not os.path.exists(config_path):
            config_file = empty_ssh_config_file()
            public_key = self.__create_and_write_ssh_keypair_and_update_config__(config_file)
            config_file.write(config_path)
            return public_key

        config_file = read_ssh_config(config_path)
        if self.config.user_git_host() in config_file.hosts():
            git_ssh_config = config_file.host(self.config.user_git_host())
            public_key_path = f"{git_ssh_config['identityfile']}.pub"
            with open(public_key_path, 'r') as f:
                return ''.join(f.readlines())

        public_key = self.__create_and_write_ssh_keypair_and_update_config__(config_file)
        config_file.save()
        return public_key

    def __create_and_write_ssh_keypair_and_update_config__(self, config_file):
        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )

        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        )

        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )

        home = os.path.expanduser('~')
        ssh_dir = os.path.join(home, '.ssh')

        # the file is opened this way in order to be created with the correct permissions
        with open(os.open(os.path.join(ssh_dir, 'gitlab'), os.O_CREAT | os.O_WRONLY, 0o400), 'wb') as f:
            f.write(private_key)

        with open(os.path.join(ssh_dir, 'gitlab.pub'), 'wb') as f:
            f.write(public_key)

        config_file.add(self.config.user_git_host(), Hostname=self.config.user_git_host(),
                        IdentityFile=os.path.join(ssh_dir, 'gitlab'))

        return public_key.decode('utf-8')


class DeployAction(Action):
    def act(self):
        self.__configure_repo__()

    @Halo(text='Pushing latest commits', spinner='dots')
    def __configure_repo__(self):
        try:
            repo = Repo('.')
            remote = None
            for r in repo.remotes:
                if r.name == 'starmart':
                    remote = r
                    break
            if remote is None:
                raise ValueError(f'The repository does not contain the starmart remote. Please call' +
                                 f' {bold("starmart init")}, before calling {bold("starmart deploy")}.')
            remote.push(refspec="main:main")
        except InvalidGitRepositoryError:
            raise ValueError('Github repository not initialized. Call starmart init before calling starmart deploy.')
        finally:
            print('\nPushed. Happy coding!')


class CloneAction(Action):

    def act(self):
        self.__clone_repo__()

    def __clone_repo__(self):
        project_id = self.args.project_id
        if project_id is None:
            raise ValueError(bold('starmart clone') + ' needs the project id')
        spinner = Halo(text=f'Cloning project {project_id}', spinner='dots')
        spinner.start()
        repo = Repo.clone_from(f'{self.config.git_remote_host()}/{project_id}.git', f'starmart_project_{project_id}')
        repo.remote('origin').rename('starmart')
        spinner.stop()
        print('Cloned. Happy coding!')


def exit_after_seconds(seconds=2):
    def do_exit():
        time.sleep(seconds)
        _thread.interrupt_main()

    Thread(target=do_exit).start()


def bold(text):
    return '\033[1m' + text + '\033[0m'


def main():
    Action.get_action().act()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
