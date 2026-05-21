from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

# Load feature file
scenarios("../features/login.feature")


# Open login page
@given("user opens login page")
def open_login_page(browser):
    browser.login_page = LoginPage(browser)
    browser.login_page.open()


# Enter login credentials
@when("user enters valid email and password")
def enter_credentials(browser):
    browser.login_page.enter_credentials()


# Click login button
@when("user clicks login button")
def click_login(browser):
    browser.login_page.click_login()


# Verify successful login
@then("user should login successfully")
def verify_login(browser):
    assert browser.login_page.is_logout_visible()