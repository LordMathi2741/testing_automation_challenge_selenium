from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller

try:
    chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.expandtesting.com/inputs")
    driver.find_element(By.ID, "input-number").send_keys("12345")
    driver.find_element(By.ID,"btn-display-inputs").click()
    output = driver.find_element(By.ID,"output-number").text
    assert output == "12345", "Input value does not match output value."
    print("✅ Input test successful.")
except Exception as e:
    print("❌ An error occurred during the test: {e}")
    