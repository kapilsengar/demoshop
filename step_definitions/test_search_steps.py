from pytest_bdd import scenarios, given, when, then
from pages.search_page import SearchPage

# Load feature file
scenarios("../features/search_product.feature")


# Open homepage
@given("user is on homepage")
def open_homepage(browser):
    browser.search_page = SearchPage(browser)
    browser.search_page.open_homepage()


# Search product
@when("user searches for product")
def search_product(browser):
    browser.search_page.search_product(
        "Build your own cheap computer"
    )


# Verify searched product
@then("searched product should be displayed")
def verify_product(browser):
    assert browser.search_page.is_product_displayed()