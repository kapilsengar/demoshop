from pytest_bdd import scenarios, given, when, then

from pages.existing_user_registration_page import (
    ExistingUserRegistrationPage
)

# Load feature file
scenarios(
    "../features/existing_user_registration.feature"
)


# Open register page
@given("user is on register page")
def open_register(browser):
    browser.existing_user_page = (
        ExistingUserRegistrationPage(browser)
    )

    browser.existing_user_page.open_register_page()


# Enter existing user details
@when("user enters already registered email")
def enter_existing_user(browser):
    browser.existing_user_page.enter_existing_user_details()


# Click register button
@when("user clicks register button")
def click_register(browser):
    browser.existing_user_page.click_register()


# Verify registration failure
@then("registration should fail")
def verify_registration(browser):
    assert (
        browser.existing_user_page
        .verify_registration_failed()
    )