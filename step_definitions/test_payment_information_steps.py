from pytest_bdd import scenarios, given, when, then
from pages.payment_information_page import (
    PaymentInformationPage
)

# Load feature file
scenarios(
    "../features/payment_information.feature"
)


# Open payment information page
@given("user is on payment information page")
def payment_info_page(browser):
    browser.payment_page = (
        PaymentInformationPage(browser)
    )

    browser.payment_page.open_login_page()
    browser.payment_page.login()

    browser.payment_page.add_product()
    browser.payment_page.proceed_checkout()

    browser.payment_page.fill_billing_address()
    browser.payment_page.continue_billing()

    browser.payment_page.complete_checkout_steps()


# Continue payment information
@when("user continues payment information")
def continue_payment(browser):
    browser.payment_page.continue_payment_information()


# Verify payment information
@then("payment information should be processed")
def verify_payment(browser):
    assert (
        browser.payment_page
        .verify_payment_information()
    )