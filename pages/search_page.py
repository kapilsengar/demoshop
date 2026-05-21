from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):
    # Homepage endpoint
    HOME_ENDPOINT = "/"

    # Web elements
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "input.search-box-button"
    )

    PRODUCT_TITLE = (
        By.XPATH,
        "//h2[@class='product-title']/a"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Open homepage
    def open_homepage(self):
        self.open_url(self.HOME_ENDPOINT)

    # Search product
    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()

    # Verify searched product
    def is_product_displayed(self):
        product = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

        return product.is_displayed()