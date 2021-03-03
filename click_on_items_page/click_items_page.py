
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
from utilities.util import Util

class ClickItems(SeleniumDriver):
    """
    this class implements this test case :
        automation will click on one of the elements then check if the element added successfully to the cart and the
        price is valid .
    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.action = ActionChains(driver)
        self.util = Util()

    # locators :

    # element from the main page (chair , table ...) .
    element_locator = '//*[@id="post-19"]/div/div/div/div/section[3]/div/div/div/div/div/div[4]/div//h2[contains(text(), "{0}")]'
    # after click on some element -> on the page that pops up -> locator for 'add to cart' .
    add_to_cart_locator = "//button[contains(text(), 'Add to cart')]"
    # at the top of all pages -> cart icon locator .
    cart_locator = '//*[@id="ast-site-header-cart"]/div[1]/a/div/span'
    # check the number inside the cart icon -> if the text inside it is greater then 0 -> item added to cart .
    text_in_cart_locator = '//*[@id="ast-site-header-cart"]/div[1]/a/div/span'
    # plus_locator on add to cart page .
    plus_locator = '//div[2]/form/div/a[2]'
    # price_locator
    price_locator = '//*[@id="post-5"]/div/div/form/table/tbody/tr[1]/td[4]/span'
    # total_locator
    total_locator = '//*[@id="post-5"]/div/div/div[2]/div/table/tbody/tr[2]/td/strong/span'

    def click_on_item(self, item):
        """
        automation will locate an 'item' -> click on it .
        the item will be added to the cart .
        :param item: The item from the items collection .
        :return:
        """
        # using method from 'base.selenium_driver import SeleniumDriver' file -> find element and click on it .
        self.elementClick(locator=self.element_locator.format(item), locatorType="xpath")
        self.util.sleep(2)

    def add_to_cart(self, amount):
        """
        Automation finds an elements from the collection -> click on the element -> on specific product page -> finds
        the 'plus' element -> and click on it accordint to the 'amount' entered .
        :param amount: add 'amount' elements to the card .
        :return:
        """
        # get the 'plus' element every time and click on it .
        for i in range(0, int(amount)):
            element = self.getElement(locator=self.plus_locator, locatorType="xpath")
            self.elementClick(element=element)
            self.util.sleep(1)
        # after the automation done clicking on the 'plus' element -> finds 'add to cart' element and click it .
        self.elementClick(locator=self.add_to_cart_locator, locatorType="xpath")
        self.util.sleep(2)
        # then click on the cart icon on the top right of the web page .
        self.elementClick(locator=self.cart_locator, locatorType="xpath")

    def verify_item_added_successfully(self, amount):
        """
        this function checks if the right number of items added to the cart .
        after the automation add 'amount' of specific items to the cart -> the function checks 2 things :
        1. there is 'amount' elements on the cart on the final page before purchase .
        2. the price is valid by check if 'total_locator' / 'price_locator' = 'amount' + 1 .
        :param amount:
        :return:
        """
        # two boolean statements to check 1 and 2 .
        statement_one = False
        statement_two = False

        # get the text inside cart icon .
        text_in_cart = self.getElement(self.text_in_cart_locator, "xpath")
        text = text_in_cart.text
        self.log.info("THE TEXT IS : {}".format(text))
        # the text should be amount + 1 if the items added successfully .
        if int(text) == int(amount)+1:
            statement_one = True
        else:
            statement_one = False

        # get the 'price' element per one unit and the 'total price' element .
        price_element = self.getElement(locator=self.price_locator, locatorType="xpath")
        total_price_element = self.getElement(locator=self.total_locator, locatorType="xpath")
        price_text = price_element.text[1:]
        total_price_text = total_price_element.text[1:]
        self.log.info("price per one : {} ||| total price : {}".format(price_text, total_price_text))
        # make the math check and initialize 'statement_two' boolean variable .
        if float(total_price_text) / float(price_text) == float(amount) + 1:
            statement_two = True
        else:
            statement_two = False

        # if both statements are 'True' then the test passed .
        if statement_one and statement_two == True:
            self.log.info("Items added successfully and price is valid .")
            return True
        # if one of the tests (or both) are false then -> print the right message to the log and return false .
        else:
            if statement_one == False:
                self.log.info("Add to cart test did not passed successfully .")
            if statement_two == False:
                self.log.info("Price test did not passed successfully .")
            return False




