# 🧪 Selenium Automation Framework using Page Object Model (POM)

A clean and scalable test automation framework built with **Python**, **Selenium**, and the **Page Object Model (POM)** pattern.

This project automates login functionality for [SauceDemo](https://www.saucedemo.com/v1/) using industry-standard practices to help QA teams ensure application quality through maintainable code and structured testing.

---

## 📂 Project Structure

├── base_file.py # BasePage class: reusable Selenium actions
├── DataModel.py # Test data and constants
├── login_page.py # Login Page Object Model
├── main_test.py # Executable test case using unittest

yaml
Copy
Edit

---

## 💡 Key Concepts

### ✅ Page Object Model (POM)

**POM** separates test logic from UI structure by creating individual page classes that encapsulate element locators and interactions.

Example from `login_page.py`:

```python
USERNAME = By.ID, "user-name"

def do_login(self, user_name, password):
    self.do_send_keys(self.USERNAME, user_name)
    ...
```
This promotes:

Reusability of code

Better readability

Easy maintenance

🔁 Base Page Abstraction
The BasePage class (in base_file.py) provides:
```
do_click(locator)

do_send_keys(locator, value)
```
These utility functions allow clean interaction with web elements across all page objects.

🚀 Running the Test
🧱 Prerequisites
Python 3.8+

Google Chrome

Update chrome_path in main_test.py to your Chrome binary location

Install dependencies:
```
pip install selenium undetected-chromedriver
```
▶️ Run the Test

python main_test.py
The script will:

Launch Chrome using undetected driver

Navigate to SauceDemo

Attempt login using predefined credentials

🔐 Features
🧩 Page Object Model structure

🔒 Uses undetected_chromedriver to bypass bot detection

🧪 Test execution via Python unittest

📁 Clean separation of test data, logic, and locators

🔍 Sample Test Snippet

def test_case(self):
    login = loginPage(self.driver)
    login.do_login(Test_data.USER_NAME[0], Test_data.PASSWORD)
    self.assertTrue(True)
📈 Why This Project?
This project demonstrates:

Proficiency with Selenium and test automation frameworks

Use of best practices in QA engineering

Clean, maintainable, and scalable test code

Real-world login testing scenario

🙋‍♂️ About Me
I'm a dedicated SQA Engineer who believes in test automation as a driver for efficiency
and quality. I specialize in building test systems that are both reliable and easy to expand as software grows.

📌 Plans for Next Steps
✅ Add test reports (e.g., pytest-html, unittest-xml-reporting)

✅ Include edge/negative login cases

✅ Add test steps for product/cart/inventory pages

✅ Integrate CI tools (GitHub Actions, Jenkins)
```
