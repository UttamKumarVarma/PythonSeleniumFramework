import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")

driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

element= driver.find_element(By.XPATH, "//input[@value='option2']")

element.click()
assert element.is_selected()
#assert not element.is_selected()