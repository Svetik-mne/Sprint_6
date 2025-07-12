import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import TestData

@pytest.mark.parametrize("button", [
    MainPageLocators.order_button_in_main,
    MainPageLocators.order_button_in_header
])
def test_order_form_first_step(driver, button):
    main_page = MainPage(driver)
    main_page.open()
    order_page = OrderPage(driver)

    order_page.scroll_to_element(button)
    order_page.click_button(button)

    order_page.fill_personal_info(TestData.test_data_user1)

    order_page.wait_visibility_of_element(OrderPageLocators.title_page_rent)

def test_order_form_second_step(driver):
    main_page = MainPage(driver)
    main_page.open()

    order_page = OrderPage(driver)
    order_page.scroll_to_element(MainPageLocators.order_button_in_main)
    order_page.click_button(MainPageLocators.order_button_in_main)

    order_page.fill_personal_info(TestData.test_data_user1)

    order_page.fill_rent_info(TestData.test_data_user1)

    order_page.click_button(OrderPageLocators.button_make_order)
    order_page.click_button(OrderPageLocators.button_yes_confirm_order)

    order_page.wait_visibility_of_element(OrderPageLocators.button_check_status_of_order)
