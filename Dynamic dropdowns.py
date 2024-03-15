import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") #this variable holds all the matching variables with driver.find_elements
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text) #This wouldntt work sisnce autosuggest value is empty when we first get into the website
assert (driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "India"

time.sleep(1)