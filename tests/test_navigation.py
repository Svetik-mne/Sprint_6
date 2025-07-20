import pytest
import allure
from pages.main_page import MainPage
from urls import BASE_URL


@allure.suite("Переходы по логотипам")
class TestLogoRedirects:

    @allure.title("Проверка, что логотип Самоката ведет на главную страницу")
    def test_logo_scooter_redirects_to_main(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_order_button_header()
        page.click_logo_scooter()
        page.check_url_contains(BASE_URL)

    @allure.title("Проверка, что логотип Яндекса открывает Dzen в новой вкладке")
    def test_logo_yandex_redirects_to_dzen(self, driver):
        page = MainPage(driver)
        page.open()
        original_window = driver.current_window_handle
        page.click_logo_yandex()
        page.switch_to_new_window(original_window)
        page.check_url_contains("dzen")
