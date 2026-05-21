from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    # Contact page endpoint
    CONTACT_ENDPOINT = "/contactus"

    # Web elements
    FULL_NAME = (By.ID, "FullName")

    EMAIL = (By.ID, "Email")

    ENQUIRY = (By.ID, "Enquiry")

    SUBMIT_BUTTON = (By.NAME, "send-email")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    def __init__(self, driver):
        super().__init__(driver)

    # Open contact page
    def open_contact_page(self):
        self.open_url(self.CONTACT_ENDPOINT)

    # Submit contact form
    def submit_contact_form(self):
        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME)).send_keys(
            "Aditya Raj"
        )

        self.driver.find_element(*self.EMAIL).send_keys("ram444@gmail.com")

        self.driver.find_element(*self.ENQUIRY).send_keys(
            "This is automation testing enquiry"
        )

        submit = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))

        self.driver.execute_script("arguments[0].click();", submit)

    # Verify successful submission
    def verify_contact_submission(self):
        success = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        return success.is_displayed()
