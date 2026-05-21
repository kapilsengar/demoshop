from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_login_data


class LogoutPage(BasePage):
    # Login page endpoint
    LOGIN_ENDPOINT = "/login"

    # Web elements
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")

    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    LOGIN_LINK = (By.LINK_TEXT, "Log in")

    def __init__(self, driver):
        super().__init__(driver)

    # Open login page
    def open_login_page(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Login with valid credentials
    def login(self):
        email, password = get_login_data()

        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Click logout button
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    # Verify successful logout
    def verify_logout(self):
        login_link = self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))

        return login_link.is_displayed()
