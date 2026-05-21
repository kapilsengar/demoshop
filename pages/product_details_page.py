from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    # Product page endpoint
    PRODUCT_ENDPOINT = "/141-inch-laptop"

    # Web elements
    PRODUCT_TITLE = (
        By.CLASS_NAME,
        "product-name"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "span.price-value"
    )

    ADD_TO_CART = (
        By.ID,
        "add-to-cart-button-31"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Open product page
    def open_product_page(self):
        self.open_url(self.PRODUCT_ENDPOINT)

    # Verify product title
    def verify_product_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

        return (
            "14.1-inch Laptop"
            in title.text
        )

    # Verify add to cart button
    def verify_add_to_cart(self):
        button = self.wait.until(
            EC.visibility_of_element_located(
                self.ADD_TO_CART
            )
        )

        return button.is_displayed()