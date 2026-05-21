from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    # Common base URL for all pages
    BASE_URL = "https://demowebshop.tricentis.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Open complete URL using endpoint
    def open_url(self, endpoint):
        self.driver.get(self.BASE_URL + endpoint)
