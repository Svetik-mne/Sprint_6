import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait

def test_logo_scooter_redirects_to_main(driver):
    page = MainPage(driver)
    page.open()
    page.click_order_button_header()
    page.click_logo_scooter()
    WebDriverWait(driver, 10).until(lambda d: "https://qa-scooter.praktikum-services.ru/" in d.current_url)
    assert "https://qa-scooter.praktikum-services.ru/" in driver.current_url

def test_logo_yandex_redirects_to_dzen(driver):
    page = MainPage(driver)
    page.open()
    original_window = driver.current_window_handle
    page.click_logo_yandex()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)
    assert "dzen.ru" in driver.current_url
