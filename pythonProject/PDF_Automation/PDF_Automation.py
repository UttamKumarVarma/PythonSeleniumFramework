import os.path
from configparser import ConfigParser
from fillpdf import fillpdfs
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

# Get form fields
form_fields = fillpdfs.get_form_fields("MISSOURI_APPLICATION.pdf")
print("Form Fields:", form_fields)

# Read data from properties file
config = ConfigParser()
config.read("config.properties")

# Input values
customerName = config.get("PDF_FIELDS", "customerName")



# Create data dictionary with correct field names
# Create data dictionary with updated fields
data_dict = {
    "customerName": config.get("PDF_FIELDS", "customerName"),  # Already present
    "customerName_RLHT": config.get("PDF_FIELDS", "customerName"),
    "nameBS": config.get("PDF_FIELDS", "customerName"),
    "address": config.get("PDF_FIELDS", "address"),  # Already present
    "cityName": config.get("PDF_FIELDS", "cityName"),  # Already present
    "state": config.get("PDF_FIELDS", "state"),  # Already present
    "nosState": config.get("PDF_FIELDS", "state"),
    "nosState2": config.get("PDF_FIELDS", "state"),
    "zipCode": config.get("PDF_FIELDS", "zipCode"),  # Already present
    "vinNumber": config.get("PDF_FIELDS", "vinNumber"),  # Already present
    "vinNumber_0KAW": config.get("PDF_FIELDS", "vinNumber"),
    "year": config.get("PDF_FIELDS", "year"),  # Already present
    "year_XRUP": config.get("PDF_FIELDS", "year"),
    "yearPS": config.get("PDF_FIELDS", "year"),
    "make": config.get("PDF_FIELDS", "make"),  # Already present
    "makeBS": config.get("PDF_FIELDS", "make"),
    "make_DPY1": config.get("PDF_FIELDS", "make"),
    "carTitleNumber": config.get("PDF_FIELDS", "carTitleNumber"),  # Already present
    "nosTitle": config.get("PDF_FIELDS", "carTitleNumber"),
    "titleState": config.get("PDF_FIELDS", "titleState"),  # Already present
    "bodyStyle": config.get("PDF_FIELDS", "bodyStyle"),  # Already present
    "missouriTitleStyle": config.get("PDF_FIELDS", "bodyStyle"),
    "color": config.get("PDF_FIELDS", "color"),  # Already present
    "color_0BQI": config.get("PDF_FIELDS", "color"),  # Already present
    "Fuel": config.get("PDF_FIELDS", "Fuel"),  # Already present
    "Fuel_MPKG": config.get("PDF_FIELDS", "Fuel"),
    "mileage": config.get("PDF_FIELDS", "mileage"),  # Already present
    "missouriTitleMileage": config.get("PDF_FIELDS", "mileage"),
    "purchaseDate": config.get("PDF_FIELDS", "purchaseDate"),  # Already present
    "customerLicenseNumber": config.get("PDF_FIELDS", "customerLicenseNumber"),  # Already present
    "nosDLN": config.get("PDF_FIELDS", "customerLicenseNumber"),
    "customerBirthDate": config.get("PDF_FIELDS", "customerBirthDate"),  # Already present
    "nosCustomerDOB": config.get("PDF_FIELDS", "customerBirthDate"),
    "netPrice": config.get("PDF_FIELDS", "netPrice"),  # Already present
    "carModel": config.get("PDF_FIELDS", "carModel"),  # New field added
    "text_197uxse": config.get("PDF_FIELDS", "year"),  # New field added
}


# Define the output directory and file
output_dir = "filledDocs"
output_file = f"{customerName}_MISSOURI_APPLICATION.pdf"
output_path = os.path.join(output_dir, output_file)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Fill the PDF form and save it
fillpdfs.write_fillable_pdf("MISSOURI_APPLICATION.pdf", output_path, data_dict)

#fillpdfs.flatten_pdf(output_path, output_path)


#print(f"PDF filled and saved to {output_path}")
# Open the generated PDF
try:
    subprocess.run(["open", output_path], check=True)  # For macOS
    print(f"Opened PDF: {output_path}")
except Exception as e:
    print(f"Failed to open PDF: {e}")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://sa.dor.mo.gov/mv/trpa_dealers/logon.aspx")

driver.maximize_window()

driver.find_element(By.ID, "ContentPlaceHolder1_Login1_UserName").send_keys(config.get("PDF_FIELDS", "tempUsername"))
driver.find_element(By.ID, "ContentPlaceHolder1_Login1_Password").send_keys(config.get("PDF_FIELDS", "tempPassword"))
driver.find_element(By.ID, "ContentPlaceHolder1_Login1_LoginButton").click()

dropDown= Select(driver.find_element(By.ID, "ContentPlaceHolder1_TypeDropDown0" ))

dropDown.select_by_visible_text(config.get("PDF_FIELDS", "type"))

driver.find_element(By.ID, "ContentPlaceHolder1_DLNTextBoxestextBox0").send_keys(config.get("PDF_FIELDS", "customerLicenseNumber"))
driver.find_element(By.ID, "ContentPlaceHolder1_LastNametextBox0").send_keys(config.get("PDF_FIELDS", "customerLastName"))
driver.find_element(By.ID, "ContentPlaceHolder1_FirstNametextBox0").send_keys(config.get("PDF_FIELDS", "customerFirstName"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtAddress").send_keys(config.get("PDF_FIELDS", "address"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").send_keys(config.get("PDF_FIELDS", "cityName"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtState").send_keys(config.get("PDF_FIELDS", "state"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtZip").send_keys(config.get("PDF_FIELDS", "zipCode"))
Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlKOV" )).select_by_visible_text(config.get("PDF_FIELDS", "kindOfVehicle"))
Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlNCICMake" )).select_by_visible_text("Make")
driver.find_element(By.ID, "ContentPlaceHolder1_txtYear").send_keys(config.get("PDF_FIELDS", "year"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtVIN").send_keys(config.get("PDF_FIELDS", "vinNumber"))
driver.find_element(By.ID, "ContentPlaceHolder1_txtPurchase").send_keys(config.get("PDF_FIELDS", "purchaseDate"))
Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlDealer" )).select_by_visible_text("D7297")
Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlOwnership" )).select_by_visible_text(config.get("PDF_FIELDS", "stateTitle"))
driver.find_element(By.ID, "ContentPlaceHolder1_rblFinancial_0").click()
driver.find_element(By.ID, "ContentPlaceHolder1_rblInspection_0").click()