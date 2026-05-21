from pytest_bdd import scenarios, given, when, then
from pages.order_confirmation_page import (
    OrderConfirmationPage
)

# Load feature file
scenarios(
    "../features/order_confirmation.feature"
)


# Complete checkout process
@given("user completes checkout process")
def checkout_process(browser):
    browser.order_page = (
        OrderConfirmationPage(browser)
    )

    browser.order_page.open_login_page()
    browser.order_page.login()

    browser.order_page.add_product()
    browser.order_page.proceed_checkout()

    browser.order_page.fill_billing_address()
    browser.order_page.continue_billing()

    browser.order_page.complete_checkout_steps()


# Confirm order
@when("user confirms the order")
def confirm_order(browser):
    browser.order_page.confirm_order()


# Verify order success
@then("order should be placed successfully")
def verify_order(browser):
    assert (
        browser.order_page
        .verify_order_success()
    )