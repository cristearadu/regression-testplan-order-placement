from retry import retry
from step_impl.utils import Driver
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button, log_attribute_and_value
from core_elements.pages.base_page import HeaderBasePage


class ShoppingCart(HeaderBasePage):

    ORDER_STEPS = (By.XPATH, '//ul[@id="order_step"]/li')

    def __init__(self):
        super(ShoppingCart, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.ORDER_STEPS)
