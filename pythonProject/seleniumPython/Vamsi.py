import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# Open the website
driver.get("https://rockyweb.usgs.gov/vdelivery/Datasets/Staged/Elevation/LPC/Projects/legacy/MO_STLOUIS_2012/LAZ/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(text(),'Size')]").click()

try:
    # Wait until elements are visible on the page
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'USGS_LPC_MO_Saint_Louis_')]"))
    )

    # Click the link
    link.click()
    time.sleep(2)  # Allow time for the PDF to load in the new tab

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    # Add any actions to interact with the PDF or verify its presence if needed
    # (PDF content might not be directly accessible in Selenium, but you can confirm the URL)

    # For example, print the current URL of the PDF
    print("PDF URL:", driver.current_url)

    # Close the PDF tab and switch back to the original window
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

finally:
    driver.quit()

