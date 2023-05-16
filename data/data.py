

# Создание класса который хранит параметры для формы (человека)
from dataclasses import dataclass


@dataclass
# нужно описывать тип свойств класса (str)
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None