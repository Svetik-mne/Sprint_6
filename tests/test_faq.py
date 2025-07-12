import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TestData
from locators.main_page_locators import MainPageLocators


@pytest.mark.parametrize("index, expected_answer", TestData.test_data_question_answer)
def test_faq_questions(driver, index, expected_answer):
    driver.get(TestData.scooter_address)


    faq_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.faq_section)
    )
    driver.execute_script("arguments[0].scrollIntoView();", faq_section)


    question_locator = MainPageLocators.faq_questions_items[index]
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(question_locator)
    ).click()


    answer_locator = MainPageLocators.faq_answers_items[index]
    answer_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(answer_locator)
    )

    assert expected_answer in answer_element.text
