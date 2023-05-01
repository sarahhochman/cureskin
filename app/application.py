from Pages.base_page import BasePage
from Pages.search_page import SearchPage
from Pages.signup_page import SignUpPage
from selenium.webdriver.common.by import By


class Application:

    def __init__(self, driver):
        self.driver = driver
        #self.main_page = MainPage(self.driver)
        #self.header = Header(self.driver)
        #self.search_results_page = SearchResultsPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.signup_page = SignUpPage(self.driver)