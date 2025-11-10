from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ssl, certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
import chromedriver_autoinstaller
chromedriver_autoinstaller.install(no_ssl=True)
driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.find_element(By.XPATH, "//button[contains(., 'Aceptar')]").click()
except:
    pass

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)
print("🔍 Searching for 'Selenium Python'...")
try:
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    print("✅ Search results loaded successfully.")
except:
    print("❌ Search results did not load in time.")
driver.quit()   