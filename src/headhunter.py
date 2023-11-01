from abc import ABC, abstractmethod
import requests
import json


class PlatformsAPI(ABC):  # Создаем абстрактный класс и абстрактный метод
    @abstractmethod
    def get_vacancies(self, data):
        pass


class HeadHunterAPI(PlatformsAPI):  # Создаем класс, наследуемый от абстрактного класса
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
        response = requests.get('https://api.hh.ru/areas').text
        # Записываем в переменную всю информацию о ородах через api
        areas = json.loads(response)  # Преобразуем в формат json
        for area_state in areas[0]['areas']:  # Проходим по каждой области
            if len(area_state['areas']) == 0:
                # Данным условием мы отсеиваем все города кроме Москвы и Санкт-Петербурга,
                # т к на данной платформе, у этих городов в словаре отсуствует ключ - область
                cities[area_state['name']] = area_state['id']  # Записываем в словарь эти города
            for area_city in area_state['areas']:  # Проходим по каждому городу
                transform_city = []
                # Переменная, куда будет добавляться 'чистое' имя города
                # Например вместа Иваново (Ивановская область) будет просто Иваново
                for word in area_city['name'].split(' '):
                    # Разбиваем имя города на слова по пробелам
                    # Например Иваново (Ивановская область) - ['Иваново', '(Ивановская', 'область)']
                    # И проходимся по этому списку слов
                    if '(' in word or ')' in word:  # Отсеиваем слова в скобках
                        continue
                    transform_city.append(word)  # Записываем в списко 'чистое' имя города без области в скобках
                cities[' '.join(transform_city)] = int(area_city['id'])
                # соединяем слова в одно слово и записываем в ключ словаря - имя города, а в значние id города
        return cities[self.city]  # возвращаем значение id города по ключу (наименованию города)

    """Данные метод возвращает имя города в строковом значении.
    Метод реализован, для того, чтобы при вводе пользователем неправильного
    имени города, пользователю выводилось соответствующее замечание.
    """

    def get_vacancies(self, **kwargs):
        params = {}  # Переменная в которой будут храниться значения параметров поиска вакансий
        if self.city is None and self.salary is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову
            params = {'text': self.key_word,
                      'only_with_salary': True}
        elif self.city is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову и з/п
            params = {'text': self.key_word,
                      'salary': self.salary,
                      'only_with_salary': True}
        elif self.salary is None:
            # Если пользователь выбрал поиск вакансий по ключевому слову и городу
            params = {'text': self.key_word,
                      'area': self.get_city(),
                      'only_with_salary': True}
        elif self.key_word is None:
            # Если пользователь выбрал поиск вакансий по з/п и городу
            params = {'salary': self.salary,
                      'area': self.get_city(),
                      'only_with_salary': True}
        response = requests.get("https://api.hh.ru/vacancies", params)
        # Выгружаем информацию о вакансиях в соответсвии с выбранными параметрами посика
        self.vacancies = json.loads(response.text)  # Записываем информацию в json формате в атрибут класса

    """Данные метод выгружает всю информацию о вакансиях с платформы Head Hunter
    и записывает эту информацию в атрибут класса vacancies в формате json"""
