from getgauge.python import step, data_store
from step_impl.utils import Driver
from core_elements.pages import AuthenticationPage, CreateAccount, MyAccount
from core_elements import logger
from core_elements.algos import UserPass, CreateNewUser, GaugeData
from core_elements.expected_errors import RegisterError


@step("Log in using valid credentials")
def log_in_using_valid_credentials():
    authentication_page = AuthenticationPage()
    valid_user_password = UserPass()

    logger.info("Logging in with valid user and password")

    authentication_page.email_input.contents = valid_user_password.decode_username
    authentication_page.password_input.contents = valid_user_password.decode_password

    authentication_page.click_sign_in_button()


@step("Write last registered email address")
def write_last_registered_email_address():

    authentication_page = AuthenticationPage()
    data_store.create_user = CreateNewUser()

    authentication_page.create_account_email_address(data_store.create_user.last_created_username)
    authentication_page.click_create_account_button()


@step("Write unused email address")
def write_unused_email_address():
    authentication_page = AuthenticationPage()
    data_store.create_user = CreateNewUser()
    data_store.new_username = data_store.create_user.new_username
    logger.info(f"Creating new valid user using: {data_store.new_username}")

    authentication_page.create_account_email_address(data_store.new_username)
    authentication_page.click_create_account_button()

    assert Driver.driver.check_exists(CreateAccount.FIRST_NAME_TEXTBOX), "Failed to load \'Create Account\' page"


@step("Write valid data for user and Register <table>")
def write_valid_data_for_user(table):
    data_store.sign_in_client_information = GaugeData.table_to_dict(table)
    logger.info(f"Using sign in information for client: {data_store.sign_in_client_information}")

    create_account = CreateAccount()

    create_account.complete_mandatory_client_sign_in_data(
        personal_information_first_name=data_store.sign_in_client_information['first_name'],
        personal_information_last_name=data_store.sign_in_client_information['last_name'],
        email_value=data_store.new_username,
        password=data_store.sign_in_client_information['password'],
        date_of_birth_day=data_store.sign_in_client_information['day'],
        date_of_birth_month=data_store.sign_in_client_information['month'],
        date_of_birth_year=data_store.sign_in_client_information['year'],
        first_name_textbox=data_store.sign_in_client_information['first_name'],
        last_name_textbox=data_store.sign_in_client_information['last_name'],
        company=data_store.sign_in_client_information['company'],
        address_1_textbox=data_store.sign_in_client_information['address'],
        city=data_store.sign_in_client_information['city'],
        state_dropdown=data_store.sign_in_client_information['state'],
        postcode=data_store.sign_in_client_information['post_code'],
        country_dropdown=data_store.sign_in_client_information['country'],
        home_phone=data_store.sign_in_client_information['phone_number'])

    create_account.click_register_button()

    data_store.create_user.modify_new_user_file()


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
    assert Driver.driver.check_exists(AuthenticationPage.SIGN_OUT_BUTTON), "Failed to see \'Sign Out\' button"
    assert Driver.driver.check_exists(MyAccount.ORDER_HISTORY_AND_DETAILS), \
        "Failed to load \'Order and History Details\' element"
    logger.info("Authentication page has loaded")


@step("Verify an error appears on page after clicking on register")
def verify_error_appears_after_clicking_on_register():
    assert Driver.driver.check_exists(AuthenticationPage.FAIL_CREATE_ACCOUNT_TEXTBOX), \
        f"The expected error did not appear for already registered user"
    logger.info("The expected error has appeared for already registered user")


@step("Verify the error message is correctly thrown for already registered user")
def verify_the_error_message_already_registered_user():
    authentication_page = AuthenticationPage()
    assert RegisterError.already_registered_user.value in authentication_page.fail_to_create_account_textbox, \
        f"Failed to find the expected message error. Expected results: {RegisterError.already_registered_user.value}" \
        f"\nActual results: {authentication_page.fail_to_create_account_textbox}"
    logger.info(f"The expected error message has correctly appeared: {RegisterError.already_registered_user.value}")
