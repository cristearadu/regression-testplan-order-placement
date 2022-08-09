from retry import retry
from selenium.webdriver.common.by import By
from core_elements.pages.base_page import BasePage
from core_elements.models.elements import Button
from core_elements.project_decorators import log_click_button


class HomePage(BasePage):

    SLIDER_ROW = (By.XPATH, '//div[@id="slider_row"]')
    HOMEFEATURED_ELEMENTS = (By.XPATH, '//ul[@id="homefeatured"]/li')
    CONTENT_HOME = (By.XPATH, '//div[@id="htmlcontent_home"]/ul')

    def __init__(self):
        super(HomePage, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.SIGN_IN)
        self.driver.wait_for_element_to_be_visible(self.SLIDER_ROW)
        self.driver.wait_for_element_to_be_visible(self.HOMEFEATURED_ELEMENTS)
        self.driver.wait_for_element_to_be_visible(self.CONTENT_HOME)

    @property
    def sign_in_button(self):
        return Button(self.SIGN_IN)

    @log_click_button
    @retry(tries=3, delay=1)
    def click_sign_in_button(self):
        self.sign_in_button.click()
