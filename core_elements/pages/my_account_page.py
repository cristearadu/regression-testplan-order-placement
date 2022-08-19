from retry import retry
import random
from selenium.webdriver.common.by import By
from core_elements.pages.base_page import BasePage
from core_elements.models.elements import Button, TextBox, Dropdown, RadioButton
from core_elements.project_decorators import log_click_button, log_attribute_and_value
from settings import Timeouts


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
    def create_account_email_address(self, email_address: str):
        TextBox(self.CREATE_ACCOUNT_MAIL).contents = email_address


class CreateAccount(BasePage):

    # Personal Information
    GENDER_MALE_RADIO = (By.XPATH, '//input[@id="id_gender1"]')
    GENDER_FEMALE_RADIO = (By.XPATH, '//input[@id="id_gender2"]')

    PERSONAL_FIRST_NAME_TEXTBOX = (By.XPATH, '//input[@id="customer_firstname"]')
    PERSONAL_LAST_NAME_TEXTBOX = (By.XPATH, '//input[@id="customer_lastname"]')
    EMAIL_TEXTBOX = (By.XPATH, '//input[@id="email"]')
    PASSWORD_TEXTBOX = (By.XPATH, '//input[@id="passwd"]')

    DAY_DROPDOWN = (By.XPATH, '//select[@id="days"]')
    MONTHS_DROPDOWN = (By.XPATH, '//select[@id="months"]')
    YEARS_DROPDOWN = (By.XPATH, '//select[@id="years"]')

    # Address
    FIRST_NAME_TEXTBOX = (By.XPATH, '//input[@id="firstname"]')
    LAST_NAME_TEXTBOX = (By.XPATH, '//input[@id="lastname"]')
    COMPANY_TEXTBOX = (By.XPATH, '//input[@id="company"]')
    ADDRESS_1_TEXTBOX = (By.XPATH, '//input[@id="address1"]')
    CITY_TEXTBOX = (By.XPATH, '//input[@id="city"]')
    STATE_DROPDOWN = (By.XPATH, '//select[@id="id_state"]')
    POSTCODE_TEXTBOX = (By.XPATH, '//input[@id="postcode"]')
    COUNTRY_DROPDOWN = (By.XPATH, '//select[@id="id_country"]')
    HOME_PHONE = (By.XPATH, '//input[@id="phone"]')

    def __init__(self, timeout=Timeouts.ELEMENT):
        super(CreateAccount, self).__init__()
        self.driver.wait_for_element_to_be_visible(self.PERSONAL_FIRST_NAME_TEXTBOX)
        self.__timeout = timeout

    @log_click_button
    def click_gender_male_radio(self):
        return RadioButton(self.GENDER_MALE_RADIO, timeout=self.__timeout).enable_radio()

    @log_click_button
    def click_gender_female_radio(self):
        return RadioButton(self.GENDER_FEMALE_RADIO, timeout=self.__timeout).enable_radio()

    @log_attribute_and_value
    def personal_information_first_name(self, first_name: str):
        TextBox(self.PERSONAL_FIRST_NAME_TEXTBOX).contents = first_name

    @log_attribute_and_value
    def personal_information_last_name(self, last_name: str):
        TextBox(self.PERSONAL_LAST_NAME_TEXTBOX).contents = last_name

    @property
    def email_contents(self):
        return TextBox(self.EMAIL_TEXTBOX).contents

    @log_attribute_and_value
    def email_value(self, first_name: str):
        TextBox(self.EMAIL_TEXTBOX).contents = first_name

    @log_attribute_and_value
    def password(self, password: str):
        TextBox(self.PASSWORD_TEXTBOX).contents = password

    @log_attribute_and_value
    def date_of_birth_day(self, day: str):
        Dropdown(self.DAY_DROPDOWN).dropdown_value_by_text = day

    @log_attribute_and_value
    def date_of_birth_month(self, month: str):
        Dropdown(self.MONTHS_DROPDOWN).dropdown_value_by_text = month

    @log_attribute_and_value
    def date_of_birth_year(self, year: str):
        Dropdown(self.YEARS_DROPDOWN).dropdown_value_by_text = year

    @log_attribute_and_value
    def first_name_textbox(self, first_name: str):
        TextBox(self.FIRST_NAME_TEXTBOX).contents = first_name

    @log_attribute_and_value
    def last_name_textbox(self, last_name: str):
        TextBox(self.LAST_NAME_TEXTBOX).contents = last_name

    @log_attribute_and_value
    def company(self, company_name: str):
        TextBox(self.COMPANY_TEXTBOX).contents = company_name

    @log_attribute_and_value
    def address_1_textbox(self, address: str):
        TextBox(self.ADDRESS_1_TEXTBOX).contents = address

    @log_attribute_and_value
    def city(self, city_name: str):
        TextBox(self.CITY_TEXTBOX).contents = city_name

    @log_attribute_and_value
    def state_dropdown(self, state_name: str):
        Dropdown(self.STATE_DROPDOWN).dropdown_value_by_text = state_name

    @log_attribute_and_value
    def postcode(self, postcode_number: str):
        TextBox(self.POSTCODE_TEXTBOX).contents = postcode_number

    @log_attribute_and_value
    def country_dropdown(self, country: str):
        Dropdown(self.COUNTRY_DROPDOWN).dropdown_value_by_text = country

    @log_attribute_and_value
    def home_phone(self, home_phone_number: str):
        TextBox(self.HOME_PHONE).contents = home_phone_number

    def complete_mandatory_client_sign_in_data(self, personal_information_first_name, personal_information_last_name,
                                               password, date_of_birth_day, date_of_birth_month, date_of_birth_year,
                                               email_value, first_name_textbox, last_name_textbox, company,
                                               address_1_textbox, city, state_dropdown, postcode, country_dropdown,
                                               home_phone):
        """
        Function that completes data for singing in.
        Implemented only for mandatory data.
        """
        select_gender = random.choice((self.click_gender_male_radio, self.click_gender_female_radio))
        select_gender()

        self.personal_information_first_name(personal_information_first_name)
        self.personal_information_last_name(personal_information_last_name)
        self.email_value(email_value)
        self.password(password)
        self.date_of_birth_day(date_of_birth_day)
        self.date_of_birth_month(date_of_birth_month)
        self.date_of_birth_year(date_of_birth_year)
        self.first_name_textbox(first_name_textbox)
        self.last_name_textbox(last_name_textbox)
        self.company(company)
        self.address_1_textbox(address_1_textbox)
        self.city(city)
        self.state_dropdown(state_dropdown)
        self.postcode(postcode)
        self.country_dropdown(country_dropdown)
        self.home_phone(home_phone)


class MyAccount(BasePage):
    ORDER_HISTORY_AND_DETAILS = (By.XPATH, '//div[@id="center_column"]/div/div[1]/ul/li[1]/a/span')
