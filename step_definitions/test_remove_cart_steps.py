from pytest_bdd import scenarios, given, when, then
from pages.remove_cart_page import RemoveCartPage

# Load feature file
scenarios("../features/remove_from_cart.feature")


# Add product into cart
@given("user has product in cart")
def add_product(browser):
    browser.remove_cart_page = RemoveCartPage(browser)

    browser.remove_cart_page.open_homepage()
    browser.remove_cart_page.add_product_to_cart()


# Remove product from cart
@when("user removes product from cart")
def remove_product(browser):
    browser.remove_cart_page.open_cart()
    browser.remove_cart_page.remove_product()


# Verify empty cart
@then("cart should become empty")
def verify_empty_cart(browser):
    assert browser.remove_cart_page.verify_cart_empty()