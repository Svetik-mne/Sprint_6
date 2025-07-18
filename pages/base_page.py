import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        with allure.step(f"Открыть страницу {url}"):
            self.driver.get(url)

    def click(self, locator):
        with allure.step(f"Клик по элементу {locator}"):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.find(locator).text

    def switch_to_new_window(self, original_window):
        with allure.step("Переключение на новое окно браузера"):
            self.wait.until(lambda d: len(d.window_handles) > 1)
            new_window = next(w for w in self.driver.window_handles if w != original_window)
            self.driver.switch_to.window(new_window)

    def is_url_contains(self, text):
        with allure.step(f"Проверка, что URL содержит '{text}'"):
            return self.wait.until(lambda d: text in d.current_url)
