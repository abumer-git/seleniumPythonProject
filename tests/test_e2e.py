import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By
import time
from utilities.BaseClass import BaseClass
from utilities.test_data import LoginData
from utilities.LoginPage import LoginPage
import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=5)
class Test_rshub(BaseClass):
    def test_login_1(self):
        log = self.getLogger()
        self.implicitly_wait()

        # Create LoginPage object and pass driver from BaseClass
        login_page = LoginPage(self.driver)

        log.info("Clicking login button")
        login_page.click_login_button()

        log.info("Entering email")
        login_page.enter_email(LoginData.valid_user["email"])

        log.info("Clicking Next button")
        login_page.click_next_button()

        log.info("Entering password")
        login_page.enter_password(LoginData.valid_user["password"])

        log.info("Clicking Sign in button")
        login_page.stay_signedin()

        log.info("Stay Signed-In")
        login_page.stay_signedin()

        # ----------------------------------------------------------------------

        # ✅ Get dashboard text
        log.info("Getting dashboard text")
        dashboard_text = login_page.dashboard()
        log.info("Dashboard text captured: " + dashboard_text)

        # ✅ Assert expected content is present
        assert "Dashboard" in dashboard_text or "FT Users" in dashboard_text, \
            f"Expected dashboard text not found. Got: {dashboard_text}"

        log.info("Login test passed successfully.")
