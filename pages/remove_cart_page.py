from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RemoveCartPage(BasePage):
    # Page endpoints
    HOME_ENDPOINT = "/"
    PRODUCT_ENDPOINT = "/build-your-cheap-own-computer"
    CART_ENDPOINT = "/cart"

    # Web elements
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[contains(@class,'add-to-cart-button')]")

    SHOPPING_CART = (By.LINK_TEXT, "Shopping cart")

    REMOVE_CHECKBOX = (By.XPATH, "//input[contains(@name,'removefromcart')]")

    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div.order-summary-content")

    def __init__(self, driver):
        super().__init__(driver)

    # Open homepage
    def open_homepage(self):
        self.open_url(self.HOME_ENDPOINT)

    # Add product to cart
    def add_product_to_cart(self):
        self.open_url(self.PRODUCT_ENDPOINT)

        add_cart = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))

        self.driver.execute_script("arguments[0].click();", add_cart)

        self.open_url(self.CART_ENDPOINT)

    # Open shopping cart
    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART)).click()

    # Remove product from cart
    def remove_product(self):
        try:
            remove_checkbox = self.wait.until(
                EC.element_to_be_clickable(self.REMOVE_CHECKBOX)
            )

            self.driver.execute_script("arguments[0].click();", remove_checkbox)

            update_button = self.wait.until(
                EC.element_to_be_clickable(self.UPDATE_CART_BUTTON)
            )

            self.driver.execute_script("arguments[0].click();", update_button)

        except:
            print("Cart already empty")

    # Verify empty cart
    def verify_cart_empty(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)
        )

        return "Your Shopping Cart is empty!" in message.text
