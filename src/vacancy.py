class Vacancy:  # Создаем класс вакансии
    def __init__(self, name: str, salary: str, city: str, url: str,
                 trusted: bool, organization_name: str, schedule: str):
        self.name = name
        self.salary = salary
        self.city = city
        self.url = url
        self.trusted = trusted
        self.organization_name = organization_name
        self.schedule = schedule
        # Поля, необходимые при инициализации класса: профессия, з/п, город,
        # ссылка, проверенный статус, имя организации, график работы

    def __repr__(self):
        return (f"{self.__class__} ({self.name}, {self.salary}, {self.city}, "
                f"{self.url}, {self.trusted}, {self.organization_name}, {self.schedule}")

    def __str__(self):
        return (f"Профессия - {self.name}\n"
                f"Заработная плата - {self.salary}\n"
                f"Город - {self.city}\n"
                f"Ссылка - {self.url}\n"
                f"Статус проверено - {self.trusted}\n"
                f"Наименование организации - {self.organization_name}\n"
                f"График работы - {self.schedule}\n"
                "------------------------------------------------------")

    """Возвращаем информацию о вакансиях в удобном для чтения формте 
    с помощью магического метода __str__"""

    @staticmethod
    def get_salary_for_hh(salary):
        if salary is None:
            return "по результатам собеседования"
        else:
            if salary['from'] is None:
                return f"до {salary['to']}"
            elif salary['to'] is None:
                return f"от {salary['from']}"
            else:
                return f"от {salary['from']} до {salary['to']}"

    """Метод для преобразования з/п в удобный для пользователя формат,
    т к на обеих площадках з/п состоит и двух частей: от и до.
    Соответственно при выигрузке информации одно из полей (от или до)
    могут быть пустыми. Если оба поля пустых, то сообщаем. что з/п
    назначается по результатм собеседования (Head Hunter)"""

    @classmethod
    def create_exemplars_for_hh(cls, data):  # В параметр data будет передаваться вся информация о вакансиях
        list_of_exemplars = []  # Список, в котором будут храниться все экземпляры класса
        for vacancy in data['items']:  # проходимся по информации о вакансиях
            exemplar = Vacancy(vacancy['name'], cls.get_salary_for_hh(vacancy['salary']),
                               vacancy['area']['name'], vacancy['alternate_url'],
                               vacancy['employer']['trusted'], vacancy['employer']['name'],
                               vacancy['schedule']['name'])
            # Инициализируем экземпляры класса
            list_of_exemplars.append(exemplar)  # Добавляем экземпляр в список
        return list_of_exemplars  # Возвращаем список

    """Метод класса инициализирует экземпляры класса и возвращает список
    из экземпляров класса (Head Hunter)."""

    @staticmethod
    def get_salary_for_sj(data):
        if data['payment_from'] is None and data['payment_to'] is None:
            return "по результатам собеседования"
        elif data['payment_from'] is None:
            return f"до {data['payment_to']}"
        elif data['payment_to'] is None:
            return f"от {data['payment_from']}"
        else:
            return f"от {data['payment_from']} до {data['payment_to']}"

    """Метод для преобразования з/п в удобный для пользователя формат,
        т к на обеих площадках з/п состоит и двух частей: от и до.
        Соответственно при выигрузке информации одно из полей (от или до)
        могут быть пустыми. Если оба поля пустых, то сообщаем. что з/п
        назначается по результатм собеседования (Super Job)"""

    @classmethod
    def create_exemplars_for_sj(cls, data):  # В параметр data будет передаваться вся информация о вакансиях
        list_of_exemplars = []  # Список, в котором будут храниться все экземпляры класса
        for vacancy in data['objects']:  # проходимся по информации о вакансиях
            try:
                exemplar = Vacancy(vacancy['profession'], cls.get_salary_for_sj(vacancy),
                                   vacancy['client']['town']['title'], vacancy['client']['link'],
                                   True, vacancy['client']['title'], vacancy['type_of_work']['title'])
            except KeyError:
                continue
            # Инициализируем экземпляры класса, с обработкой исключений,
            # т к информация о вакансиях с платформы Super Job может выгружаться с отсутсвием
            # некоторых полей
            list_of_exemplars.append(exemplar)  # Добавляем экземпляр в список
        return list_of_exemplars  # Возвращаем список

    """Метод класса инициализирует экземпляры класса и возвращает список
        из экземпляров класса (Super Job)."""
