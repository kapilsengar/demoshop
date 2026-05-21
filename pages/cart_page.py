from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    # Homepage endpoint
    HOME_ENDPOINT = "/"

    # Web elements
    PRODUCT = (
        By.LINK_TEXT,
        "Build your own cheap computer"
    )

    ADD_TO_CART_BUTTON = (
        By.ID,
        "add-to-cart-button-72"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "p.content"
    )

    SHOPPING_CART_LINK = (
        By.CSS_SELECTOR,
        "span.cart-label"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Open homepage
    def open_homepage(self):
        self.open_url(self.HOME_ENDPOINT)

    # Add product to cart
    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        ).click()

    # Verify success message
    def verify_success_message(self):
        success = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

        return "The product has been added" in success.text