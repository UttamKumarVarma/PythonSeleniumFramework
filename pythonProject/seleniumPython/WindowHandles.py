import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service_object = Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


driver.find_element(By.ID,"opentab").click()

windowsNames = driver.window_handles

driver.switch_to.window(windowsNames[1])


assert driver.find_element(By.XPATH,"//span[text()='info@qaclickacademy.com']").is_displayed(), "Mail ID is not present"

driver.close()

driver.switch_to.window(windowsNames[0])

time.sleep(4)