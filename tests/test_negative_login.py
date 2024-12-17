import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestNegativeScenarious:

    @pytest.mark.parametrize("username, password, expected_error_message", 
                        [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(driver, 10)

        # Log in with wrong credentials
        # Enter username
        username_locator = driver.find_element(By.ID, "username")
        wait.until(ec.presence_of_element_located((By.ID, "username")))
        username_locator.send_keys(username)

        # Enter password
        password_locator = driver.find_element(By.ID, "password")
        wait.until(ec.presence_of_element_located((By.ID, "password")))
        password_locator.send_keys(password)

        # press submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        wait.until(ec.element_to_be_clickable((By.ID, "submit")))
        submit_button_locator.click()

        # Verify new page URL hasn't changed
        current_url = driver.current_url
        assert current_url == "https://practicetestautomation.com/practice-test-login/"
        
        # Verify new page contains the expected_error_message 
        error_message_locator = driver.find_element(By.ID, "error") 
        wait.until(ec.visibility_of_all_elements_located((By.ID, "error")))
        assert error_message_locator.text == expected_error_message
