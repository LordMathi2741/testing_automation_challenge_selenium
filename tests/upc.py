from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from dotenv import load_dotenv
import os

try:
    load_dotenv()

    email = os.getenv("UPC_EMAIL")
    password = os.getenv("UPC_PASSWORD")

    chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    driver.get("https://aulavirtual.upc.edu.pe/webapps/login/")
    
    assert "Blackboard" in driver.title, "This page is not the UPC login page."

    wait.until(EC.element_to_be_clickable((By.ID, "btn-login"))).click()

    input_email = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
    input_email.send_keys(email)
    
    print("Email submitted")

    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

    input_password = wait.until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )

    input_password.send_keys(password)
    print("Password submitted")
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
    print("Waiting for login to complete...")
    wait.until(EC.url_contains("aulavirtual.upc.edu.pe/ultra/institution-page"))
    assert "aulavirtual.upc.edu.pe/ultra/institution-page" in driver.current_url, "Login was not successful."

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    driver.quit()
