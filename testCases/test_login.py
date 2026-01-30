import time

import pytest

from utilities.parse_config import *
from pageObjects.login import Login
from utilities.custom_logger import MyLogger
from utilities.xl_reader import read_xl_data_to_list



class TestLogin:

    @pytest.mark.regression
    def test_login(self,setup):
        logger = MyLogger.getLogger()
        # print(get_username())
        driver = setup
        logger.info("open the url")
        driver.get(get_base_url())
        logger.info("wait for the page to load")
        driver.maximize_window()
        driver.implicitly_wait(5)
        login = Login(driver)
        login.set_username(get_username())
        login.set_password(get_password())
        login.click_login()
        # driver.switch_to.alert.accept()
        assert login.is_login_successful(), "login not successful"

    @pytest.mark.sanity
    def test_login_data_driven(self, setup):
        logger = MyLogger.getLogger()
        driver = setup
        login_data_list = read_xl_data_to_list()
        logger.info(f"++++++++++++>>>>>> {login_data_list}")
        logger.info("open the url")
        driver.get(get_base_url())
        logger.info("wait for the page to load")
        driver.maximize_window()
        login = Login(driver)
        result = []

        for data in login_data_list:
            login.set_username(data[0])
            login.set_password(data[1])
            login.click_login()
            if data[2] == "Valid":
                if login.is_login_successful():
                    result.append("pass")
                    login.click_logout()
                    login.wait_until_logged_out()
                else:
                    result.append("fail")
            elif data[2] == "Invalid":
                if not login.is_login_successful():
                    result.append("pass")
                else:
                    result.append("fail")
        logger.info(f"result =========> {result}")

        assert "fail" not in result, "data driven test failed"





