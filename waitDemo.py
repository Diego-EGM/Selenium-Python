import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\OQA\PycharmProjects\PythonTesting\pythonProject1\PythonSelenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/") # .get ---accede a X pagina
driver.maximize_window() #.maximize ---- Amplia a pantalla completa
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"promoBtn").click()
time.sleep(3)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)


























time.sleep(2)