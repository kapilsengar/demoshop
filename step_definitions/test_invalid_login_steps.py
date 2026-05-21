from pytest_bdd import scenarios, given, when, then
from pages.invalid_login_page import InvalidLoginPage

# Load feature file
scenarios("../features/invalid_login.feature")


# Open login page
@given("user opens login page for invalid login")
def open_login(browser):
    browser.invalid_login_page = InvalidLoginPage(browser)
    browser.invalid_login_page.open_login_page()


# Enter invalid credentials
@when("user enters invalid email and password")
def invalid_credentials(browser):
    browser.invalid_login_page.enter_invalid_credentials()


# Click login button
@when("user clicks login button for invalid login")
def click_login(browser):
    browser.invalid_login_page.click_login()


# Verify error message
@then("error message should be displayed")
def verify_error(browser):
    assert browser.invalid_login_page.verify_error_message()