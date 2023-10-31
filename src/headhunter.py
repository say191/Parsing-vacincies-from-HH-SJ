from abc import ABC, abstractmethod
import requests
import json


class PlatformsAPI(ABC):
    @abstractmethod
    def get_vacancies(self, data):
        pass


class HeadHunterAPI(PlatformsAPI):
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
        response = requests.get('https://api.hh.ru/areas').text
        areas = json.loads(response)
        for area_state in areas[0]['areas']:
            if len(area_state['areas']) == 0:
                cities[area_state['name']] = area_state['id']
            for area_city in area_state['areas']:
                transform_city = []
                for word in area_city['name'].split(' '):
                    if '(' in word or ')' in word:
                        continue
                    transform_city.append(word)
                cities[' '.join(transform_city)] = int(area_city['id'])
        return cities[self.city]

    def get_vacancies(self, **kwargs):
        params = {}
        if self.city is None and self.salary is None:
            params = {'text': self.key_word,
                      'only_with_salary': True}
        elif self.city is None:
            params = {'text': self.key_word,
                      'salary': self.salary,
                      'only_with_salary': True}
        elif self.salary is None:
            params = {'text': self.key_word,
                      'area': self.get_city(),
                      'only_with_salary': True}
        elif self.key_word is None:
            params = {'salary': self.salary,
                      'area': self.get_city(),
                      'only_with_salary': True}
        response = requests.get("https://api.hh.ru/vacancies", params)
        self.vacancies = json.loads(response.text)
