from pytest_bdd import scenarios, given, when, then
from pages.logout_page import LogoutPage

# Load feature file
scenarios("../features/logout.feature")


# Login into application
@given("user logs into application")
def login_user(browser):
    browser.logout_page = LogoutPage(browser)

    browser.logout_page.open_login_page()
    browser.logout_page.login()


# Click logout button
@when("user clicks logout button")
def click_logout(browser):
    browser.logout_page.click_logout()


# Verify successful logout
@then("user should logout successfully")
def verify_logout(browser):
    assert browser.logout_page.verify_logout()