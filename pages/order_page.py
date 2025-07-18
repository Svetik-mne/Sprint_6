from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_visibility_of_element(self, locator):
        return self.wait.until(lambda d: d.find_element(*locator).is_displayed())

    def scroll_to_element(self, locator):
        element = self.wait.until(lambda d: d.find_element(*locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_button(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_name(self, name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="* Имя"]').send_keys(name)

    def input_surname(self, surname):
        self.driver.find_element(By.XPATH, '//input[@placeholder="* Фамилия"]').send_keys(surname)

    def input_address(self, address):
        self.driver.find_element(By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]').send_keys(address)

    def enter_metro_station(self, station_name):
        metro_input = self.wait.until(lambda d: d.find_element(By.XPATH, '//input[@placeholder="* Станция метро"]'))
        metro_input.click()
        metro_input.send_keys(station_name)
        self.wait.until(
            lambda d: d.find_element(By.XPATH, f'//div[@class="select-search__select"]//div[text()="{station_name}"]')
        ).click()

    def input_phone(self, phone):
        self.driver.find_element(By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]').send_keys(phone)

    def click_next_button(self):
        self.click_button((By.XPATH, '//button[text()="Далее"]'))

    def fill_personal_info(self, data):
        self.input_name(data["name"])
        self.input_surname(data["lastname"])
        self.input_address(data["address"])
        self.enter_metro_station(data["metro"])
        self.input_phone(data["phone"])
        self.click_next_button()

    def input_date(self, date_str):
        date_input = self.driver.find_element(By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
        date_input.send_keys(date_str)
        date_input.send_keys(Keys.ENTER)

    def select_rental_period(self, period):
        self.click_button((By.XPATH, '//div[@class="Dropdown-control"]'))
        self.click_button((By.XPATH, f'//div[@class="Dropdown-menu"]/div[text()="{period}"]'))

    def select_scooter_color(self, color_name):
        if "чёрный" in color_name:
            self.driver.find_element(By.ID, 'black').click()
        if "серый" in color_name:
            self.driver.find_element(By.ID, 'grey').click()

    def input_comment(self, comment):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Комментарий для курьера"]').send_keys(comment)

    def fill_rent_info(self, data):
        self.input_date(data["date"])
        self.select_rental_period(data["rental_period"])
        self.select_scooter_color(data["color"])
        self.input_comment(data["comment"])
