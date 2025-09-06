import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = None

chrome_options = webdriver.ChromeOptions()
firefox_options = webdriver.FirefoxOptions()
edge_options = webdriver.EdgeOptions()
#chrome_options.add_argument("--headless")  # Optional: headless mode
#firefox_options.add_argument("--headless")  # Optional: headless mode
#edge_options.add_argument("--headless")  # Optional: run in headless mode

chrome_options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,  # Allow upgrade of the download directory
    "safebrowsing.enabled": True  # Enable safe browsing to avoid warnings
})


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name == "firefox":
        service = Service(GeckoDriverManager().install())  # Use Service for the driver
        driver = webdriver.Firefox(service=service, options=firefox_options)
    elif browser_name == "edge":
        service = Service(EdgeChromiumDriverManager().install())  # Use Service for the driver
        driver = webdriver.Edge(service=service, options=edge_options)
    else:
        raise ValueError("Invalid browser name provided")

    driver.get("https://devrshub.forcetechnology.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()