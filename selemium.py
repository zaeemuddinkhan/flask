# cross_browser_test.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def run_test(browser_name):
    try:
        # Initialize the WebDriver for the specified browser
        if browser_name.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            driver = webdriver.Firefox()
        elif browser_name.lower() == "safari":
            driver = webdriver.Safari()
        else:
            raise Exception("Unsupported browser")

        # Open the web application
        driver.get("https://codeforforce.com")

        # Perform actions (you can modify this based on your application)
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)

        # Wait for some time (in seconds) to observe the automation
        time.sleep(5)

    except Exception as e:
        print(f"Error in {browser_name} test: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    browsers = ["chrome", "firefox", "safari"]

    # Run the test for each browser
    for browser in browsers:
        run_test(browser)
