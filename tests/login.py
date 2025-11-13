from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


try:
    chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    button = driver.find_element(By.ID, "submit-login")
    button.click()
    assert "secure" in driver.current_url, "Login was not successful."
    print("✅ Login test successful.")
except Exception as e:
        print(f"❌ An error occurred during the test: {e}")