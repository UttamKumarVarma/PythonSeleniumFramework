from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromeOptions= webdriver.ChromeOptions()
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors") # ignores proceed unsafe

service_object = Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")
driver = webdriver.Chrome(service=service_object, options= chromeOptions)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.maximize_window()

driver.execute_script("window.scrollBy(0,300);")
driver.get_screenshot_as_file("screen.png")