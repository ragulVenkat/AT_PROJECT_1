from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Data
class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Step 1: Navigate to the login page
    driver.get(Data.url)

    # Step 2: Log in with valid credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(Data.username)
    driver.find_element(By.NAME, "password").send_keys(Data.password + Keys.RETURN)

    # Wait for the PIM module to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "PIM"))).click()

    # Step 3: Edit an employee's information
    # Wait for the employee list to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Find and click the first employee in the list (customize the locator as needed)
    employee_row = driver.find_element(By.XPATH, "//table/tbody/tr[1]")
    employee_row.click()

    # Edit the employee's details (modify the locators based on the application)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).clear()
    driver.find_element(By.NAME, "firstName").send_keys("UpdatedFirstName")

    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("UpdatedLastName")

    # Save the changes
    driver.find_element(By.XPATH, "//button[text()='Save']").click()

    # Verify the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'success-message')]")
    )).text

    assert "successfully" in success_message.lower(), "Employee details update failed."

    print("Test Passed: Employee details updated successfully.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
