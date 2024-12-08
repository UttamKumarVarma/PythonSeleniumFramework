import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")

driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()
#alert.dismiss()

time.sleep(3)