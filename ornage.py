# import time
# from selenium import webdriver
# orangehrm = webdriver.Chrome()
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
# class a():
#     def test_orangehrm3(self):
#         orangehrm.implicitly_wait(5)
#         orangehrm.get("https://opensource-demo.orangehrmlive.com")
#         time.sleep(5)
#         orangehrm.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         orangehrm.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
#         orangehrm.find_element(By.XPATH, "//button[@type='submit']").click()
#         orangehrm.find_element(By.XPATH, "//a[normalize-space()='']").click()
#         orangehrm.implicitly_wait(5)
#         orangehrm.find_element(By.XPATH, "//header[@class='oxd-topbar']//li[3]]").click()
#         orangehrm.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("rohit")
#         orangehrm.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("kishorlal")
#         time.sleep(5)