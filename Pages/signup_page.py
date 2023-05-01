from selenium.webdriver import support
from selenium.webdriver.common import alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class SignUpPage(BasePage):

    def click_enter_email(self, locator):
        e = self.driver.find_element(*locator)
        e.send_keys(Keys.ENTER)

    def get_error_message(self):
        assert EC.alert_is_present(), 'no error message appeared'

