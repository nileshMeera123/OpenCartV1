
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,

            # THIS IS THE KEY
            "profile.password_manager_leak_detection": False,

            "profile.default_content_setting_values.notifications": 2
        }

        options.add_experimental_option("prefs", prefs)

        # Important flags
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-save-password-bubble")

        #Use fresh profile (VERY IMPORTANT)
        options.add_argument("--incognito")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")


def pytest_configure(config):
    if not hasattr(config, "_metadata"):
        config._metadata = {}
    config._metadata['Project'] = 'Selenium Automation'
    config._metadata['Tester'] = 'Nilesh'

    reports_dir = os.path.join(os.path.abspath(os.curdir), 'reports')

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # report_path = os.path.join(reports_dir, f"report_{timestamp}.html")
    report_path = os.path.join(reports_dir, f"report.html")
    # Set html report path dynamically
    if hasattr(config.option, "htmlpath"):
        config.option.htmlpath = report_path
