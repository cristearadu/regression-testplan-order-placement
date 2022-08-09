from retry import retry
from selenium.webdriver.common.by import By
from core_elements.pages.base_page import BasePage
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button, log_attribute_and_value


class AuthenticationPage(BasePage):

    SIGN_IN_EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    SIGN_IN_PASSWORD_INPUT = (By.XPATH, '//input[@id="passwd"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@id="SubmitLogin"]/span')

    CREATE_ACCOUNT_MAIL = (By.XPATH, '//input[@id="email_create"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@id="SubmitCreate"]/span')

    def __init__(self):
        super(AuthenticationPage, self).__init__()
        self.driver.wait_for_element_to_be_visible(self.SIGN_IN_EMAIL_INPUT)

    @property
    def email_input(self):
        return TextBox(self.SIGN_IN_EMAIL_INPUT)

    @property
    def password_input(self):
        return TextBox(self.SIGN_IN_PASSWORD_INPUT)

    @log_click_button
    def click_sign_in_button(self):
        return Button(self.SIGN_IN_BUTTON).click()

    @log_click_button
    def click_create_account_button(self):
        Button(self.CREATE_ACCOUNT_BUTTON).click()

    @log_attribute_and_value
    def create_account_email_address(self, value):
        TextBox(self.CREATE_ACCOUNT_MAIL).contents = value


class MyAccount(BasePage):
    ORDER_HISTORY_AND_DETAILS = (By.XPATH, '//div[@id="center_column"]/div/div[1]/ul/li[1]/a/span')
