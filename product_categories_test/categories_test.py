
from pages.product_categories_page.categories_page import ProductCategoriesCheck
from pages.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ProductCategoriesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.category = ProductCategoriesCheck(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        """
        navigate to categories page after every test in this file .
        :return:
        """
        self.nav.navigateToProductCategoriesPage()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\vadim\PycharmProjects\\automationPracticeStore.com\\categories.csv"))
    @unpack
    def test_product_categories(self, category, number):
        """
        this test will check every category from 'categories.csv' file according the explanations .
        :param category: the category the automation checks .
        :param number: variable to locate the right category using xpath .
        :return:
        """
        # clicks on a 'category' .
        self.category.click_on_category(category=category)
        # get the text (number) located on the right of the 'category' text .
        items_amount = self.category.check_displayed_item_for_category(number=number)
        # after automation clicks on category -> get the number of items displayed for this category .
        displayed_items_amount = self.category.check_displayed_items_amount()
        # check if the numbers are equal .
        result = self.category.check_amount(items_amount=items_amount, displayed_items_amount=displayed_items_amount)
        self.ts.mark(result, "######### INVALID amount of items .")
        # then checks the text under every item displayed -> check if this item should be displayed .
        result = self.category.check_items_displayed(category=category)
        self.ts.mark(result, "######### INVALID item displayed .")
        self.ts.markFinal("######## ITEMS AMOUNT TEST .")
