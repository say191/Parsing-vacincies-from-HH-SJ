from abc import ABC, abstractmethod
import json
import os


class JSONActions(ABC):  # Создаем абстрактный класс и абстрактный метод
    @abstractmethod
    def add_vacancies(self):
        pass


class JSONSaver(JSONActions):  # Создаем класс с атрибутом пути к файлу
    path = os.path.join(os.path.dirname(__file__), 'vacancies.csv')

    def __init__(self, data):
        self.data = data

    # При инициализации экземпляров поле data будем передавать выгруженную информацию о вакансиях
    def add_vacancies(self):
        with open(self.path, 'w') as file:  # Открываем файл с модификацией на запись
            json.dump(self.data, file, indent=4)  # Записываем информацию в файл в формате json

    """Данный метод записывает в файл всю информацию о вакансиях в файл в формате json,
    если файла нету, то он создатся автоматически"""
