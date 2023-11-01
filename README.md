Данный проект предназначен для парсинга информации о вакансиях с таких платофрм, как HeadHunter и SuperJob
Структурно проект разделен на несколько частей:
1. Классы: HeadHunterAPI, SuperJobAPI, JSONaction, Vacancy
2. Функции исключительно для реализации консольного взаимодействия с пользователем
3. Главная программа

В этом проекте происходит запрос пользователя с какой платформы искать вакансии, и какие параметры поиска использовать.
Далее через api происходит сбор информации о ваканиях по выбранным критериям поиска.
Затем создаются экземпляры класса Vacancy и выводится на экран информация о вакансиях в удобном формате с помощью магического метода __str__
Далее всю собранную информацию записываем в файл в формате json с помощью класса Jsonactions и его методов