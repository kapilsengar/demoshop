from pytest_bdd import scenarios, given, when, then
from pages.contact_us_page import ContactUsPage

# Load feature file
scenarios("../features/contact_us.feature")


# Open contact us page
@given("user opens contact us page")
def open_contact(browser):
    browser.contact_page = ContactUsPage(browser)
    browser.contact_page.open_contact_page()


# Submit contact form
@when("user submits contact form")
def submit_form(browser):
    browser.contact_page.submit_contact_form()


# Verify successful submission
@then("contact form should be submitted successfully")
def verify_submission(browser):
    assert browser.contact_page.verify_contact_submission()