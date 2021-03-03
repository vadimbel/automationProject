
import pytest
from base.webDriverFactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    """
    Before test -> print : Running method level setUp .
    After test -> print : Running method level tearDown .
    :return:
    """
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    """
    When user run pytest execution from cmd the last word in the execution order is a browser .
    according to this last word -> this is the browser that will run the test .

    py.test -v -s folders/..../file.py --browser 'name of browser' .

    :param request:
    :param browser:
    :return:
    """
    print("Running one time setUp")
    # create instance of 'WebDriverFactory' then activate 'getWebDriverInstance' function .
    # When user run pytest execution from cmd the last word in the execution order is a browser .
    #     according to this last word -> this is the browser that will run the test .
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

