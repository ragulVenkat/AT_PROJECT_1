"""
Automation Testing for TC_Login_01

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# Class for Data (Invalid Credentials and URL)
class Data:
    username = "Admin"  
    password = "InvalidPassword"  
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


# Class for Locators
class Locators:
    username_locator = "username"  
    password_locator = "password" 
    login_button_locator = '//button[@type="submit"]' 
    error_message_locator = '//div[@role="alert"]'  


# Class for the Invalid Login Test Case
class OrangeHRMTestInvalidLogin(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def invalid_login(self):
        try:
            
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)

            # Enter username
            self.driver.find_element(By.NAME, self.username_locator).send_keys(self.username)
            sleep(2)

            # Enter invalid password
            self.driver.find_element(By.NAME, self.password_locator).send_keys(self.password)
            sleep(2)

            # Click the login button
            self.driver.find_element(By.XPATH, self.login_button_locator).click()
            sleep(3)

            
            error_message = self.driver.find_element(By.XPATH, self.error_message_locator).text
            print(f"Login failed as expected. Error message: {error_message}")

        except NoSuchElementException as e:
            print("Element not found: ", e)

        except Exception as error:
            print("ERROR: ", error)

        finally:
            print("Automation ends.")
            self.driver.quit()


# Main execution
if __name__ == "__main__":
    test_invalid = OrangeHRMTestInvalidLogin()
    test_invalid.invalid_login()
