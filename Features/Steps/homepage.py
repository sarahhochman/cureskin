from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH = (By.CSS_SELECTOR, 'svg[class="icon icon-search modal__toggle-open"]')
SEARCH_INPUT = (By.ID, 'Search-In-Modal')
CURRENT_URL = (By.XPATH, "//ul[@id='product-grid']//li//a/span")

@given ('Open Cureskin home page')
def open_cureskin(context):
    context.app.base_page.open_url('https://shop.cureskin.com/')


@when('Click on search')
def click_search(context):
    context.app.base_page.find_element(SEARCH).click()


@when('Input {search_word} into search field')
def input_search_word(context, search_word):
    context.app.base_page.input_text(search_word, *SEARCH_INPUT)


@when('Click Enter')
def click_enter(context):
    context.app.base_page.click_enter(SEARCH_INPUT)


@then('Product results for {search_word} are shown')
def product_results_shown(context, search_word):
    context.app.search_page.product_results_shown(CURRENT_URL, search_word)
