from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages import HeaderBasePage
from core_elements.logging_element import logger


@step("Click on Home Page image button")
def click_on_home_page_image_button():
    header_page = HeaderBasePage()
    header_page.click_home_page_button()


@step("Click on Cart Button")
def click_on_cart_button():
    header_page = HeaderBasePage()
    header_page.click_on_shopping_cart_button()
