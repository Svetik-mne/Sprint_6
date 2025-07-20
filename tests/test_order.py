import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import TestData
from locators.main_page_locators import MainPageLocators


@allure.suite("Оформление заказа")
class TestOrder:

    @pytest.mark.parametrize("button_locator, case_name", [
        (MainPageLocators.order_button_in_main, "через кнопку в теле страницы"),
        (MainPageLocators.order_button_in_header, "через кнопку в шапке")
    ])
    @allure.title("Переход ко второму шагу оформления заказа {case_name}")
    def test_order_form_first_step(self, driver, button_locator, case_name):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(button_locator)

        order_page = OrderPage(driver)
        order_page.fill_personal_info(TestData.test_data_user1)

        assert order_page.is_rent_page_title_visible(), "Форма аренды не появилась"

    @allure.title("Полное оформление заказа — до появления кнопки 'Посмотреть статус'")
    def test_order_form_second_step(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(MainPageLocators.order_button_in_main)

        order_page = OrderPage(driver)
        order_page.fill_personal_info(TestData.test_data_user1)
        order_page.fill_rent_info(TestData.test_data_user1)
        order_page.click_make_order()  # Не забудь вызвать перед confirm!
        order_page.confirm_order()

        assert order_page.is_status_button_visible(), "Кнопка 'Посмотреть статус' не появилась"

