from getgauge.python import step
from core_elements.pages import HomePage
from step_impl.utils import Driver
from core_elements.logging_element import logger
from selenium.common.exceptions import TimeoutException


@step("From home page press on Sign in")
def from_home_page_press_on_sign_in():
    home_page = HomePage()
    home_page.click_sign_in_button()


@step("Press on Contact us Button")
def press_contact_us_button():
    home_page = HomePage()
    home_page.click_contact_us_button()


@step("On Search Bar search for <item>")
def search_for_specific_item(item):
    home_page = HomePage()
    home_page.search_for_item(item)
    home_page.click_on_search_button()


"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify Home Page has loaded")
def home_page_has_loaded():
    try:
        HomePage()
        logger.info("Home Page has loaded")
    except TimeoutException:
        raise TimeoutException("Failed to load \'Home Page\' page")


@step("Verify Shopping Cart Button is present on page")
def verify_cart_button_is_present():
    assert Driver.driver.check_exists(HomePage.SHOPPING_CART_BUTTON), "Failed to find \'Shopping Cart\' button"
    logger.info("Shopping Cart button has been found")


@step("Verify Search Bar Textbox is present on page")
def verify_search_bar_textbox_is_present():
    assert Driver.driver.check_exists(HomePage.SEARCH_BAR_TEXTBOX), "Failed to find \'Search Bar\' textbox"
    logger.info("Search Bar textbox has been found")


@step("Verify Search Bar Button is present on page")
def verify_search_bar_button_is_present():
    assert Driver.driver.check_exists(HomePage.SEARCH_BAR_BUTTON), "Failed to find \'Search Bar\' button"
    logger.info("Search Bar button has been found")


@step("Verify Sign In Button is present on page")
def verify_search_bar_button_is_present():
    assert Driver.driver.check_exists(HomePage.SIGN_IN_BUTTON), "Failed to find \'Search Bar\' button"
    logger.info("Sign In button has been found")


@step("Verify Contact Us Button is present on page")
def verify_search_bar_button_is_present():
    assert Driver.driver.check_exists(HomePage.CONTACT_US_BUTTON), "Failed to find \'Contact Us\' button"
    logger.info("Contact Us button has been found")


@step("Verify Home Page image Button is present on page")
def verify_home_page_image_button_is_present():
    assert Driver.driver.check_exists(HomePage.HOME_PAGE), "Failed to find \'Home Page image\' button"
    logger.info("Home Page image button has been found")
