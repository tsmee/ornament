import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument('lang=en')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("https://ornament.health")
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestRedirect:
    def test_redirect(self):
        assert self.driver.current_url == "https://ornament.health/"
        self.driver.save_screenshot("screenshots/test_redirect.png")

