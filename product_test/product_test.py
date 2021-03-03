
from pages.product_page.product_page import ProductButtonsCheck
from pages.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ProductButtonCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.product = ProductButtonsCheck(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        """
        naviage to practice page after every test .
        :return:
        """
        self.nav.navigateToPracticePage()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\vadim\PycharmProjects\\automationPracticeStore.com\\option.csv"))
    @unpack
    def test_product_tag_sofa(self, option):
        self.product.check_tag(option)
        result = self.product.check_elements_text(option)
        self.ts.mark(result, "######### PRODUCT {} TEST DID NOT PASSED .".format(option))
        self.ts.markFinal("######## PRODUCT {} TEST .".format(option))




