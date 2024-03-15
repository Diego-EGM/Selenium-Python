import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
name = "Diego"
driver.get("https://rahulshettyacademy.com/AutomationPractice") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert #  switch to alert mode and save it into an object
alertText = alert.text #copy the alert text and save it into a variable
print(alertText)
assert name in alertText
alert.accept() #click on "OK" for alerts pop up
# alert.dismiss() --------- On the other hand this means "click to cancel button for pop up alerts" 