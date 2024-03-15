import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)
driver.find_element(By.LINK_TEXT, "Forgot password?").click() #Link_Text can only be used with anchors

#Locators using parent to child  by Xpath
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#Locators using parent to child  by CSS SLECTOR
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input ").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
















time.sleep(10)