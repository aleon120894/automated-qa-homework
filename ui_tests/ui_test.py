import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from page_object import ExamplePage
import driver_setup


driver = driver_setup.get_driver()
page = ExamplePage(driver)

@pytest.fixture
def driver_setup():
    page.open()


@pytest.fixture
def text_example_page():
    page.check_header()