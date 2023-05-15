
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
# создание класса и объявление переменных которые будут наследоваться
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver  # объявление переменных
        self.url = url

# Opening browser and pasting a URL into the address line

    def open(self):
       self.driver.get(self.url)

# Методы для работы со страницами

# 1 - поиск страницы
    # Видимый элемент
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    def element_is_present(self, locator, timeout=5): # Поиск элемента по DOM дереву если самого жлемента не видно
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    def elements_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    def go_to_element(self, element): # скроллинг к нужному элементу
        self.driver.execute_script("argument[0].scrollIntoView();", element)




