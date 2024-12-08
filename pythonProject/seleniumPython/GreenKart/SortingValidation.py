

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()


dropDownEle= Select(driver.find_element(By.ID, "page-menu"))
dropDownEle.select_by_visible_text("20")

listValues = driver.find_elements(By.XPATH,"//tr/td[1]")

ListData= []

for value in listValues:
    ListData.append(value.text)

ListData.sort()

driver.find_element(By.XPATH, "//tr/th[1]").click()

sortedListValues = driver.find_elements(By.XPATH,"//tr/td[1]")

UI_List=[]
for sortedListValue in sortedListValues:
    UI_List.append(sortedListValue.text)


assert UI_List== ListData, "Both Lists are not equal"
