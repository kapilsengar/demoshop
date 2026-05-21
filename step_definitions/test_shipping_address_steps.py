from pytest_bdd import scenarios, given, when, then
from pages.shipping_address_page import ShippingAddressPage

# Load feature file
scenarios("../features/shipping_address.feature")


# Open checkout page
@given("user is on checkout page")
def checkout_page(browser):
    browser.shipping_page = ShippingAddressPage(browser)

    browser.shipping_page.open_login_page()
    browser.shipping_page.login()
    browser.shipping_page.add_product()
    browser.shipping_page.proceed_checkout()


# Enter shipping address
@when("user enters shipping address")
def enter_shipping(browser):
    browser.shipping_page.fill_billing_address()
    browser.shipping_page.continue_billing()


# Verify shipping address
@then("shipping address should be saved")
def verify_shipping(browser):
    assert (
        browser.shipping_page
        .verify_shipping_address()
    )