import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    # Инициализация Page Object
    calculator = CalculatorPage(driver)

    # 1. Открыть страницу калькулятора
    calculator.open_page(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Ввести значение 45 в поле задержки
    calculator.set_delay("45")

    # 3. Выполнить операцию: 7 + 8 =
    calculator.calculate("7+8=")

    # 4. Проверить результат через 45 секунд
    calculator.wait_for_result("15")
    assert calculator.get_result() == "15"
