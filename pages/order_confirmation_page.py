from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.test_data import get_login_data


class OrderConfirmationPage(BasePage):
    # Page endpoints
    LOGIN_ENDPOINT = "/login"
    PRODUCT_ENDPOINT = "/blue-jeans"
    CART_ENDPOINT = "/cart"

    # Login elements
    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    # Product elements
    ADD_TO_CART = (
        By.XPATH,
        "//input[contains(@class,'add-to-cart-button')]"
    )

    SHOPPING_CART = (
        By.LINK_TEXT,
        "Shopping cart"
    )

    TERMS_CHECKBOX = (
        By.ID,
        "termsofservice"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    # Billing elements
    COUNTRY = (
        By.ID,
        "BillingNewAddress_CountryId"
    )

    CITY = (
        By.ID,
        "BillingNewAddress_City"
    )

    ADDRESS1 = (
        By.ID,
        "BillingNewAddress_Address1"
    )

    ZIP_CODE = (
        By.ID,
        "BillingNewAddress_ZipPostalCode"
    )

    PHONE_NUMBER = (
        By.ID,
        "BillingNewAddress_PhoneNumber"
    )

    BILLING_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.new-address-next-step-button"
    )

    # Shipping elements
    SHIPPING_METHOD_RADIO = (
        By.XPATH,
        "//input[@name='shippingoption']"
    )

    SHIPPING_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.shipping-method-next-step-button"
    )

    # Payment elements
    PAYMENT_METHOD_RADIO = (
        By.XPATH,
        "//input[@name='paymentmethod']"
    )

    PAYMENT_METHOD_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.payment-method-next-step-button"
    )

    PAYMENT_INFO_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.payment-info-next-step-button"
    )

    # Order elements
    CONFIRM_ORDER_BUTTON = (
        By.CSS_SELECTOR,
        "input.button-1.confirm-order-next-step-button"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.title"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Open login page
    def open_login_page(self):
        self.open_url(self.LOGIN_ENDPOINT)

    # Login into application
    def login(self):
        email, password = get_login_data()

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).send_keys(email)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    # Add product to cart
    def add_product(self):
        self.open_url(self.PRODUCT_ENDPOINT)

        add_cart = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_cart
        )

    # Proceed to checkout
    def proceed_checkout(self):
        self.open_url(self.CART_ENDPOINT)

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.TERMS_CHECKBOX
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        checkout = self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

    # Fill billing address
    def fill_billing_address(self):
        try:
            country = Select(
                self.wait.until(
                    EC.visibility_of_element_located(
                        self.COUNTRY
                    )
                )
            )

            country.select_by_visible_text(
                "India"
            )

            self.driver.find_element(
                *self.CITY
            ).send_keys("Bhopal")

            self.driver.find_element(
                *self.ADDRESS1
            ).send_keys("MP Nagar")

            self.driver.find_element(
                *self.ZIP_CODE
            ).send_keys("462001")

            self.driver.find_element(
                *self.PHONE_NUMBER
            ).send_keys("9876543210")

        except:
            print("Existing address selected")

    # Continue billing
    def continue_billing(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.BILLING_CONTINUE
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # Complete checkout steps
    def complete_checkout_steps(self):
        try:
            shipping_method = self.wait.until(
                EC.element_to_be_clickable(
                    self.SHIPPING_METHOD_RADIO
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                shipping_method
            )

            shipping_continue = self.wait.until(
                EC.element_to_be_clickable(
                    self.SHIPPING_CONTINUE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                shipping_continue
            )

        except:
            print("Shipping method skipped")

        try:
            payment_method = self.wait.until(
                EC.element_to_be_clickable(
                    self.PAYMENT_METHOD_RADIO
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_method
            )

            payment_continue = self.wait.until(
                EC.element_to_be_clickable(
                    self.PAYMENT_METHOD_CONTINUE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_continue
            )

        except:
            print("Payment method skipped")

        try:
            payment_info = self.wait.until(
                EC.element_to_be_clickable(
                    self.PAYMENT_INFO_CONTINUE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_info
            )

        except:
            print("Payment info skipped")

    # Confirm order
    def confirm_order(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_ORDER_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # Verify successful order
    def verify_order_success(self):
        success = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

        return (
            "Your order has been successfully processed!"
            in success.text
        )