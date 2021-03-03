
from pages.search_box_page.search_box_page import SearchBox
from pages.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SearchBoxCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.search = SearchBox(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToPracticePage()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\vadim\PycharmProjects\\automationPracticeStore.com\\itemsToSearch.csv"))
    @unpack
    def test_search_box(self, item):
        self.search.search_item(item=item)
        result = self.search.check_search(item=item)
        self.ts.mark(result, "######### ITEM IS ON THE LIST AND LOCATOR FOUND .")
        self.ts.markFinal("######## SEARCH BOX TEST PASSED .")


