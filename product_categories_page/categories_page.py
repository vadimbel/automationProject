
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class ProductCategoriesCheck(SeleniumDriver):
    """
    test 1 :
        on shop page -> product categories -> there are 10 categories .
        on the right of each category there is a number in format (number) -> symbolize the amount of items from
        this category .
        this test checks if the web page display the right amount of item for each category .
        using : 'click_on_category' , 'check_displayed_item_for_category' , 'check_displayed_items_amount' , 'check_amount' .

    test 2 :
        on shop page -> product categories -> there are 10 categories .
        this test click on each category then check the item displayed for every category supposed to displayed .
        using : 'click_on_category' , 'check_items_displayed' .

    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    # locator :
    product_categories_locator = '//*[@id="woocommerce_product_categories-1"]/ul/li/a[contains(text(), "{}")]'
    items_amount_locator = '//*[@id="woocommerce_product_categories-1"]/ul/li[{}]/span'

    # items_display_locators :
    items_amount_display_locator = '//*[@id="main"]/div/ul/li'
    items_text_locator = '//*[@id="main"]/div/ul/li/div//h2'

    list_chair = [
        "chair", "chairs", "recliner", "couch", "armchair", "stool"
    ]

    list_sofa = [
        "sofa", "chair", "couch"
    ]

    list_table = [
        "table"
    ]

    list_two_seaters = [
        "sofa", "chair"
    ]

    def click_on_category(self, category):
        """
        used in : test case 1 , test case 2 .
        this function click on 'category' element displayed under 'Product categories' on
        https://letskodeit.com/automationpractice/shop/ web page .
        :param category:
        :return:
        """
        self.elementClick(locator=self.product_categories_locator.format(category), locatorType="xpath")
        self.util.sleep(2)

    def check_displayed_item_for_category(self, number):
        """
        used in : test case 1 .
        this function return the text located on the right of each category under 'Product categories' on
        https://letskodeit.com/automationpractice/shop/ web page .
        :param number:
        :return:
        """
        item_amount_element = self.getElement(locator=self.items_amount_locator.format(number), locatorType="xpath")
        item_amount_text = item_amount_element.text
        self.log.info("TEXT AMOUNT IS : {}".format(item_amount_text))
        return item_amount_text

    def check_displayed_items_amount(self):
        """
        used in : test case 1 .
        this function will get the amount of item displayed on the web page for each category .
        (the elements displayed after the automation clicks on on of the categories .)
        :return:
        """
        items = self.getElementList(locator=self.items_amount_display_locator, locatorType="xpath")
        self.log.info("ITEMS AMOUNT : {}".format(len(items)))
        return len(items)

    def check_amount(self, items_amount, displayed_items_amount):
        """
        used in : test case 1 .
        checks if the returned values from 'check_displayed_item_for_category' , 'check_displayed_items_amount' are
        the same .
        :param items_amount:
        :param displayed_items_amount:
        :return:
        """
        if str(items_amount) == "({})".format(displayed_items_amount):
            return True
        else:
            return False

    def check_items_displayed(self, category):
        """
        used in : test case 2 .
        this function gets list of items that displayed for some category -> get all text of the items displayed ->
        according to the category check if there is any items that Shouldn't be displayed .
        :return:
        """
        # gets the list if texts .
        all_items = self.getElementList(locator=self.items_text_locator, locatorType="xpath")
        self.log.info("######## ITEMS DISPLAYED : #########")

        # print to the log all the texts .
        for i in all_items:
            self.log.info("TEXT : {}".format(i.text))

        # if it finds one text that should not be displayed then 'overall_statement' will be false .
        # if all the items should be displayed then 'overall_statement' stay true then will be returned at the end .
        overall_statement = True
        # using 'statement' boolean variable to spot if the specific item should or Shouldn't be displayed .
        statement = False

        # if the category clicked is : chair/stool/armchair/recliner
        if str(category).lower() == "chair" or str(category).lower() == "stool" or str(category).lower() == "armchair" or str(category).lower() == "recliner":
            # loop inside every items (the text of the item) -> get the text .
            for i in all_items:
                text = i.text
                # check if any key word from 'list_chair' is in this text .
                for item in self.list_chair:
                    if item in str(text).lower():
                        statement = True

                # if 'statement' stay false -> this items should not be in this category .
                if statement == False:
                    self.log.error("ITEM : {} should not be displayed .".format(text))
                    overall_statement = False

                statement = False

        # same comments as above only for category : table/study table/computer table .
        elif str(category).lower() == "computer table" or str(category).lower() == "study table" or str(category).lower() == "table":
            for i in all_items:
                text = i.text
                for item in self.list_table:
                    if item in str(text).lower():
                        statement = True

                if statement == False:
                    self.log.error("ITEM : {} should not be displayed .".format(text))
                    overall_statement = False

                statement = False

        # same comments as above only for category : two seaters .
        elif str(category).lower() == "two seaters":
            for i in all_items:
                text = i.text
                for item in self.list_two_seaters:
                    if item in str(text).lower():
                        statement = True

                if statement == False:
                    self.log.error("ITEM : {} should not be displayed .".format(text))
                    overall_statement = False

                statement = False

        # same comments as above only for category : sofa .
        elif str(category).lower() == "sofa":
            for i in all_items:
                text = i.text
                for item in self.list_sofa:
                    if item in str(text).lower():
                        statement = True

                if statement == False:
                    self.log.error("ITEM : {} should not be displayed .".format(text))
                    overall_statement = False

                statement = False

        return overall_statement






