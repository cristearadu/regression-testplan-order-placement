from retry import retry
from step_impl.utils import Driver
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button, log_attribute_and_value


class HeaderBasePage:
    """
    Base page to init same elements POM classes
    """
    HEADER_SECTION = (By.XPATH, '//header[@id="header"]')
    SIGN_IN_BUTTON = (By.XPATH, f'{HEADER_SECTION[1]}/div[2]/div/div/nav/div[1]/a')
    SIGN_OUT_BUTTON = (By.XPATH, f'{HEADER_SECTION[1]}/div[2]/div/div/nav/div[2]/a')
    CONTACT_US_BUTTON = (By.XPATH, '//div[@id="contact-link"]/a')
    HOME_PAGE = (By.XPATH, '//div[@id="header_logo"]/a/img')
    SEARCH_BAR_TEXTBOX = (By.XPATH, '//input[@id="search_query_top"]')
    SEARCH_BAR_BUTTON = (By.XPATH, '//form[@id="searchbox"]/button')
    SHOPPING_CART_BUTTON = (By.XPATH, f'{HEADER_SECTION[1]}/div[3]/div/div/div[3]/div/a')

    def __init__(self):
        self.driver = Driver.driver
        self.driver.wait_for_element_to_be_visible(self.HEADER_SECTION)

    @log_click_button
    @retry(tries=3, delay=1)
    def click_sign_in_button(self):
        Button(self.SIGN_IN_BUTTON).click()

    @log_click_button
    def click_contact_us_button(self):
        Button(self.CONTACT_US_BUTTON).click()

    @log_click_button
    def click_home_page_button(self):
        Button(self.HOME_PAGE).click()

    @log_attribute_and_value
    def search_for_item(self, item: str):
        TextBox(self.SEARCH_BAR_TEXTBOX).contents = item

    @log_click_button
    def click_on_search_button(self):
        Button(self.SEARCH_BAR_BUTTON).click()

    @log_click_button
    def click_on_shopping_cart_button(self):
        Button(self.SHOPPING_CART_BUTTON).click()
