from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages import HomePage


@step("From home page press on Sign in")
def from_home_page_press_on_sign_in():
    home_page = HomePage()
    home_page.click_sign_in_button()
