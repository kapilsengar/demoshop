from pytest_bdd import scenarios, given, when, then
from pages.shipping_method_page import ShippingMethodPage

# Load feature file
scenarios("../features/shipping_method.feature")


# Open shipping method page
@given("user is on shipping method page")
def shipping_page(browser):
    browser.shipping_method_page = (
        ShippingMethodPage(browser)
    )

    browser.shipping_method_page.open_login_page()
    browser.shipping_method_page.login()
    browser.shipping_method_page.add_product()
    browser.shipping_method_page.proceed_checkout()

    browser.shipping_method_page.fill_billing_address()
    browser.shipping_method_page.continue_billing()


# Select shipping method
@when("user selects shipping method")
def select_shipping(browser):
    browser.shipping_method_page.complete_checkout_steps()


# Verify shipping method
@then("shipping method should be selected")
def verify_shipping(browser):
    assert (
        browser.shipping_method_page
        .verify_shipping_method()
    )