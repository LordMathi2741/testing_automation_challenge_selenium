from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import time
error_message = "New record was not added successfully."

def insert_test():
    try:
        chromedriver_autoinstaller.install(cwd=True)
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.find_element(By.ID, "addNewRecordButton").click()
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID,"userEmail").send_keys("johnDoe@gmail.com")
        driver.find_element(By.ID, "age").send_keys("30")
        driver.find_element(By.ID, "salary").send_keys("50000")
        driver.find_element(By.ID, "department").send_keys("Engineering")
        driver.find_element(By.ID, "submit").click()
        wait = WebDriverWait(driver, 10)
        rows = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group"))
        target_row = wait.until(
        lambda _ : next(
            (row for row in rows
            if "John" in row.text),
            None
         )
        )
        assert target_row is not None, error_message
        print("✅ New record added successfully.")
        time.sleep(100)
    except WebDriverException as e:
        print(f"❌ An error occurred while trying to install WebDriver: {e}")
    except AssertionError as ae:
        print(f"❌ An error was ocurred while trying to compare a condition: {ae}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        
def search_test(input):
    try:
        chromedriver_autoinstaller.install(cwd=True)
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        search_box = driver.find_element(By.ID, "searchBox")
        search_box.send_keys(input)
        wait = WebDriverWait(driver, 10)
        rows = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group"))
        target_row = wait.until(
        lambda _ : next(
            (row for row in rows
            if input in row.text),
            None
         )
        )
        assert target_row is not None, error_message
        print("✅ Search record found successfully.")
    except WebDriverException as e:
        print(f"❌ An error occurred while trying to install WebDriver: {e}")
    except AssertionError as ae:
        print(f"❌ An error was ocurred while trying to compare a condition: {ae}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
        
    

if __name__ == "__main__":
    ##insert_test()
    search_test("Cierra")