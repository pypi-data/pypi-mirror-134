import re
from io import BytesIO

import cv2
import base64
import numpy as np
from PIL import Image


class Jsonizable(object):
    def json(self):
        raise NotImplementedError(f'json() not implemented on {type(self).__name__}')


class Typed(object):
    def type(self):
        raise NotImplementedError(f'type() not implemented on {type(self).__name__}')


class Validatable(object):
    def validate_data(self, data) -> bool:
        raise NotImplementedError(f'validate_data not implemented on {type(self).__name__}')


class ImageUtils(object):
    @classmethod
    def from_cv2_image(cls, cv2_image):
        _, buffer = cv2.imencode('.jpg', cv2_image)
        return cls(base64.b64encode(buffer).decode('utf-8'))

    @classmethod
    def from_pillow_image(cls, pillow_image):
        open_cv_image = np.array(pillow_image)
        cv2_image = open_cv_image[:, :, ::-1].copy()
        return cls.from_cv2_image(cv2_image)

    def validate_base64_image(self, data: str):
        m = re.search('^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', data)
        return m is not None

    def base64_image(self) -> str:
        raise NotImplementedError(f'base64_image not implemented in {type(self).__name__}')

    def get_cv2_image(self):
        encoded_data = self.base64_image().split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    def get_pillow_image(self):
        return Image.open(BytesIO(base64.b64decode(self.base64_image())))
