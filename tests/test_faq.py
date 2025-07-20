import pytest
import allure
from data import TestData
from pages.main_page import MainPage


@allure.suite("FAQ секция")
class TestFAQ:

    @allure.title("Проверка отображения ответа на вопрос в FAQ по индексу {index}")
    @pytest.mark.parametrize("index, expected_answer", TestData.test_data_question_answer)
    def test_faq_questions(self, driver, index, expected_answer):
        page = MainPage(driver)
        page.open()
        page.scroll_to_faq_section()
        page.click_question_by_index(index)
        actual_answer = page.get_answer_text_by_index(index)
        assert expected_answer in actual_answer
