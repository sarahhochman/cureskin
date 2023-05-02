from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    context.driver = webdriver.Chrome(service=service)

    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #context.driver = webdriver.Firefox(service=service)
    #context.driver = webdriver.Chrome(options=chrome_options)
    context.browser = webdriver.Safari(service=service)
    context.browser = webdriver.Firefox(service=service)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)
    setx BROWSERSTACK_USERNAME "sarahhochman_kwFig3"
    setx BROWSERSTACK_ACCESS_KEY "QHFRY5ifrkEXPN2VfUcz"
    set BROWSERSTACK_USERNAME = sarahhochman_kwFig3
    set BROWSERSTACK_ACCESS_KEY = QHFRY5ifrkEXPN2VfUcz

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
