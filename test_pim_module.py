from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Test Data
class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"  # Valid ESS user
    password = "admin123"  # Valid password
    employee_first_name = "Venkat"
    employee_last_name = "S"
    employee_id = "722"
    driving_licences = "JNASJK2332"
    others_id = "191913-9311"


# Locators
class Locators:
    username_locator = "username"
    password_locator = "password"
    login_button_locator = '//button[@type="submit"]'
    pim_module_locator = '//a[@href="/web/index.php/pim/viewPimModule"]'
    add_employee = '//li[@class="oxd-topbar-body-nav-tab"]'
    add_button_locator = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
    first_name_locator = '//input[@class="oxd-input oxd-input--active orangehrm-firstname"]'
    mid_name_locator = '//input[@class="oxd-input oxd-input--focus orangehrm-middlename"]'
    last_name_locator = '//input[@class="oxd-input oxd-input--active orangehrm-lastname"]'
    save_button_locator = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    back_for_silde = '//button[@class="oxd-icon-button oxd-main-menu-button"]'
    add_employee_id = '//input[@data-v-1f99f73c and @class="oxd-input oxd-input--active"]'
    other_id = '//input[@class="oxd-input oxd-input--active" and @data-v-1f99f73c]'
    license = '//input[@data-v-1f99f73c and @data-v-4a95a20 and @class="oxd-input oxd-input--active" and @placeholder="yyyy-dd-mm"]'
    license_input_locator = '//div[@class="oxd-grid-3 orangehrm-full-width-grid"]//input[@class="oxd-input oxd-input--active"]'
    license_expire = '//div[@class="oxd-calendar-date --selected --today" and normalize-space(text())="8"]'
    nationality = '//div[@class="oxd-select-text oxd-select-text--focus" and @data-v-67d2aedf]'
    indian = '//span[@data-v-13cf171c and normalize-space(text())="Indian"]'
    gender = '//div[@class="oxd-select-text oxd-select-text--focus" and @data-v-67d2aedf]'
    single = '//span[@data-v-13cf171c  and normalize-space(text())="Single"]'
    date_of_birth = '//div[@class="oxd-date-wrapper"]//input[@class="oxd-input oxd-input--focus" and @placeholder="yyyy/mm/dd"]'
    male = '//span[@data-v-7ef819fd  and @class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"]'
    save_1 = '//button[@data-v-10d463b7 and @data-v-6653c066 and @class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    success_message_locator = '//div[contains(@class, "oxd-toast")]/p'
    blood_group_dropdown = '//div[@class="oxd-select-text oxd-select-text--focus"]'
    blood_group_a_plus = "//span[@data-v-13cf171c and text()='A+']"


# Test Case: Add Employee
def test_add_employee(browser):
    driver = browser
    driver.get(Data.url)
    sleep(5)

    # Step 1: Login to OrangeHRM
    driver.find_element(By.NAME, Locators.username_locator).send_keys(Data.username)
    driver.find_element(By.NAME, Locators.password_locator).send_keys(Data.password)
    driver.find_element(By.XPATH, Locators.login_button_locator).click()
    sleep(5)

    # Step 2: Navigate to the PIM module
    driver.find_element(By.XPATH, Locators.pim_module_locator).click()
    sleep(5)

    # Step 3: Click Add to add a new employee
    driver.find_element(By.XPATH, Locators.add_button_locator).click()
    sleep(5)
    
    # Step 4: Fill in basic employee details
    driver.find_element(By.XPATH, Locators.first_name_locator).send_keys(Data.employee_first_name)
    sleep(2)
    driver.find_element(By.XPATH, Locators.last_name_locator).send_keys(Data.employee_last_name)
    sleep(2)
    driver.find_element(By.XPATH, Locators.back_for_silde).click()
    sleep(2)
    driver.find_element(By.XPATH, Locators.add_employee_id).send_keys(Data.employee_id)
    sleep(2)
    driver.find_element(By.XPATH, Locators.save_button_locator).click()
    sleep(10)

    # Step 5: Fill in additional details (if required)
    driver.find_element(By.XPATH, Locators.back_for_silde).click()
    sleep(2)
    driver.find_element(By.XPATH, Locators.add_employee_id).send_keys(Data.employee_id)
    sleep(2)
    driver.find_element(By.XPATH, Locators.other_id).send_keys(Data.others_id)
    sleep(8)
    # Example: Selecting a nationality

    driver.find_element(By.XPATH, Locators.license_input_locator).send_keys(Data.driving_licences)
    sleep(5)
   
    # Example: Selecting blood group
    driver.find_element(By.XPATH, Locators.license_input_locator).send_keys(Data.driving_licences)
    sleep(5) 

    driver.find_element(By.XPATH, Locators.license).click()
    sleep(2)
    driver.find_element(By.XPATH, Locators.license_expire).click()
    sleep(2)
    
   

    # Step 6: Verify success message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.success_message_locator))
    ).text
    assert "Successfully Saved" in success_message, "Employee addition failed!"

    print("Test Passed: Employee added successfully.")
