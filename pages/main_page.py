import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        super().open("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Прокрутка до секции FAQ")
    def scroll_to_faq_section(self):
        section = self.find(MainPageLocators.faq_section)
        self.driver.execute_script("arguments[0].scrollIntoView();", section)

    @allure.step("Клик по вопросу с индексом {index}")
    def click_question_by_index(self, index):
        self.click(MainPageLocators.faq_questions_items[index])

    @allure.step("Получение текста ответа по индексу {index}")
    def get_answer_text_by_index(self, index):
        return self.get_text(MainPageLocators.faq_answers_items[index])

    @allure.step("Проверить, что URL содержит '{expected_url}'")
    def check_url_contains(self, expected_url):
        assert self.is_url_contains(expected_url), f"Ожидали URL, содержащий {expected_url}"

    @allure.step("Клик по кнопке 'Заказать' в шапке сайта")
    def click_order_button_header(self):
        self.click(MainPageLocators.order_button_in_header)

    @allure.step("Клик по логотипу Самоката в шапке сайта")
    def click_logo_scooter(self):
        self.click(MainPageLocators.header_logo_scooter)

    @allure.step("Клик по логотипу Яндекса в шапке сайта")
    def click_logo_yandex(self):
        self.click(MainPageLocators.header_logo_yandex)