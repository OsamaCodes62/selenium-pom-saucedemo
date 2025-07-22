from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
    
    def do_click(self, byLocator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((byLocator))
        ).click()

    def do_send_keys(self, byLocator, keys):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((byLocator))
        ).send_keys(keys)
    
    def get_elemwnt_text(self, byLocator):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((byLocator))
        )
        return element.text