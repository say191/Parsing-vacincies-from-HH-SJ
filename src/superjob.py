from abc import ABC, abstractmethod
import requests
import json
import os


class PlatformsAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJobAPI(PlatformsAPI):
    vacancies = {}

    def __init__(self, key_word: str = None, salary: int = None, city: str = None):
        self.key_word = key_word
        self.city = city
        self.salary = salary

    def __repr__(self):
        return f"{self.__class__}: ({self.key_word}, {self.salary}, {self.city})"

    def __str__(self):
        if self.city is None and self.salary is None:
            return f"Вакансии по запросам: ключевые слова - '{self.key_word}'"
        elif self.city is None:
            return f"Вакансии по запросам: ключевые слова - '{self.key_word}', з/п - {self.salary}"
        elif self.key_word is None:
            return f"Вакансии по запросам: з/п - '{self.salary}', город - {self.city}"
        else:
            return f"Вакансии по запросам: ключевые слова - '{self.key_word}', з/п - {self.salary}, город - {self.city}"

    def get_city(self):
        cities = {}
        response = requests.get('https://api.superjob.ru/2.0/towns/?all=True').text
        areas = json.loads(response)
        for area_state in areas['objects']:
            cities[area_state['title']] = area_state['id']
        return cities[self.city]

    def get_vacancies(self, **kwargs):
        apikey = os.getenv('API_KEY')
        url = 'https://api.superjob.ru/2.0/vacancies/'

        if self.city is None and self.salary is None:
            params = {'keywords': self.key_word,
                      'no_agreement': 1}
        elif self.city is None:
            params = {'keyword': self.key_word,
                      'payment_from': self.salary,
                      'no_agreement': 1}
        elif self.salary is None:
            params = {'keyword': self.key_word,
                      'town': self.get_city(),
                      'no_agreement': 1}
        elif self.key_word is None:
            params = {'payment_from': self.salary,
                      'town': self.get_city(),
                      'no_agreement': 1}

        response = requests.get(url, headers={'X-Api-App-Id': apikey}, params=params)
        self.vacancies = json.loads(response.text)
