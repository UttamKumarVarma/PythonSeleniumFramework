import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")

driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Uttam")
driver.find_element(By.NAME, "email").send_keys("uttamvarma98@gmail.com")

# drop down selection

dropDown= Select(driver.find_element(By.ID, "exampleFormControlSelect1" ))

dropDown.select_by_visible_text("Female")
#dropDown.select_by_index(0)


driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

assert("The Form has been submitted successfully!." in driver.find_element(By.XPATH, "//div[contains(@class,'dismissible')]").text )

time.sleep(3)