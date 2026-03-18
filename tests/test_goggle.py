import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_google_searchbox(driver):
    driver.get("https://www.google.com")
    searchbox = driver.find_element(By.NAME, "q")
    assert searchbox.is_displayed()

def test_google_search(driver):
    driver.get("https://www.google.com")
    searchbox = driver.find_element(By.NAME, "q")
    searchbox.send_keys("Jenkins CI/CD")
    searchbox.submit()
    assert "Google" in driver.title
