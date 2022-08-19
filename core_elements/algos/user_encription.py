import base64
from settings import USER_PASS, CREATE_USER
from core_elements.algos.file_methods import read_json_file, overwrite_json_file
from core_elements.logging_element import logger
import re


class ReadJson:
    def __init__(self, login_user=True, create_user=False):

        if login_user:
            self._file = USER_PASS
            self._data = read_json_file(USER_PASS)
        elif create_user:
            self._file = CREATE_USER
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

    def __create_new_username(self, old_username):
        last_created_user_list = self._data['new_username'].split('@')

        literal_and_number_pattern = r"([a-z]+)([0-9]+)"
        email_address_match = re.match(literal_and_number_pattern, last_created_user_list[0])
        assert email_address_match, f"Failed to find a specific match for this pattern: {literal_and_number_pattern}\n" \
                                    f"Input data: {last_created_user_list}"
        email_address_items = email_address_match.groups()
        # todo
        new_username = f""  # todo

        new_username = f"{last_created_user_list[0]}@{last_created_user_list[1]}"
        return new_username

    def modify_new_user_file(self):
        logger.info("Incrementing the new user with one for the new user")
        self._data['last_created_username'] = self._data['new_username']
        self._data['new_username'] = self.__create_new_username(self._data['new_username'])
        overwrite_json_file(self._file, self._data)
