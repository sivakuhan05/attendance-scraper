from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# --- Driver initialization ---
options = Options()
options.binary_location = "/snap/bin/brave"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=/tmp/brave-selenium")

driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="145").install()),
        options=options
        )

print("Driver created")
driver.maximize_window()

# --- Open login page and allow the user to login ---
driver.get("https://ecampus.psgtech.ac.in/studzone")
print("Login to account")
time.sleep(15)

# --- Open attendance page once the user logs in ---
driver.get("https://ecampus.psgtech.ac.in/studzone/Attendance/StudentPercentage")
print("Navigated to attendance page")

# --- Change the dropdown menu to show 20 entries ---
select = Select(driver.find_element("name", "example_length"))
select.select_by_value("20")
print("Changed number of visible entries in page to 20")
time.sleep(1)

# --- Extract data from table ---
rows = driver.find_elements("css selector", "#example tbody tr")
print(f"Found {len(rows)} rows")

# --- Summarised tabular data ---
print("\nAttendance Summary\n")

# Header/Title row
header = f"{'Course':<10}{'Total hrs':<13}{'Total Absent':<16}{'Total Present':<17}{'Physical %':<14}{'Medical %':<13}"
print(header)
print('-' * len(header))

# Data
for row in rows:

    # Extract data of each row in the table
    cols = row.find_elements('tag name', 'td')
    data = [i.text for i in cols]

    # Assign variables to the necessary fields from each row
    course = data[0]
    tot_hrs = data[1]
    tot_abs = data[3]
    tot_pres = data[4]
    physical = data[5]
    medical = data[7]

    row_str = f"{course:<10}{tot_hrs:<13}{tot_abs:<16}{tot_pres:<17}{physical:<14}{medical:<13}"
    print(row_str)
