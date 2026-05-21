from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_register_data


class RegisterPage(BasePage):
    # Register page endpoint
    REGISTER_ENDPOINT = "/register"

    # Web elements
    GENDER = (By.ID, "gender-male")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    # Open register page
    def open_register_page(self):
        self.open_url(self.REGISTER_ENDPOINT)

    # Enter registration details
    def enter_registration_details(self):
        first_name, last_name, email, password = get_register_data()

        self.wait.until(EC.element_to_be_clickable(self.GENDER)).click()

        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)

    # Click register button
    def click_register(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()

    # Verify successful registration
    def verify_registration(self):
        success = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        return "Your registration completed" in success.text
