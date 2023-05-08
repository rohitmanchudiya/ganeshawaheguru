import time
from selenium import webdriver
orangehrm = webdriver.Chrome()
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_d():
#     def test_d1(self):
#         a = 1
#         b = 2
#         c = a + b
#         if c == 3:
#             assert True
#         else:
#             assert False
#     #
#     def test_orangehrm2(self):
#         orangehrm.implicitly_wait(5)
#         orangehrm.get("https://opensource-demo.orangehrmlive.com")
#         orangehrm.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
#         orangehrm.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
#         orangehrm.find_element(By.XPATH,"//button[@type='submit']").click()
#         try:
#             dashboard =orangehrm.find_element(By.XPATH,"//div[@class='oxd-topbar-header']").text
#             if dashboard == True:
#                 print("u are on the dashboard")
#                 orangehrm.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
#                 orangehrm.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
#                 assert True
#         except NoSuchElementException:
#                 assert False
#           # print("ur not on the dashboard")



    def test_orangehrm3(self):
      orangehrm.implicitly_wait(5)
      time.sleep(5)
      orangehrm.get("https://opensource-demo.orangehrmlive")
      orangehrm.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
      orangehrm.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
      orangehrm.find_element(By.XPATH, "//button[@type='submit']").click()
      orangehrm.find_element(By.XPATH,"//a[normalize-space()='']").click()
      orangehrm.implicitly_wait(5)
      orangehrm.find_element(By.XPATH,"//header[@class='oxd-topbar']//li[3]]").click()
      orangehrm.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("rohit")
      orangehrm.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("kishorlal")
      time.sleep(5)

      orangehrm.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("manchudiya")
      orangehrm.find_element(By.XPATH,"//button[@type='submit']").click()
      orangehrm.find_element(By.XPATH,"//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']").click()
      employee_name =orangehrm.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 --strong']").text
      if employee_name == "rohit manchudiya":
          print(employee_name)
          assert True
      else:
          print(employee_name)
          assert False



