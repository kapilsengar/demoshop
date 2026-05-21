from pytest_bdd import scenarios, given, when, then
from pages.cart_page import CartPage

# Load feature file
scenarios("../features/add_to_cart.feature")


# Open homepage
@given("user opens homepage")
def open_homepage(browser):
    browser.cart_page = CartPage(browser)
    browser.cart_page.open_homepage()


# Add product to cart
@when("user adds product to cart")
def add_product(browser):
    browser.cart_page.add_product_to_cart()


# Verify added product
@then("product should be added successfully")
def verify_cart(browser):
    assert browser.cart_page.verify_success_message()
