from abc import ABC, abstractmethod
import json
import os


class JSONActions(ABC):
    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancies):
        pass

    @abstractmethod
    def sorted_vacancies(self, vacancies):
        pass


class JSONSaver(JSONActions):
    path = os.path.join(os.path.dirname(__file__), 'vacancies.csv')

    def __init__(self, data):
        self.data = data

    def add_vacancies(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_vacancy_by_salary(self, vacancies):
        pass

    def delete_vacancies(self, vacancies):
        pass

    def sorted_vacancies(self, vacancies):
        pass
