from selenium.webdriver.common.by import By


class MainPageLocators:

    main_header = (By.XPATH, '//div[contains(@class, "Home_Header")]')
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    faq_questions_items = {
        0: (By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'),
        1: (By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'),
        2: (By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'),
        3: (By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'),
        4: (By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'),
        5: (By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'),
        6: (By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'),
        7: (By.XPATH, '//div[@id="accordion__heading-7"]/parent::div'),
        8: (By.XPATH, '//div[@id="accordion__heading-8"]/parent::div'),
    }


    faq_answers_items = {
        0: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        1: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-7"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-8"]'),
    }

    order_button_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')

    order_button_in_header = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')

    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')

    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')

    title_dzen = (By.TAG_NAME, 'title')
