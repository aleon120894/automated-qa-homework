from pygments.lexers.robotframework import HEADING
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ExamplePage:

    def __init__(self, driver : WebDriver):

        self.driver = driver
        self.url = "https://example.com/"

    HEADING = (By.CSS_SELECTOR, "body > div > h1")
    HEADING_TEXT = (By.CSS_SELECTOR, "body > div > p:nth-child(2)")

    def open(self):
        """
        Open the example.com page.
        """
        self.driver.get(self.url)


    def check_header(self):

        header = self.driver.find_element(HEADING)
        assert header.text == "Example Domain"

