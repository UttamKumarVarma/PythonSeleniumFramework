import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chromedriver_path = os.path.expanduser("~/drivers/chromedriver")

service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")

driver = webdriver.Chrome(service=service_object)


# for firefox
# service_object=Service("/Users/uttam/PycharmProjects/pythonProject/drivers/geckodriver")
#
# driver = webdriver.Firefox(service=service_object)


# Initialize the Chrome WebDriver
#driver = webdriver.Chrome()
driver.get("https://uttamkumarvarma.github.io/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(3)

