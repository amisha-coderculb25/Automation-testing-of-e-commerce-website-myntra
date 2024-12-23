from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class MyntraTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_and_add_lakme_lipstick_and_tshirt_to_cart(self):
        driver = self.driver
        driver.get("https://www.myntra.com")

        # Wait for the page to be fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        # Wait for the search bar to be present and search for "lipstick"
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "desktop-searchBar"))
        )
        search_bar.clear()
        search_bar.send_keys("lipstick")
        time.sleep(3)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the filter options to load and select the "Lakme" brand filter
        lakme_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@title='Lakme 9to5 Powerplay Priming Matte Lipstick, Lasts 16hrs, Deep Wine, 3.6g']"))
        )
        lakme_filter.click()

        # Wait for the products to load
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-base"))
        )
        self.assertGreater(len(products), 0)

        # Click the first product
        products[0].click()

        # Switch to the new window/tab if one is opened
        driver.switch_to.window(driver.window_handles[1])

        # Wait for the add to bag button to be clickable and click it
        add_to_bag_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pdp-add-to-bag"))
        )
        add_to_bag_button.click()

        # Switch back to the original window/tab
        driver.switch_to.window(driver.window_handles[0])

        # Wait for the search bar to be present and search for "tshirt"
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "desktop-searchBar"))
        )
        search_bar.clear()
        search_bar.send_keys("tshirt")
        time.sleep(3)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the products to load
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-base"))
        )
        self.assertGreater(len(products), 0)

        # Click the first product
        products[0].click()

        # Switch to the new window/tab if one is opened
        driver.switch_to.window(driver.window_handles[1])

        # Wait for the add to bag button to be clickable and click it
        add_to_bag_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pdp-add-to-bag"))
        )
        add_to_bag_button.click()

        # Verify the products are in the bag
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "desktop-bagIcon"))
        ).click()
        cart_items = driver.find_elements(By.CLASS_NAME, "itemContainer-base")
        self.assertGreater(len(cart_items), 0)

    def tearDown(self):
        try:
            self.driver.quit()
        except:
            pass  # Ignore errors if the window is already closed

if __name__ == "__main__":
    unittest.main()
