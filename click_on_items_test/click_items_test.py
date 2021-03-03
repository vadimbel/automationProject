
from pages.click_on_items_page.click_items_page import ClickItems
from pages.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ClickItemsCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.items = ClickItems(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        """
        after every test -> the web page will be navigate to practice page -> main page .
        :return:
        """
        self.nav.navigateToPracticePage()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\vadim\PycharmProjects\\automationPracticeStore.com\\datafile.csv"))
    @unpack
    def test_click_on_item(self, item, amount):
        """
        using ddt and get the items from 'datafile.csv' file .
        :param item: the item the automation will be checking .
        :param amount: amount of time this item will be added to the cart .
        :return:
        """
        self.items.click_on_item(item=item)
        self.items.add_to_cart(amount=amount)
        result1 = self.items.verify_item_added_successfully(amount=amount)
        self.ts.mark(result1, "######### ITEM DID NOT ADDED SUCCESSFULLY .")
        self.ts.markFinal("##### ADD ITEM AND TOTAL PRICE TEST CHECK")




