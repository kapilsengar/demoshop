from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_login_data


class AddressPage(BasePage):
    # Page endpoints
    LOGIN_ENDPOINT = "/login"
    ADDRESS_ENDPOINT = "/customer/addresses"

    # Login elements
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")

    # Address elements
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "input.button-1.add-address-button")

    FIRST_NAME = (By.ID, "Address_FirstName")

    LAST_NAME = (By.ID, "Address_LastName")

    EMAIL_ADDRESS = (By.ID, "Address_Email")

    COMPANY = (By.ID, "Address_Company")

    COUNTRY = (By.ID, "Address_CountryId")

    CITY = (By.ID, "Address_City")

    ADDRESS1 = (By.ID, "Address_Address1")

    ZIP_CODE = (By.ID, "Address_ZipPostalCode")

    PHONE_NUMBER = (By.ID, "Address_PhoneNumber")

    SAVE_BUTTON = (By.CSS_SELECTOR, "input.button-1.save-address-button")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.section.address-item")

    # Open login page
    def open_login_page(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Login into application
    def login(self):
        email, password = get_login_data()

        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Open address page
    def open_addresses(self):
        self.open_url(self.ADDRESS_ENDPOINT)

    # Click add new address
    def click_add_new_address(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_NEW_BUTTON)).click()

    # Fill address form
    def fill_address_form(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(
            "Aditya"
        )

        self.driver.find_element(*self.LAST_NAME).send_keys("Raj")

        self.driver.find_element(*self.EMAIL_ADDRESS).send_keys("ram444@gmail.com")

        self.driver.find_element(*self.COMPANY).send_keys("Wipro")

        country = Select(self.driver.find_element(*self.COUNTRY))

        country.select_by_visible_text("India")

        self.driver.find_element(*self.CITY).send_keys("Bhopal")

        self.driver.find_element(*self.ADDRESS1).send_keys("MP Nagar")

        self.driver.find_element(*self.ZIP_CODE).send_keys("462001")

        self.driver.find_element(*self.PHONE_NUMBER).send_keys("9876543210")

    # Save address
    def save_address(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    # Verify address added
    def verify_address_added(self):
        success = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        return success.is_displayed()
