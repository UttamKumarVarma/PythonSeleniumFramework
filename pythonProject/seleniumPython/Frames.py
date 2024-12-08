from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


driver.switch_to.frame("courses-iframe")

assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()

driver.switch_to.default_content()

assert driver.find_element(By.CLASS_NAME, "logoClass").is_displayed()