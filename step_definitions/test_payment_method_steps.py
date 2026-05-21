from pytest_bdd import scenarios, given, when, then
from pages.payment_method_page import (
    PaymentMethodPage
)

# Load feature file
scenarios("../features/payment_method.feature")


# Open payment page
@given("user is on payment page")
def payment_page(browser):
    browser.payment_method_page = (
        PaymentMethodPage(browser)
    )

    browser.payment_method_page.open_login_page()
    browser.payment_method_page.login()

    browser.payment_method_page.add_product()
    browser.payment_method_page.proceed_checkout()

    browser.payment_method_page.fill_billing_address()
    browser.payment_method_page.continue_billing()

    browser.payment_method_page.complete_checkout_steps()


# Select payment method
@when("user selects payment method")
def select_payment(browser):
    browser.payment_method_page.complete_checkout_steps()


# Verify payment method
@then("payment method should be selected")
def verify_payment(browser):
    assert (
        browser.payment_method_page
        .verify_payment_method()
    )