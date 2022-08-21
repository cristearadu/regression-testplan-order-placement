from getgauge.python import step, data_store
from step_impl.utils import Driver
from core_elements.pages import ShoppingCart
from core_elements import logger

"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify Cart Page has opened")
def verify_cart_page_has_opened():
    assert Driver.driver.check_exists(ShoppingCart.ORDER_STEPS), "Failed to load \'Shopping Cart\' page"
    logger.info("Shopping Cart page has loaded")
