from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage


class SearchPage(BasePage):

    def product_results_shown(self, locator, search_word):
        EC.text_to_be_present_in_element(locator, search_word)

    def click_enter_search(self, locator):
        e = self.driver.find_element(*locator)
        e.send_keys(Keys.ENTER)



