from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import time
from concurrent.futures import ThreadPoolExecutor
error_message = "New record was not added successfully."

def init():
    chromedriver_autoinstaller.install(cwd=True)

def insert_test():
    try:
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
        time.sleep(500)
    except WebDriverException as e:
        print(f"❌ An error occurred while trying to install WebDriver: {e}")
    except AssertionError as ae:
        print(f"❌ An error was ocurred while trying to compare a condition: {ae}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        
def search_test(input):
    try:
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
        
def edit_edit():
    try:
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.find_element(By.ID, "edit-record-1").click()
        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.clear()
        first_name_field.send_keys("Jane")
        driver.find_element(By.ID, "submit").click()
        wait = WebDriverWait(driver, 10)
        rows = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group"))
        target_row = wait.until(
        lambda _ : next(
            (row for row in rows
            if "Jane" in row.text),
            None
         )
        )
        assert target_row is not None, error_message
        time.sleep(500)
        print("✅ Record edited successfully.")
    except WebDriverException as e:
        print(f"❌ An error occurred while trying to install WebDriver: {e}")
    except AssertionError as ae:
        print(f"❌ An error was ocurred while trying to compare a condition: {ae}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def delete_test():
    try:
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.find_element(By.ID, "delete-record-1").click()
        wait = WebDriverWait(driver, 10)
        rows = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group"))
        target_row = wait.until(
        lambda _ : next(
            (row for row in rows
            if "Cierra" in row.text),
            None
         )
        )
        assert target_row is None, error_message
        print("✅ Record deleted successfully.")
    except WebDriverException as e:
        print(f"❌ An error occurred while trying to install WebDriver: {e}")
    except AssertionError as ae:
        print(f"❌ An error was ocurred while trying to compare a condition: {ae}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
        
    

if __name__ == "__main__":
    init()
    with ThreadPoolExecutor() as executor:
        executor.submit(insert_test)
        executor.submit(search_test, "Alden")
        executor.submit(edit_edit)
        executor.submit(delete_test)