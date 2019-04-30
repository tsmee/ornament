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
class TestText:
    def test_text_fullscreen(self):
        visible_text = self.driver.find_element_by_xpath("//*[contains(text(), 'A modern mobile app for keeping track "
                                                    "of lab test results and analyze their dynamics')]").text
        assert visible_text == 'A modern mobile app for keeping track of lab test results and analyze their dynamics'

    def test_text_767(self):
        self.driver.set_window_size(767, 800)
        visible_text = self.driver.find_element_by_xpath("//*[contains(text(), 'A modern mobile app for keeping track "
                                                         "of lab test results and analyze their dynamics')]").text
        assert visible_text == ""
        print('text is not visible')
        self.driver.save_screenshot("screenshots/test_text.png")
