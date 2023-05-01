from selenium.webdriver.common.by import By
from behave import given, when, then


EMAIL_FIELD = (By.ID, 'ContactFooter-email')
SIGNUP = (By.CSS_SELECTOR, 'h3[ID="ContactFooter-success"]')


@when('click on email field')
def email_field(context):
    context.app.base_page.find_element(EMAIL_FIELD).click()


@when('input {string}')
def input_string(context, string):
    context.app.base_page.input_text(string, *EMAIL_FIELD)


@when('Click Enter EMAIL')
def click_enter_email(context):
    context.app.signup_page.click_enter_email(EMAIL_FIELD)


@then('Get SignUp Message')
def sign_up_message(context):
    context.app.base_page.verify_text("Thanks for subscribing", *SIGNUP)


@then('Get Error Message')
def get_error_message(context):
    context.app.signup_page.get_error_message()



