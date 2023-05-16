


from data.data import Person # подключаем класс Person из data
from faker import Faker #подключаем библиотеку faker для работы с полями

faker_ru = Faker('ru_RU') # для обозначения русского языка
Faker.seed()


# Генерация данных для ввода в форму
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )



