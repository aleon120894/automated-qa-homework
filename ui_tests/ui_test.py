import pytest
from page_object import ExamplePage
import driver_setup
from test_data import TestData


@pytest.fixture
def setup_driver():
    """
    Fixture to set up the WebDriver instance.
    """
    driver = driver_setup.get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def example_page(setup_driver):
    """
    Fixture to initialize the ExamplePage object and navigate to the page.
    """
    page = ExamplePage(setup_driver)
    page.open()
    return page


def test_example_page_title(example_page):
    """
    Test to verify the header of the example page.
    """
    header_text = example_page.check_header()
    assert header_text == TestData.text_header, f"Header mismatch! Found: {header_text}"


def test_example_page_text(example_page):
    """
    Test to verify the text content of the example page.
    """
    text_content = example_page.check_text()
    assert text_content == TestData.text_content, f"Text mismatch! Found: {text_content}"

