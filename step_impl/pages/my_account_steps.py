from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages import AuthenticationPage, MyAccount
from core_elements import logger
from core_elements.algos import UserPass


@step("Log in using valid credentials")
def log_in_using_valid_credentials():
    authentication_page = AuthenticationPage()
    valid_user_password = UserPass()

    logger.info("Logging in with valid user and password")

    authentication_page.email_input.contents = valid_user_password.decode_username
    authentication_page.password_input.contents = valid_user_password.decode_password

    authentication_page.click_sign_in_button()


"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify authentication page has loaded")
def verify_auth_page_has_loaded():
    assert Driver.driver.check_exists(AuthenticationPage.SIGN_IN_EMAIL_INPUT), "Failed to load \'Authentication\' page"
    logger.info("Authentication page has loaded")


@step("Verify my account page has loaded")
def verify_my_account_page_has_loaded():
    assert Driver.driver.check_exists(AuthenticationPage.SIGN_IN_EMAIL_INPUT), "Failed to load \'Authentication\' page"
    logger.info("Authentication page has loaded")


@step("Verify the user is signed in")
def verify_my_account_page_has_loaded():
    assert Driver.driver.check_exists(AuthenticationPage.SIGN_OUT), "Failed to see \'Sign Out\' button"
    assert Driver.driver.check_exists(MyAccount.ORDER_HISTORY_AND_DETAILS), \
        "Failed to load \'Order and History Details\' element"
    logger.info("Authentication page has loaded")

