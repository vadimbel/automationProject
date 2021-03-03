
"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

if i am using assert in one test case then when one assert returns false then all the asserts after him wont be checked
to avoid this i am using this file .

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        """
        This fucntion will get 'result' and 'resultMessage' .
        then append the 'result' to the result list and write the result message to the log .
        :param result: result .
        :param resultMessage: message that entered from where the function activated .
        :return: None .
        """
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + "Test Has Passed !")
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
                    # if the test case failed -> i want to take a screenshot of the page where it failed .
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        if "FAIL" in self.resultList:
            # print error in the log for this test .
            self.log.error(testName + " ### TEST FAILED\n")
            self.resultList.clear()
            # then it will show that this specific test is failed (on terminal/cmd) and go to next test .
            assert False == True
        else:
            # print success in the log for this test .
            self.log.info(testName + " ### TEST SUCCESSFUL\n")
            self.resultList.clear()
            # then it will show that this specific test passed successful and go to next test .
            assert True == True



