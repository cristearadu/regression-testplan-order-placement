from getgauge.python import before_scenario, after_scenario, step
from step_impl.utils.init_driver import Driver
from settings import WEBSITE


@before_scenario
def open_driver_before_scenario():
    Driver.init_driver()
    Driver.driver.get(WEBSITE)


@after_scenario
def close_driver_after_scenario():
    Driver.close_driver()
