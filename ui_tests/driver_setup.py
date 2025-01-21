from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """
    Set up and return a Selenium WebDriver instance for Chrome.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Optional: Start browser maximized
    options.add_argument("--headless")  # Optional: Run browser in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Useful for running tests in CI/CD pipelines

    # Initialize the driver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver