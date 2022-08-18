import base64
from settings import USER_PASS, CREATE_USER
from core_elements.algos.file_methods import read_json_file


class ReadJson:
    def __init__(self, login_user=True, create_user=False):

        if login_user:
            self._data = read_json_file(USER_PASS)
        elif create_user:
            self._data = read_json_file(CREATE_USER)

    def decode_string(self, encoded_string):
        base64_bytes = encoded_string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('ascii')


class UserPass(ReadJson):

    def __init__(self):
        super(UserPass, self).__init__()
        self.__user = self._data['username']
        self.__password = self._data['password']

    @property
    def decode_username(self):
        return self.decode_string(self.__user)

    @property
    def decode_password(self):
        return self.decode_string(self.__password)


class CreateNewUser(ReadJson):

    def __init__(self):
        super(CreateNewUser, self).__init__(login_user=False, create_user=True)
        self.__last_created_username = self._data['last_created_username']
        self.__new_username = self._data['new_username']

    @property
    def last_created_username(self):
        return self.decode_string(self.__last_created_username)

    @property
    def new_username(self):
        return self.decode_string(self.__new_username)

