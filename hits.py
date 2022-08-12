from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import time
import sys

id_username = input("Masukkan username: ")
id_password = input("Masukkan password: ")
kelas = int(input("Masukkan jumlah kelas: "))
repetisi = float(input("Masukkan jumlah hits yang diinginkan tiap kelas: "))

url = "https://elearning.ut.ac.id/login/index.php"
repetisi1 = int(round(repetisi / 2))

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-gpu")
opts.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/83.0.4103.61 Safari/537.36")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)
driver.get(f"{url}")

print("*** Attempt to login")
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.ID, "username")))

user = driver.find_element(By.ID, 'username')
user.send_keys(id_username)
password = driver.find_element(By.ID, 'password')
password.send_keys(id_password)
driver.find_element(By.ID, 'loginbtn').click()
print("*** Login Succesfully")
print("============================")

for i in range(kelas):
    try:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "aalink")))
    except TimeoutException:
        for j in range(3):
            print(f"*** Attempt to refresh ({j})")
            driver.refresh()
            try:
                WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "aalink")))
                break
            except:
                continue
        pass
    time.sleep(5)
    courses = driver.find_elements(By.CLASS_NAME, 'aalink')
    print(courses[i].text.strip())
    courses[i].click()
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "nav-item")))
    for x in range(repetisi1):
        try:
            nav_items = driver.find_elements(By.CLASS_NAME, 'nav-item')
            nav_items[1].click()
        except ElementNotInteractableException:
            pass

        try:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "nav-item")))
        except TimeoutException:
            for attempt in range(3):
                print("*** Attempt to refresh")
                driver.refresh()
                if WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "item-dashboard"))):
                    break
            pass

        try:
            nav_items = driver.find_elements(By.CLASS_NAME, 'nav-item')
            nav_items[0].click()
        except ElementNotInteractableException:
            pass

        try:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "item-dashboard")))
        except TimeoutException:
            for attempt in range(3):
                print("*** Attempt to refresh")
                driver.refresh()
                if WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "item-dashboard"))):
                    break
            pass

        sys.stdout.write(f"\rNumber of Hits : {(x + 1) * 2}")
        sys.stdout.flush()

    print("\nDone!")
    driver.find_element(By.CLASS_NAME, 'item-dashboard').click()
    print("============================")
print("Press ctrl + c or close button to close the console!")
