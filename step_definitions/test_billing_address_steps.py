from pytest_bdd import scenarios, given, when, then
from pages.billing_address_page import BillingAddressPage

# Load feature file
scenarios("../features/billing_address.feature")


# Proceed to checkout
@given("user proceeds to checkout")
def proceed_checkout(browser):
    browser.billing_page = BillingAddressPage(browser)

    browser.billing_page.open_login_page()
    browser.billing_page.login()
    browser.billing_page.add_product_to_cart()
    browser.billing_page.proceed_to_checkout()


# Enter billing address
@when("user enters billing address")
def enter_address(browser):
    browser.billing_page.enter_billing_address()
    browser.billing_page.save_billing_address()


# Verify billing address
@then("billing address should be saved")
def verify_billing(browser):
    assert (
        browser.billing_page
        .verify_billing_address_saved()
    )