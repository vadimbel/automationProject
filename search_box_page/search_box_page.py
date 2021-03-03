
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
from utilities.util import Util


class SearchBox(SeleniumDriver):
    """
    this test case is :
    locate the search box and the search button on the main page .
    send key to the search box -> click on the search button .

    if the 'item' that searched on the search box is on 'list_of_items' then the next web page should be able to find
        'list_of_items_display' element on the dom .

    returns True/False according the 'check_search' statements .
    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.action = ActionChains(driver)
        self.util = Util()

    # locators :
    search_box_locator = "//div//input[@type='search']"
    search_button_locator = "//div//button[@type='submit']"
    list_of_items_display = '//*[@id="main"]/div/ul'

    # list of elements that if search them on the search box -> we should be able to find 'list_of_items_display' .
    list_of_items = [
        'armchair', 'chair', 'computer table', 'recliner', 'sofa', 'stool',
        'study table', 'table', 'two seaters'
    ]

    def search_item(self, item):
        """
        get the search box element -> send key to it .
        get the search button element -> click on it .
        goes to the next web page .
        :param item: the item i search on the search box .
        :return:
        """
        self.sendKeys(data=item, locator=self.search_box_locator, locatorType="xpath")
        self.elementClick(locator=self.search_button_locator, locatorType="xpath")

    def check_search(self, item):
        """
        the function returns True : if the 'item' searched on the searched box is on the 'list_of_items' list and
        the 'list_of_items_display_element' element on the dom is displayed .
        the function returns False : on any other case .
        :param item: searched item on the search box .
        :return: True/False .
        """
        # search the element on the dom that supposed to contain the products .
        list_of_items_display_element = self.getElement(locator=self.list_of_items_display, locatorType="xpath")

        # if the element on the dom is not .
        if list_of_items_display_element == None:
            self.log.info("#### ITEMS LIST IS NONE #####")
        else:
            self.log.info("#### ITEMS LIST IS FOUND #####")

        # boolean variable initialized to be False -> item is not on the list .
        statement = False

        # check if 'item' we searched in the search box is on the list -> convert 'statement' = True
        for i in self.list_of_items:
            if item == i:
                self.log.info("item that was searched is on the list .")
                statement = True
                break

        # the item that i searched is equal to one of the items on the list and i found the element on the dom .
        # then the item that was searched displaying items on the web page -> return True .
        if statement and list_of_items_display_element:
            self.log.debug("ITEM : {} is on the list and ITEM LIST in FOUND .".format(item))
            self.log.debug("### RETURN TRUE .")
            return True

        # item searched is on the list but the element on the dom is not found .
        elif statement and list_of_items_display_element == None:
            self.log.error("ITEM {} is on the list . ### ITEM LIST NOT FOUND .".format(item))
            self.log.debug("#### RETURN FALSE .")
            return False

        # item searched is not on the list but the element on the dom was found .
        elif statement == False and list_of_items_display_element != None:
            self.log.error("ITEM {} is NOT on the list . ### ITEM LIST is FOUND .".format(item))
            return False

        elif statement == False and list_of_items_display_element == None:
            self.log.info("ITEM {} is not on the list . ### ITEM LIST NOT FOUND .".format(item))
            return True

        else:
            self.log.error("WENT TO ELSE STATEMENT . SOMETHING WRONG .")
            return False















