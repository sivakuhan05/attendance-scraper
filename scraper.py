from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
time.sleep(10)

# Pull up the attendance page once the user logs in
driver.get("https://ecampus.psgtech.ac.in/studzone/Attendance/StudentPercentage")
time.sleep(20)


