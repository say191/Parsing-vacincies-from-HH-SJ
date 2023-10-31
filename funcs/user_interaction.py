def search_query(name_user):
    action = input(f"Здравствуйте, {name_user}!\n"
                   "Выберите с какой платформы вы хотите получить данные о вакансиях:\n"
                   "1 - HeadHunter\n"
                   "2 - SuperJob\n"
                   "0 - выход из программы\n")
    return action


def user_action():
    action = input("Выберите дальнейшие действия:\n"
                   "1 - поиск вакансий по ключевому слову\n"
                   "2 - поиск вакансии по ключевому слову и заработной плате\n"
                   "3 - поиск вакансии по ключевому слову и городу\n"
                   "4 - получить топ-N вакансий по зарабатной плате в выбранном городе\n"
                   "0 - выход из программы\n")
    return action


def user_action_1():
    key_word = input('Введите ключевое слово:\n')
    return key_word


def user_action_2():
    key_word = input('Введите ключевое слово:\n')
    salary = int(input('Введите зарплату:\n'))
    return [key_word, salary]


def user_action_3():
    key_word = input('Введите ключевое слово:\n')
    city = input('Введите город:\n').capitalize()
    return [key_word, city]


def user_action_4():
    salary = int(input('Введите зарплату:\n'))
    city = input('Введите город:\n').capitalize()
    return [salary, city]
