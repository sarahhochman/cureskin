from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """

    ##old stuff##
    #driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
    #service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

    ## different browsers ##
    # context.browser = webdriver.Safari(service=service)
    # context.browser = webdriver.Firefox(service=service)
    # context.driver = webdriver.Chrome(service=service)


    ## Headless on Chrome ##
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # context.driver = webdriver.Chrome(options=chrome_options)


    ## Mobil Development ##
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='https://127.0.0.1//192.168.254.9:4444/wd/hub',
    #                          desired_capabilities=chrome_options.to_capabilities())
    # context.driver.wait = WebDriverWait(context.driver, 10)


    ## BrowserStack ##
    desired_cap = {
         'browser': 'chrome',
         'browser_version': '89',
         'os': 'Windows',
         'os_version': '10',
         'name': 'test_name'
    }
    url = f'https://{"sarahhochman_kwFig3"}:{"QHFRY5ifrkEXPN2VfUcz"}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)


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
