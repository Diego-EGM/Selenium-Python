import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)

























time.sleep(5)