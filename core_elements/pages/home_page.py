from selenium.webdriver.common.by import By
from core_elements.pages.base_page import HeaderBasePage


class HomePage(HeaderBasePage):

    SLIDER_ROW = (By.XPATH, '//div[@id="slider_row"]')
    HOME_FEATURED_ELEMENTS = (By.XPATH, '//ul[@id="homefeatured"]/li')
    CONTENT_HOME = (By.XPATH, '//div[@id="htmlcontent_home"]/ul')

    def __init__(self):
        super(HomePage, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.SIGN_IN_BUTTON)
        self.driver.wait_for_element_to_be_visible(self.SLIDER_ROW)
        self.driver.wait_for_element_to_be_visible(self.HOME_FEATURED_ELEMENTS)
        self.driver.wait_for_element_to_be_visible(self.CONTENT_HOME)


class ContactUsPage(HeaderBasePage):

    MESSAGE_TEXTBOX = (By.XPATH, '//textarea[@id="message"]')

    def __init__(self):
        super(ContactUsPage, self).__init__()
