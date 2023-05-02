from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://shop.cureskin.com/'

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text
        f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Checking by locator {locator}. Expected text {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def verify_item_displayed(self,  expected_result, locator):
        assert self.driver.find_element(*locator).is_displayed(), f'{expected_result} does not appear'

    def verify_items_displayed(self, expected_result, locator):
        assert self.driver.find_elements(*locator).is_displayed(), f'{expected_result} does not appear'


