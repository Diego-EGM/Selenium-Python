import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)

# radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
#
# for radio in radios:
#     if radio.get_attribute("value") == "radio2":
#         radio.click()
#         assert radio.is_selected()
#         break

radiobuttons= driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# With this dynamic way we asure we are picking option 2 even if there are more options added later.
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() # Sees if checkbox has been selected and returns true or false
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()



time.sleep(1)