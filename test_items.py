import time


# инициализируем переменную отвечающую за адрес страницы которую надо открыть
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# тест на проверку наличия кнопки buy на странице
def test_buy_button_existence(browser):
    # открытие страницы драйвером
    browser.get(link)
    # ищем кнопку buy
    buy_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    time.sleep(30)
    # проверяем что список buy_button не пустой
    assert len(buy_button) != 0, "Should not be empty"

