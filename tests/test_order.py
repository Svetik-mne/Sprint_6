import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import TestData

@allure.suite("Оформление заказа")
class TestOrder:

    @pytest.mark.parametrize("button, case_name", [
        (MainPageLocators.order_button_in_main, "через кнопку в теле страницы"),
        (MainPageLocators.order_button_in_header, "через кнопку в шапке")
    ])
    @allure.title("Переход ко второму шагу оформления заказа {case_name}")
    def test_order_form_first_step(self, driver, button, case_name):
        main_page = MainPage(driver)
        main_page.open()
        order_page = OrderPage(driver)

        order_page.scroll_to_element(button)
        order_page.click_button(button)
        order_page.fill_personal_info(TestData.test_data_user1)

        assert order_page.is_visible(OrderPageLocators.title_page_rent), \
            "Заголовок второго шага формы заказа не появился"

    @allure.title("Полное оформление заказа — до появления кнопки 'Посмотреть статус'")
    def test_order_form_second_step(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        order_page = OrderPage(driver)
        order_page.scroll_to_element(MainPageLocators.order_button_in_main)
        order_page.click_button(MainPageLocators.order_button_in_main)

        order_page.fill_personal_info(TestData.test_data_user1)
        order_page.fill_rent_info(TestData.test_data_user1)

        order_page.click_button(OrderPageLocators.button_make_order)
        order_page.click_button(OrderPageLocators.button_yes_confirm_order)

        assert order_page.is_visible(OrderPageLocators.button_check_status_of_order), \
            "Кнопка 'Посмотреть статус' не появилась — заказ не завершён"
