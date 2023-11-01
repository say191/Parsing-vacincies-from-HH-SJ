from abc import ABC, abstractmethod
import requests
import json
import os


class PlatformsAPI(ABC):  # Создаем абстрактный класс и абстрактный метод
    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJobAPI(PlatformsAPI):  # Создаем класс, наследуемый от абстрактного класса
    vacancies = {}  # Атрибут класса, в котором будет хранится вся информация о вакансиях

    def __init__(self, key_word: str = None, salary: int = None, city: str = None):
        self.key_word = key_word
        self.city = city
        self.salary = salary

    # Поля класса, необходимые для инициализации экземпляров класса
    # По умолчанию всем присвоенно значение None, т к мы не знаем, по каким критериям
    # поиска будут выигружаться вакансии
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
        cities = {}  # В переменной будут храниться все города РФ, в формате словаря (Название города: id)
        response = requests.get('https://api.superjob.ru/2.0/towns/?all=True').text
        # Записываем в переменную всю информацию о ородах через api
        areas = json.loads(response)
        # Преобразуем в формат json
        for area_state in areas['objects']:  # Проходим по каждой области
            cities[area_state['title']] = area_state['id']
            # Добавляем в словарь ключ (наименование города) и значение (id uорода)
        return cities[self.city]  # Возвращем id города по наименованию корода, который ввел пользователь

    """Данные метод возвращает имя города в строковом значении.
        Метод реализован, для того, чтобы при вводе пользователем неправильного
        имени города, пользователю выводилось соответствующее замечание.
        """

    def get_vacancies(self, **kwargs):
        params = {}  # Переменная в которой будут храниться значения параметров поиска вакансий
        apikey = os.getenv('API_KEY')
        # Переменная в которй будет хранится api ключ, записанный в виртуальную среду
        url = 'https://api.superjob.ru/2.0/vacancies/'  # Исходная ссылка на вакансии через api

        if self.city is None and self.salary is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову
            params = {'keywords': self.key_word,
                      'no_agreement': 1}
        elif self.city is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову и з/п
            params = {'keyword': self.key_word,
                      'payment_from': self.salary,
                      'no_agreement': 1}
        elif self.salary is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову и городу
            params = {'keyword': self.key_word,
                      'town': self.get_city(),
                      'no_agreement': 1}
        elif self.key_word is None:
            # Если пользователь выбрал поиск вакансий по з/п и городу
            params = {'payment_from': self.salary,
                      'town': self.get_city(),
                      'no_agreement': 1}

        response = requests.get(url, headers={'X-Api-App-Id': apikey}, params=params)
        # Записываем в перемнную всю информацию о вакансиях SuperJob
        self.vacancies = json.loads(response.text)
        # Записываем информацию в атрибут класса в формате json
        """Данные метод выгружает всю информацию о вакансиях с платформы Head Hunter
            и записывает эту информацию в атрибут класса vacancies в формате json"""
