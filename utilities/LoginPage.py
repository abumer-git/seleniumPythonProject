# utilities/LoginPage.py
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Locators as class variables ---
    LOGIN_BUTTON = (By.XPATH, "//span[contains(text(),'Login')]")
    EMAIL_INPUT = (By.NAME, "loginfmt")
    NEXT_BUTTON = (By.ID, "idSIButton9")
    PASSWORD_INPUT = (By.NAME, "passwd")
    SIGNIN_BUTTON = (By.ID, "idSIButton9")
    STAY_SIGNEDIN = (By.XPATH, "//input[@id='idSIButton9']")
    DASHBOARD_ELEMENTS = (By.XPATH, "//body/app-root[1]/app-layout[1]/div[1]/div[1]")

    # --- Page Actions ---

    def click_login_button(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)

    def click_next_button(self):
        next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_btn.click()

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)

    def click_signin_button(self):
        signin_btn = self.wait.until(EC.element_to_be_clickable(self.SIGNIN_BUTTON))
        signin_btn.click()

    def stay_signedin(self):
        try:
            # Wait for the element to be clickable and interact with it
            stay_signedin_btn = self.wait.until(
                EC.element_to_be_clickable(self.STAY_SIGNEDIN)
            )
            stay_signedin_btn.click()
        except StaleElementReferenceException:
            # Re-find the element and try again
            stay_signedin_btn = self.wait.until(
                EC.element_to_be_clickable(self.STAY_SIGNEDIN)
            )
            stay_signedin_btn.click()

    def dashboard(self):
        """Waits for the dashboard area and returns its visible text."""
        dashboard_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-layout[1]/div[1]/div[1]")
            )
        )
        return dashboard_element.text.strip()

