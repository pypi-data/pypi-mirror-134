from starmart.config.config import Config


class ProductionConfig(Config):
    def github_repo(self) -> str:
        return 'https://github.com/starmart-io/Model-Template.git'

    def authentication_host(self) -> str:
        return 'https://starmart.io'

    def git_remote_host(self) -> str:
        return 'git@gitlab.com:starmart/user-uploaded-mappers-and-models'

    def user_git_host(self) -> str:
        return 'gitlab.com'