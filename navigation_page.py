
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class NavigationPage(SeleniumDriver):
    """
    this file created to navigate to different web pages according the the tests .
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # my
    def navigateToPracticePage(self):
        """
        navigate to the main page .
        :return:
        """
        self.driver.get('https://letskodeit.com/automationpractice/')
        self.log.info("Navigate to https://letskodeit.com/automationpractice/ -> Main page .")

    def navigateToProductCategoriesPage(self):
        """
        navigate to categories page/shop page .
        :return:
        """
        self.driver.get('https://letskodeit.com/automationpractice/shop/')
        self.log.info("Navigate to https://letskodeit.com/automationpractice/shop/ -> Shop page .")




