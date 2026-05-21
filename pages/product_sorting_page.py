from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductSortingPage(BasePage):
    # Category page endpoint
    CATEGORY_ENDPOINT = "/apparel-shoes"

    # Web elements
    SORT_DROPDOWN = (By.ID, "products-orderby")

    PRODUCT_PRICES = (By.CSS_SELECTOR, "span.price.actual-price")

    def __init__(self, driver):
        super().__init__(driver)

    # Open category page
    def open_category_page(self):
        self.open_url(self.CATEGORY_ENDPOINT)

    # Sort products by price
    def sort_products(self):
        dropdown = Select(
            self.wait.until(EC.presence_of_element_located(self.SORT_DROPDOWN))
        )

        dropdown.select_by_visible_text("Price: Low to High")

    # Verify product sorting
    def verify_sorting(self):
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_PRICES))

        prices = self.driver.find_elements(*self.PRODUCT_PRICES)

        price_list = []

        for price in prices:
            value = price.text.replace("$", "")

            price_list.append(float(value))

        return price_list == sorted(price_list)
