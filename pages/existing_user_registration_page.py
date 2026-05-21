from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ExistingUserRegistrationPage(BasePage):
    # Register page endpoint
    REGISTER_ENDPOINT = "/register"

    # Web elements
    GENDER = (
        By.ID,
        "gender-male"
    )

    FIRST_NAME = (
        By.ID,
        "FirstName"
    )

    LAST_NAME = (
        By.ID,
        "LastName"
    )

    EMAIL = (
        By.ID,
        "Email"
    )

    PASSWORD = (
        By.ID,
        "Password"
    )

    CONFIRM_PASSWORD = (
        By.ID,
        "ConfirmPassword"
    )

    REGISTER_BUTTON = (
        By.ID,
        "register-button"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "div.validation-summary-errors"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Open register page
    def open_register_page(self):
        self.open_url(self.REGISTER_ENDPOINT)

    # Enter existing user details
    def enter_existing_user_details(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.GENDER
            )
        ).click()

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys("Aditya")

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys("Raj")

        self.driver.find_element(
            *self.EMAIL
        ).send_keys("ram444@gmail.com")

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys("Pass@123")

        self.driver.find_element(
            *self.CONFIRM_PASSWORD
        ).send_keys("Pass@123")

    # Click register button
    def click_register(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.REGISTER_BUTTON
            )
        ).click()

    # Verify registration failure
    def verify_registration_failed(self):
        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return (
            "The specified email already exists"
            in error.text
        )