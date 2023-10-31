from funcs.user_interaction import (search_query, user_action, user_action_1,
                                    user_action_2, user_action_3, user_action_4)
from src.vacancy import Vacancy
from src.headhunter import HeadHunterAPI
from src.superjob import SuperJobAPI
from src.jsonactions import JSONSaver

name_user = input('Введите ваше имя:\n')  # Просим ввести имя пользователя и записываем его в переменную

while True:  # Запускаем бесконечный цикл для реализации консольного меню
    action = search_query(name_user)  # Выводим список площадок, откуда мы будем парсить данные о вакансиях

    if action == '1':  # Если выбрали площадку Head Hunter
        while True:  # Запускаем бесконечный цикл для реализации консольного подменю
            action = user_action()  # Выводим список доступных действий

            if action == '1':  # Если выбрали поиск вакансии по ключевому слову
                hh_api = HeadHunterAPI(user_action_1())
                # Инициализируем экземпляр класса HeadHunerAPI, где при инициализации передаем атрибут
                # ключевого слова (Т к в списке действий мы выбрали поиск исключительно по ключевому слову
                # Функция user_action_1() возвращает ключевое слово, которое мы передаем
                # классу при инициализации
                hh_api.get_vacancies()
                # Использую метод класса get_vacansies() записываем список, выгруженных с платформы
                # вакансий в атрибут класса vacancies
                hh_vacancy = Vacancy  # Инициализируем экземпляр класса Vacancy
                list_exemplars = hh_vacancy.create_exemplars_for_hh(hh_api.vacancies)
                # С помощью метода класса create_exemplars_for_hh создаем экземпляры класса Vacancy
                # и возвращаем список из этих самых экземпляров
                for i in list_exemplars:  # Проходим по списку из экземпляров вакансий
                    print(str(i))
                    # Выводим пользователю на экран всю информацию об вакансиях в удобном формате
                    # используя магический метод __str__

                json_hh = JSONSaver(hh_api.vacancies)  # Инициализируем экземпляр класса JSONSaver
                json_hh.add_vacancies()  # Записываем список вакансий в файл 'vacancies.csv' в json формате
                quit()  # Завершаем программу

            elif action == '2':  # Если выбрали поиск вакансии по ключевому слову и з/п
                search_options = user_action_2()
                # Записываем параметры поиска, которые были возвращены с помощью функции
                # user_action_2() в переменную
                hh_api = HeadHunterAPI(key_word=search_options[0], salary=search_options[1])
                # Инициализируем экземпляр класса с параметрами поиска: ключевое слово и з/п
                hh_api.get_vacancies()
                hh_vacancy = Vacancy
                list_exemplars = hh_vacancy.create_exemplars_for_hh(hh_api.vacancies)
                for i in list_exemplars:
                    print(str(i))

                json_hh = JSONSaver(hh_api.vacancies)
                json_hh.add_vacancies()
                quit()
                # Все остальные действия выполняются аналогично первому блоку,
                # когда мы делали поиск исключительно по ключевому слову

            elif action == '3':  # Если выбрали поиск вакансии по ключевому слову и городу
                while True:
                    # Запускаем бесконечный цикл, который будет работать, пока пользователь
                    # не введет корректное название города
                    try:  # Проверям блок на наличие ошибок
                        search_options = user_action_3()
                        hh_api = HeadHunterAPI(key_word=search_options[0], city=search_options[1])
                        # Инициализируем экземпляр класса с параметрами поиска: ключевое слово и город
                        hh_api.get_vacancies()
                        hh_vacancy = Vacancy
                        list_exemplars = hh_vacancy.create_exemplars_for_hh(hh_api.vacancies)
                        for i in list_exemplars:
                            print(str(i))
                        json_hh = JSONSaver(hh_api.vacancies)
                        json_hh.add_vacancies()
                        quit()
                    except KeyError:  # Обрабатываем исключения
                        print('Введите правильное имя города на руском языке!')
                        # Если блок поймает ошибку KeyError, пользователю выйдет соответствующее сообщение
                        continue
                        # Возвращаемся в начало блока, если пользователь ввел неправильное
                        # имя города, спровацировав ошибку KeyError

            elif action == '4':
                while True:
                    try:
                        search_options = user_action_4()
                        hh_api = HeadHunterAPI(salary=search_options[0], city=search_options[1])
                        # Инициализируем экземпляр класса с параметрами поиска: з/п и город
                        hh_api.get_vacancies()
                        hh_vacancy = Vacancy
                        list_exemplars = hh_vacancy.create_exemplars_for_hh(hh_api.vacancies)
                        for i in list_exemplars:
                            print(str(i))
                        json_hh = JSONSaver(hh_api.vacancies)
                        json_hh.add_vacancies()
                        quit()
                    except KeyError:
                        print('Введите правильное имя города на руском языке!')
                        continue
            elif action == '0':
                quit()
            else:
                print("Пожалуйта, введите корректное значение")
                continue
    elif action == '2':  # Если выбрали SuperJob
        while True:  # Запускаем бесконечный цикл, для реализации консольного меню
            action = user_action()  # Выводим на экран список доступных действий и записываем имя пользователя

            if action == '1':  # Если выбрали поиск вакансий по ключевому слову
                sj_api = SuperJobAPI(key_word=user_action_1())
                # Инициализируем экземпляр класса с параметрами поиска по ключевому слову
                sj_api.get_vacancies()
                # Возвращаем в атрибут класса список вакансий
                sj_vacancy = Vacancy
                # Создаем экземпляр класса вакансии
                list_exemplars = sj_vacancy.create_exemplars_for_sj(sj_api.vacancies)
                # Записываем в переменную список из экземпляров класса вакансии с помощию метода

                for i in list_exemplars:  # Проходим по каждому экземпляру
                    print(str(i))  # Выводим на экран вакансии в удобном формате с помощью __str__

                json_sj = JSONSaver(sj_api.vacancies)  # Инициализируем экземпляр класса
                json_sj.add_vacancies()  # Записываем информацию о вакансиях в файл в формате json
                quit()
            if action == '2':  # Если выбрали поиск вакансий по ключевому слову и з/п
                search_options = user_action_2()  # записываем в переменную параметры поиска
                sj_api = SuperJobAPI(key_word=search_options[0], salary=search_options[1])
                # Инициализируем экземпляр класса с параметрами поиска
                sj_api.get_vacancies()
                sj_vacancy = Vacancy
                list_exemplars = sj_vacancy.create_exemplars_for_sj(sj_api.vacancies)

                for i in list_exemplars:
                    print(str(i))

                json_sj = JSONSaver(sj_api.vacancies)
                json_sj.add_vacancies()
                quit()
            if action == '3':  # Если выбрали поиск вакансий по ключевому слову и городу
                while True:
                    # Запускем бесконечный цикл для введения параметров поиска, после неудачной обработки исключений
                    try:  # Обрабатываем исключения
                        search_options = user_action_3()
                        # Записываем в переменную параметры поиска: ключевое слово и город
                        sj_api = SuperJobAPI(key_word=search_options[0], city=search_options[1])
                        sj_api.get_vacancies()
                        sj_vacancy = Vacancy
                        list_exemplars = sj_vacancy.create_exemplars_for_sj(sj_api.vacancies)

                        for i in list_exemplars:
                            print(str(i))

                        json_sj = JSONSaver(sj_api.vacancies)
                        json_sj.add_vacancies()
                        quit()
                    except KeyError:
                        print('Введите правильное имя города на руском языке!')
                        continue
                        # При перехвате исключения возвращаемся к началу цикла,
                        # для повторного введения параметров поиска
            if action == '4':  # Если выбрали получить топ вакансий по з/п в городе
                while True:
                    try:
                        search_options = user_action_4()  # Записываем в переменную параметры поиска
                        sj_api = SuperJobAPI(salary=search_options[0], city=search_options[1])
                        # Инициализируем экземпляр класса с параметрами поиска
                        sj_api.get_vacancies()
                        sj_vacancy = Vacancy
                        list_exemplars = sj_vacancy.create_exemplars_for_sj(sj_api.vacancies)

                        for i in list_exemplars:
                            print(str(i))

                        json_sj = JSONSaver(sj_api.vacancies)
                        json_sj.add_vacancies()
                        quit()
                    except KeyError:
                        print('Введите правильное имя города на руском языке!')
                        continue
            elif action == '0':  # Выходим из программы
                quit()
            else:
                print("Пожалуйта, введите корректное значение")
                continue
                # При вводе не верное команды выводим соответствующее сообщению пользователю
                # и возвращаемся к началу цикла
    elif action == '0':
        quit()
    else:
        print("Пожалуйта, введите корректное значение")
        continue
