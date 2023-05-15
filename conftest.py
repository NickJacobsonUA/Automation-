# используется для написания фикстуры открытия браузера
# для каждого теста
# фикстуры - функции, которые позволяют выполнять что либо до или после теста
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function") # для что бы определить функцию фикстурой нужен декоратор
#scope="function" это дефолтное состояние, которое используется для открытия браузера в setup и закрытия в teardown каждого теста
# что бы тесты были независимые

def driver():  #фикстура создания драйвера. Открыте и после выполнения теста закрытие.
    driver = driver = webdriver.Chrome(ChromeDriverManager().install()) #открытие браузера
    driver.maximize_window() #открытие браузера на весь экран
    yield driver  #teardown фикстуры - операции после завершения теста
    driver.quit() # выход из браузера
    # переходим к построению теста базовой страницы