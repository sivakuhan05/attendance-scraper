from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

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

# Pull up login page and allow the user to login
driver.get("https://ecampus.psgtech.ac.in/studzone")
print("Login to account")
time.sleep(15)

# Pull up the attendance page once the user logs in
driver.get("https://ecampus.psgtech.ac.in/studzone/Attendance/StudentPercentage")
print("Navigated to attendance page")
time.sleep(5)

# Changing the dropdown menu to show 20 entries
select = Select(driver.find_element("name", "example_length"))
select.select_by_value("20")
print("Changed number of visible entires in page to 20")
time.sleep(10)

# Extract data from table
rows = driver.find_elements("css selector", "#example tbody tr")
print(f"Found {len(rows)} rows")

#printing data from all rows
for row in rows:
    cols = row.find_elements("tag name", "td")
    data = [i.text for i in cols]
    print(data)
