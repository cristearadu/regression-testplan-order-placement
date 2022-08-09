from step_impl.utils import Driver
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base page to init same elements POM classes
    """

    SIGN_IN = (By.XPATH, '//header[@id="header"]/div[2]/div/div/nav/div[1]/a')
    SIGN_OUT = (By.XPATH, '//header[@id="header"]/div[2]/div/div/nav/div[2]/a')

    def __init__(self):
        self.driver = Driver.driver
