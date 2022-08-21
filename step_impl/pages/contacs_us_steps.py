from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages import ContactUsPage
from core_elements.logging_element import logger


@step("Verify Contact us page has loaded")
def contact_us_page_has_loaded():
    assert Driver.driver.check_exists(ContactUsPage.MESSAGE_TEXTBOX), "Failed to load \'Contact Us\' page"
    logger.info("Contact us page has loaded")
