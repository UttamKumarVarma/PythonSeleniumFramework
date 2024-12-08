import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.XPATH, "//input[@placeholder='Type to Select']").send_keys("Ind")

time.sleep(2)

driver.find_element(By.ID, "ui-id-95").click()

time.sleep(10)