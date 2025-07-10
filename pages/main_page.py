from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators:
    order_button_in_header = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_order_button_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.order_button_in_header)).click()

    def click_logo_scooter(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.header_logo_scooter)).click()

    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.header_logo_yandex)).click()
