import os.path
from configparser import ConfigParser
from fillpdf import fillpdfs
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Get form fields
form_fields = fillpdfs.get_form_fields("OutOfStateDocument.pdf")
print("Form Fields:", form_fields)

# Read data from properties file
config = ConfigParser()
config.read("config.properties")

# Input values
customerName = config.get("PDF_FIELDS", "customerName")



# Create data dictionary with correct field names
# Create data dictionary with updated fields
data_dict = {
    "year": config.get("PDF_FIELDS", "year"),
    "make": config.get("PDF_FIELDS", "make"),
    "bodyType": config.get("PDF_FIELDS", "bodyType"),
    "carModel": config.get("PDF_FIELDS", "carModel"),
    "color": config.get("PDF_FIELDS", "color"),
    "carTitleNumber": config.get("PDF_FIELDS", "carTitleNumber"),
    "vinNumber": config.get("PDF_FIELDS", "vinNumber"),
    "customerName": config.get("PDF_FIELDS", "customerName"),
    "text_76muim": config.get("PDF_FIELDS", "customerLicenseState"),
    "text_77radq": config.get("PDF_FIELDS", "customerLicenseNumber"),
    "text_78grxd": config.get("PDF_FIELDS", "address"),
    "text_79cbso": config.get("PDF_FIELDS", "cityName"),
    "text_80kwsw": config.get("PDF_FIELDS", "state"),
    "text_81omfl": config.get("PDF_FIELDS", "zipCode"),
    "text_84aliz": config.get("PDF_FIELDS", "purchaseDate"),
    "text_83jfdl": config.get("PDF_FIELDS", "salesPersonName"),
    "text_82xkfb": config.get("PDF_FIELDS", "netPrice"),
    "text_85nzgq": config.get("PDF_FIELDS", "purchaseDate"),
    "text_86ntzu": config.get("PDF_FIELDS", "purchaseDate"),
    "text_87xoxv": config.get("PDF_FIELDS", "mileage"),
    "text_88vikh": config.get("PDF_FIELDS", "netPrice"),
    "text_89bxir": config.get("PDF_FIELDS", "netPrice"),
    "text_90dayq": config.get("PDF_FIELDS", "customerName"),
    "text_91vceh": config.get("PDF_FIELDS", "purchaseDate"),
    "text_92wwcr": config.get("PDF_FIELDS", "purchaseDate"),
    "text_60isms": config.get("PDF_FIELDS", "make"),
    "text_61jlmt": config.get("PDF_FIELDS", "carModel"),
    "text_62ezr": config.get("PDF_FIELDS", "year"),
    "text_63ahwi": config.get("PDF_FIELDS", "vinNumber"),
    "text_64cedr": config.get("PDF_FIELDS", "customerName"),
    "text_65laoy": config.get("PDF_FIELDS", "customerName"),
    "text_66cbfa": config.get("PDF_FIELDS", "address"),
    "text_67hd": config.get("PDF_FIELDS", "cityName"),
    "text_68nbpp": config.get("PDF_FIELDS", "state"),
    "text_69enbb": config.get("PDF_FIELDS", "zipCode"),
    "text_79rfnv": config.get("PDF_FIELDS", "purchaseDate"),
    "text_80mhhm": config.get("PDF_FIELDS", "salesPersonName"),
    "text_72teov": config.get("PDF_FIELDS", "year"),
    "text_73hvyz": config.get("PDF_FIELDS", "make"),
    "text_74nsac": config.get("PDF_FIELDS", "carModel"),
    "text_75gxzx": config.get("PDF_FIELDS", "bodyStyle"),
    "text_76ivdp": config.get("PDF_FIELDS", "vinNumber"),
    "text_77mth": config.get("PDF_FIELDS", "mileage"),
    "text_78pjho": config.get("PDF_FIELDS", "color"),
    "text_70vsdr": config.get("PDF_FIELDS", "netPrice"),
    "text_71tqll": config.get("PDF_FIELDS", "netPrice"),
    "text_81noyp": config.get("PDF_FIELDS", "customerName"),
    "text_84tdsv": config.get("PDF_FIELDS", "year"),
    "text_85msg": config.get("PDF_FIELDS", "make"),
    "text_83gocv": config.get("PDF_FIELDS", "carModel"),
    "text_82dubn": config.get("PDF_FIELDS", "vinNumber"),
    "text_86jfyu": config.get("PDF_FIELDS", "customerName"),
    "text_87chyp": config.get("PDF_FIELDS", "purchaseDate"),
}

# Define the output directory and file
output_dir = "filledDocs"
output_file = f"{customerName}_OutOfStateDocument.pdf"
output_path = os.path.join(output_dir, output_file)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Fill the PDF form and save it
fillpdfs.write_fillable_pdf("OutOfStateDocument.pdf", output_path, data_dict)

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