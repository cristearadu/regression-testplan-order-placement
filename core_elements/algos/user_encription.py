import base64
from settings import USER_PASS
from core_elements.algos.file_methods import read_json_file


class UserPass:
    def __init__(self):
        data = read_json_file(USER_PASS)
        self.__user = data['username']
        self.__password = data['password']

    @property
    def decode_username(self):
        return self.decode_string(self.__user)

    @property
    def decode_password(self):
        return self.decode_string(self.__password)

    def decode_string(self, encoded_string):
        base64_bytes = encoded_string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('ascii')
