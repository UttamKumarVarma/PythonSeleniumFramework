import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

# Click on all product-action elements
elements = driver.find_elements(By.XPATH, "//div[@class='product-action']")
for element in elements:
    element.click()
    print(element)

# Proceed to cart and checkout
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='cart-preview active']//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

time.sleep(3)

totalValue=0

for textElement in driver.find_elements(By.XPATH,"//tbody//td[5]/p"):
    totalValue += int(textElement.text)

UI_TotalValue= driver.find_element(By.CSS_SELECTOR, ".totAmt").text

assert totalValue == int(UI_TotalValue)+10, "Expected "+UI_TotalValue+ " But Actual value is "+ str(totalValue)