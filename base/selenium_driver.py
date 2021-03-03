
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

"""
this file implements basic functions of selenium web driver .
the functions on this file will be used in multiple test cases .
"""

class SeleniumDriver(object):

    # use the logger from 'utilities.custom_logger' file -> create a log to debug the program .
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            # if the directory does not exists then create one .
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            # then save it in this directory and update the log .
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getByType(self, locatorType):
        """
        This function will return the locator type of specific element .
        :param locatorType:
        :return:
        """
        # convert the locator to lower case then return its type .
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        """
        This function will find an element and return it using another function called 'getByType' .
        :param locator: The element XPATH .
        :param locatorType: XPATH/ID/TEXT ... of the element .
        :return:
        """
        element = None
        try:
            # convert the locator to lower case and get is type using other function .
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)

            # then finds the element .
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not Found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        this function gets a list of elements using 'locator' and 'locatorType' .
        :param locator:
        :param locatorType:
        :return:
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def moveToElement(self, name, locator="", locatorType="id", element=None):
        """
        finds an element and move to it using 'action' class .
        :param name:
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            self.action.move_to_element(element).perform()
            self.log.info("Moved to {} element .".format(name))
        except:
            self.log.error("Cannot move to {} element .".format(name))
            print_stack()


    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element .
        Either provide element or a combination of locator and locatorType

        This function will click on element .
        the function will find an element using 'getElement' function -> then click on it .
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            # if locator is not empty -> i find this element then click it .
            # if i provide an element then it click it .
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element .
        Either provide element or a combination of locator and locatorType

        This function will send key to element .
        the function will find an element using 'getElement' function -> then click on it .
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element .
        Either provide element or a combination of locator and locatorType .
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present .
        Either provide element or a combination of locator and locatorType .

        This function will check if the element is present on the web page .
        :param locator: the locator of the element .
        :param byType: XPATH/ID/TEXT ....
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed .
        Either provide element or a combination of locator and locatorType .
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        (another way to do this is the function 'isElementPresent')
        This function will check if the element is present on the web page .
        :param locator: the locator of the element .
        :param byType: XPATH/ID/TEXT ....
        :return:
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        """
        Explicit wait for a specific element .
        :param locator: the locator of the element .
        :param locatorType: XPATH/ID/TEXT ....
        :param timeout: amount of time we will wait .
        :param pollFrequency:
        :return:
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +" :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")



