
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class ProductButtonsCheck(SeleniumDriver):
    """
    this class checks the 'product' tags (chair/table/sofa elements) .
    the test move to 'product' element -> click on one of the elements (chair/table/sofa elements) -> check the displayed
    items (check that all the items displayed are valid) .
    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    # locators :
    product_tag_locator = '//*[@id="menu-item-37"]/a'
    product_sofa_locator = '//*[@id="menu-item-228"]/a'
    product_chair_locator = '//*[@id="menu-item-102"]/a'
    product_table_locator = '//*[@id="menu-item-292"]/a'

    all_items = '//*[@id="main"]/div/ul/li//h2'

    list_for_sofa_check = [
        'sofa', 'couch', 'chair'
    ]

    list_for_chair_check = [
        'chair', 'recliner', 'couch', 'stool'
    ]

    list_for_table_check = [
        'table'
    ]

    def check_tag(self, option):
        """
        moves to 'product element' -> moves to the 'option' item and click it .
        :param option: (chair/table/sofa) .
        :return:
        """
        self.moveToElement(name="product", locator=self.product_tag_locator, locatorType="xpath")
        self.util.sleep(2)
        if option == 'sofa':
            self.moveToElement(name=option, locator=self.product_sofa_locator, locatorType="xpath")
            self.util.sleep(2)
            self.elementClick(self.product_sofa_locator, "xpath")
        elif option == 'chair':
            self.moveToElement(name=option, locator=self.product_chair_locator, locatorType="xpath")
            self.util.sleep(2)
            self.elementClick(self.product_chair_locator, "xpath")
        elif option == 'table':
            self.moveToElement(name=option, locator=self.product_table_locator, locatorType="xpath")
            self.util.sleep(2)
            self.elementClick(self.product_table_locator, "xpath")

    def check_elements_text(self, option):
        """
        according to the selected option -> check the text of the items displayed .
        :param option:
        :return:
        """
        # gets all the item .
        items = self.getElementList(locator=self.all_items, locatorType="xpath")

        # for each item in the items list .
        for item in items:
            # get the text .
            text = item.text
            self.log.debug("check text : {}".format(text))

            # create boolean variable -> if i find an item that do not contain any word from 'list_for_sofa_check'
            # then i return false .
            statement = False

            # according to the option entered (option = chair/table/sofa on product element on main page)
            if option == 'sofa':
                for word in self.list_for_sofa_check:
                    # text contains one of the word -> 'statement' = True -> go for the next element .
                    if word in str(text).lower():
                        statement = True
                        break
                # if the text did not become True in the loop above -> this item should not be in the display .
                if statement == False:
                    self.log.error("ITEM with text : {}  -> should not be in the display .".format(text))
                    return False

            elif option == 'table':
                for word in self.list_for_table_check:
                    # text contains one of the word -> 'statement' = True -> go for the next element .
                    if word in str(text).lower():
                        statement = True
                        break
                # if the text did not become True in the loop above -> this item should not be in the display .
                if statement == False:
                    self.log.error("ITEM with text : {}  -> should not be in the display .".format(text))
                    return False

            elif option == 'chair':
                for word in self.list_for_chair_check:
                    # text contains one of the word -> 'statement' = True -> go for the next element .
                    if word in str(text).lower():
                        statement = True
                        break
                # if the text did not become True in the loop above -> this item should not be in the display .
                if statement == False:
                    self.log.error("ITEM with text : {}  -> should not be in the display .".format(text))
                    return False

        return True




