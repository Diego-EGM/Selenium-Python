import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)
#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0) #Index 0 for first option
dropdown.select_by_value("value here")






# Locate the dropdown element by its ID, name, XPath, CSS selector, etc.
# dropdown_element = driver.find_element(By.ID,"exampleFormControlSelect1") # Replace "dropdown_id" with the actual ID of the dropdown
#
# # Use the Select class to interact with the dropdown
# dropdown = Select(dropdown_element)
#
# # Method 1: Select by visible text
# dropdown.select_by_visible_text("Female")


# driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# # driver.find_element(By.ID,"exampleInputPassword1").send_keys("Lucian")
# driver.find_element(By.ID,"exampleCheck1").click()
#
# # CSS - tagname[attribute = 'value']
#
# driver.find_element(By.XPATH, "(//input[@type = 'text'])[1]").send_keys("Diego Garcia")
# # driver.find_element(By.CLASS_NAME, "ng-pristine ng-valid ng-touched").send_keys("Diego Garcia")
# # driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Diego Garcia")
# driver.find_element(By.ID,"inlineRadio1").click()
#
# # Xpath --> //tagname[@attribute = "value"] -> //input[@type='submit']
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# message = driver.find_element(By.CLASS_NAME, "alert-success").text #.text -->  copies the text
# print(message)

# assert "Success" in message #assert is a keyword used to test if a condition is true

# driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Hello Again")
# driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()




















time.sleep(10)