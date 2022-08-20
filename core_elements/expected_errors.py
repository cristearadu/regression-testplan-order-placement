from enum import Enum


class RegisterError(Enum):
    already_registered_user = "An account using this email address has already been registered. Please enter a valid" \
                              " password or request a new one."
