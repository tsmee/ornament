import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
class TestMessenger:
    def test_waiting_for_elements(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_link_text("Ask a Question").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//iframe[@name="intercom-launcher-frame"]')))
        launcher_frame = self.driver.find_element_by_xpath('//iframe[@name="intercom-launcher-frame"]')
        self.driver.switch_to_frame(launcher_frame)
        self.driver.find_element_by_css_selector("div[class*='intercom-launcher']")
        assert True
        print('intercom-launcher loaded successfully')
        self.driver.switch_to.parent_frame()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//iframe[@name="intercom-messenger-frame"]')))
        messenger_frame = self.driver.find_element_by_xpath('//iframe[@name="intercom-messenger-frame"]')
        self.driver.switch_to_frame(messenger_frame)
        self.driver.find_element_by_css_selector("div[class*='intercom-messenger']")
        assert True
        print('intercom-messenger loaded successfully')

    def test_messenger_is_closed(self):
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath("//a[@class='nuxt-link-active']").click()
        launcher_iframe = self.driver.find_elements_by_xpath('//iframe[@name="intercom-launcher-frame"]')
        messenger_iframe = self.driver.find_elements_by_xpath('//iframe[@name="intercom-messenger-frame"]')
        assert len(launcher_iframe) == 0
        assert len(messenger_iframe) == 0
        assert self.driver.current_url == 'https://ornament.health/'
        print('messenger is closed')
        self.driver.save_screenshot("screenshots/test_messenger.png")
