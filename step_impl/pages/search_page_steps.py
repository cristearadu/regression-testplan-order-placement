from getgauge.python import step
from step_impl.utils import Driver
from core_elements.pages import SearchPage
from core_elements.logging_element import logger


"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify Search Page has opened")
def verify_search_page_has_opened():
    assert Driver.driver.check_exists(SearchPage.PRODUCT_LIST), "Failed to load \'Search Page\'"
    logger.info("Search page has loaded")
