from pytest_bdd import scenarios, given, when, then
from pages.product_sorting_page import ProductSortingPage

# Load feature file
scenarios("../features/product_sorting.feature")


# Open category page
@given("user is on category page")
def open_category(browser):
    browser.sorting_page = ProductSortingPage(browser)
    browser.sorting_page.open_category_page()


# Sort products
@when("user sorts products by price low to high")
def sort_products(browser):
    browser.sorting_page.sort_products()


# Verify sorting
@then("products should be sorted successfully")
def verify_sorting(browser):
    assert browser.sorting_page.verify_sorting()