from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the Instagram page
    driver.get("https://www.instagram.com/guviofficial/")

    # Give some time for the page to load
    time.sleep(5)

    # Use WebDriverWait to wait until the followers/following elements are clickable
    # ffp stands for follower_following_path
    ffp = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'x78zum5 x1q0g3np xieb3on')]"))
    )

    # Find list items within the ul
    items = ffp.find_elements(By.XPATH, ".//li[contains(@class, 'xl565be x1m39q7l x1uw6ca5 x2pgyrj')]")

    # Loop through the items, skipping the first element
    for li in items[1:]:
        print(li.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()