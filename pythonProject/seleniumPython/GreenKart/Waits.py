import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service_object = Service("/Users/uttam/PycharmProjects/pythonProject/drivers/chromedriver")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# Set implicit wait
driver.implicitly_wait(5)

# Click on all product-action elements
elements = driver.find_elements(By.XPATH, "//div[@class='product-action']")
for element in elements:
    element.click()
    print(element)

# Proceed to cart and checkout
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='cart-preview active']//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

# Explicit wait to ensure the page loads with the element
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='brand greenLogo']")))

# Verify items in cart
itemsInCartCount = driver.find_elements(By.XPATH, "//img[@class='product-image']")
print("Number of items added:", len(elements))
print("Number of items in cart:", len(itemsInCartCount))
assert len(elements) == len(itemsInCartCount)
print("All items added are present in the cart")

# Close the browser
driver.quit()
