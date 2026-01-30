from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//i[normalize-space(text())='Logout']"



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_username(self,username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.btn_logout_xpath)))
            return True
        except:
            return False

    def wait_until_logged_out(self):
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH,self.btn_logout_xpath))
        )