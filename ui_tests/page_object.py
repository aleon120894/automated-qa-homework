from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ExamplePage:

    def __init__(self, driver: WebDriver):
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
        """
        Check the header of the page and assert its text.
        Return the header text for further verification.
        """
        header = self.driver.find_element(*self.HEADING)
        header_text = header.text
        return header_text

    def check_text(self):
        """
        Check the header of the page and assert its text.
        Return the header text for further verification.
        """

        text = self.driver.find_element(*self.HEADING_TEXT)
        text_content = text.text
        return text_content
