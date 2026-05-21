from pytest_bdd import scenarios, given, when, then
from pages.address_page import AddressPage

# Load feature file
scenarios("../features/address_management.feature")


# Login user
@given("user is logged in")
def login_user(browser):
    browser.address_page = AddressPage(browser)

    browser.address_page.open_login_page()
    browser.address_page.login()


# Add new address
@when("user adds new address")
def add_new_address(browser):
    browser.address_page.open_addresses()
    browser.address_page.click_add_new_address()
    browser.address_page.fill_address_form()


# Save address
@when("user saves address")
def save_address(browser):
    browser.address_page.save_address()


# Verify address added
@then("address should be added successfully")
def verify_address(browser):
    assert browser.address_page.verify_address_added()