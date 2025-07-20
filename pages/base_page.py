from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input(self, locator, value):
        self.find(locator).send_keys(value)

    def get_text(self, locator):
        return self.find(locator).text

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def is_url_contains(self, expected_url):
        return expected_url in self.driver.current_url

    def switch_to_new_window(self, original_window):
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)
