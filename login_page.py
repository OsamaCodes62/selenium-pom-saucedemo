from base_file import BasePage
from selenium.webdriver.common.by import By

class loginPage(BasePage):
    USERNAME = By.ID, "user-name"
    PASSWORD = By.ID , "password"
    LOGIN_BTN = By.ID, "login-button"
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, user_name, password):
        super().do_send_keys(self.USERNAME, user_name)
        super().do_send_keys(self.PASSWORD, password)
        super().do_click(self.LOGIN_BTN)