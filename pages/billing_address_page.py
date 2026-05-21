from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_login_data


class BillingAddressPage(BasePage):
    # Page endpoints
    LOGIN_ENDPOINT = "/login"

    # Login elements
    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")

    # Product elements
    BOOK_PRODUCT = (By.LINK_TEXT, "14.1-inch Laptop")

    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")

    SHOPPING_CART = (By.LINK_TEXT, "Shopping cart")

    TERMS_CHECKBOX = (By.ID, "termsofservice")

    CHECKOUT_BUTTON = (By.ID, "checkout")

    # Billing address elements
    COUNTRY = (By.ID, "BillingNewAddress_CountryId")

    CITY = (By.ID, "BillingNewAddress_City")

    ADDRESS1 = (By.ID, "BillingNewAddress_Address1")

    ZIP_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")

    PHONE_NUMBER = (By.ID, "BillingNewAddress_PhoneNumber")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input.button-1.new-address-next-step-button")

    BILLING_SECTION = (By.ID, "billing-buttons-container")

    def __init__(self, driver):
        super().__init__(driver)

    # Open login page
    def open_login_page(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Login into application
    def login(self):
        email, password = get_login_data()

        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Add product to cart
    def add_product_to_cart(self):
        product = self.wait.until(EC.element_to_be_clickable(self.BOOK_PRODUCT))

        self.driver.execute_script("arguments[0].click();", product)

        add_cart = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))

        self.driver.execute_script("arguments[0].click();", add_cart)

    # Proceed to checkout
    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART)).click()

        checkbox = self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX))

        self.driver.execute_script("arguments[0].click();", checkbox)

        checkout = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))

        self.driver.execute_script("arguments[0].click();", checkout)

    # Enter billing address
    def enter_billing_address(self):
        try:
            country = Select(
                self.wait.until(EC.visibility_of_element_located(self.COUNTRY))
            )

            country.select_by_visible_text("India")

            self.driver.find_element(*self.CITY).send_keys("Bhopal")

            self.driver.find_element(*self.ADDRESS1).send_keys("MP Nagar")

            self.driver.find_element(*self.ZIP_CODE).send_keys("462001")

            self.driver.find_element(*self.PHONE_NUMBER).send_keys("9876543210")

        except:
            print("Existing billing address already selected")

    # Save billing address
    def save_billing_address(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", continue_button)

    # Verify billing address saved
    def verify_billing_address_saved(self):
        billing = self.wait.until(
            EC.visibility_of_element_located(self.BILLING_SECTION)
        )

        return billing.is_displayed()
