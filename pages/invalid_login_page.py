from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_invalid_login_data


class InvalidLoginPage(BasePage):
    # Login page endpoint
    LOGIN_ENDPOINT = "/login"

    # Web elements
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.validation-summary-errors")

    def __init__(self, driver):
        super().__init__(driver)

    # Open login page
    def open_login_page(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Enter invalid credentials
    def enter_invalid_credentials(self):
        email, password = get_invalid_login_data()

        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

    # Click login button
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    # Verify error message
    def verify_error_message(self):
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))

        return "Login was unsuccessful" in error.text
