import time

from selenium.webdriver.common.by import By


class TestPositiveScenarious:
    def test_positive_login(self, driver):
        # create the driver

        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Verify successful login with valid credentials
        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.ID, "password")
        submit_button_locator = driver.find_element(By.ID, "submit")

        username_locator.send_keys("student")
        password_locator.send_keys("Password123")
        submit_button_locator.click()

        time.sleep(4)
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        current_url = driver.current_url
        assert current_url == "https://practicetestautomation.com/logged-in-successfully/"
        text_locator = driver.find_element(By.TAG_NAME, "h1")        
        
        # Verify new page contains expected text ('Logged In Successfully')
        assert text_locator.text == "Logged In Successfully"

        # Verify Log out button is displayed on the new page
        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed()