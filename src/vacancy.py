class Vacancy:
    def __init__(self, name: str, salary: str, city: str, url: str,
                 trusted: bool, organization_name: str, schedule: str):
        self.name = name
        self.salary = salary
        self.city = city
        self.url = url
        self.trusted = trusted
        self.organization_name = organization_name
        self.schedule = schedule

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

    @classmethod
    def create_exemplars_for_hh(cls, data):
        list_of_exemplars = []
        for vacancy in data['items']:
            exemplar = Vacancy(vacancy['name'], cls.get_salary_for_hh(vacancy['salary']),
                               vacancy['area']['name'], vacancy['alternate_url'],
                               vacancy['employer']['trusted'], vacancy['employer']['name'],
                               vacancy['schedule']['name'])
            list_of_exemplars.append(exemplar)
        return list_of_exemplars

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

    @classmethod
    def create_exemplars_for_sj(cls, data):
        list_of_exemplars = []
        for vacancy in data['objects']:
            try:
                exemplar = Vacancy(vacancy['profession'], cls.get_salary_for_sj(vacancy),
                                   vacancy['client']['town']['title'], vacancy['client']['link'],
                                   True, vacancy['client']['title'], vacancy['type_of_work']['title'])
            except KeyError:
                continue
            list_of_exemplars.append(exemplar)
        return list_of_exemplars
