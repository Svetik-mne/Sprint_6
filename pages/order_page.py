import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Прокрутка до элемента {locator}")
    def scroll_to_element(self, locator):
        self.scroll_into_view(locator)

    @allure.step("Ввод имени: {name}")
    def input_name(self, name):
        self.input(OrderPageLocators.name, name)

    @allure.step("Ввод фамилии: {surname}")
    def input_surname(self, surname):
        self.input(OrderPageLocators.lastname, surname)

    @allure.step("Ввод адреса: {address}")
    def input_address(self, address):
        self.input(OrderPageLocators.address, address)

    @allure.step("Выбор станции метро: {station_name}")
    def enter_metro_station(self, station_name):
        self.click(OrderPageLocators.metro)
        self.input(OrderPageLocators.metro, station_name)
        self.click((By.XPATH, f'//div[@class="select-search__select"]//div[text()="{station_name}"]'))

    @allure.step("Ввод телефона: {phone}")
    def input_phone(self, phone):
        self.input(OrderPageLocators.phone, phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click(OrderPageLocators.button_next)

    @allure.step("Заполнение данных пользователя")
    def fill_personal_info(self, data):
        self.input_name(data["name"])
        self.input_surname(data["lastname"])
        self.input_address(data["address"])
        self.enter_metro_station(data["metro"])
        self.input_phone(data["phone"])
        self.click_next_button()

    @allure.step("Ввод даты аренды: {date_str}")
    def input_date(self, date_str):
        self.input(OrderPageLocators.date, date_str)
        self.find(OrderPageLocators.date).send_keys(Keys.ENTER)

    @allure.step("Выбор срока аренды: {period}")
    def select_rental_period(self, period):
        self.click(OrderPageLocators.field_rental_period)
        self.click((By.XPATH, f'//div[@class="Dropdown-menu"]/div[text()="{period}"]'))

    @allure.step("Выбор цвета самоката: {color_name}")
    def select_scooter_color(self, color_name):
        if "чёрный" in color_name:
            self.click(OrderPageLocators.checkbox_black_color_scooter)
        if "серый" in color_name:
            self.click(OrderPageLocators.checkbox_grey_color_scooter)

    @allure.step("Ввод комментария курьеру: {comment}")
    def input_comment(self, comment):
        self.input(OrderPageLocators.comment, comment)

    @allure.step("Заполнение данных аренды")
    def fill_rent_info(self, data):
        self.input_date(data["date"])
        self.select_rental_period(data["rental_period"])
        self.select_scooter_color(data["color"])
        self.input_comment(data["comment"])

    @allure.step("Клик по кнопке 'Заказать'")
    def click_make_order(self):
        self.click(OrderPageLocators.button_make_order)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.button_yes_confirm_order)

    @allure.step("Проверка появления кнопки 'Посмотреть статус'")
    def is_status_button_visible(self):
        return self.is_visible(OrderPageLocators.button_check_status_of_order)

    @allure.step("Проверка перехода на страницу аренды")
    def is_rent_page_title_visible(self):
        return self.is_visible(OrderPageLocators.title_page_rent)
