from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.test_data import get_login_data


class LoginPage(BasePage):
    # Login page endpoint
    LOGIN_ENDPOINT = "/login"

    # Web elements
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    # Open login page
    def open(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Enter credentials from database
    def enter_credentials(self):
        email, password = get_login_data()

        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    # Click login button
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Verify successful login
    def is_logout_visible(self):
        return self.driver.find_element(*self.LOGOUT_LINK).is_displayed()
