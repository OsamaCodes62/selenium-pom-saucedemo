from selenium.webdriver.chrome.options import Options
from DataModel import Test_data 
import unittest
import undetected_chromedriver as uc
from login_page import loginPage
import time

chrome_path = r"chrome-win64/chrome.exe"

options = Options()
options.binary_location = chrome_path
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = uc.Chrome(options= options)
        self.driver.maximize_window()
        self.driver.get(Test_data.BASE_URL)

    def test_case(self):
        login = loginPage(self.driver)
        login.do_login(Test_data.USER_NAME[0], Test_data.PASSWORD)
        time.sleep(5)
        self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()