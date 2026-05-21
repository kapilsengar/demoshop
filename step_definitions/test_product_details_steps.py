from pytest_bdd import scenarios, given, then
from pages.product_details_page import ProductDetailsPage

# Load feature file
scenarios("../features/product_details.feature")


# Open product details page
@given("user opens product details page")
def open_product(browser):
    browser.product_page = ProductDetailsPage(browser)
    browser.product_page.open_product_page()


# Verify product details
@then("product details should be displayed correctly")
def verify_product(browser):
    assert (
        browser.product_page
        .verify_product_title()
    )

    assert (
        browser.product_page
        .verify_add_to_cart()
    )