from pytest_bdd import scenarios, given, when, then
from pages.register_page import RegisterPage

# Load feature file
scenarios("../features/register.feature")


# Open registration page
@given("user opens registration page")
def open_register(browser):
    browser.register_page = RegisterPage(browser)
    browser.register_page.open_register_page()


# Enter registration details
@when("user enters registration details")
def enter_details(browser):
    browser.register_page.enter_registration_details()


# Click register button
@when("user clicks register button")
def click_register(browser):
    browser.register_page.click_register()


# Verify successful registration
@then("user should register successfully")
def verify_register(browser):
    assert browser.register_page.verify_registration()