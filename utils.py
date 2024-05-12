import time

from src import Wallet

user = Wallet()


def add_a_note():
    date = input('Введите дату в формате dd.mm.yyyy:\n')
    while True:
        try:
            time.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print('Неверный формат!')
            date = input('Введите дату в формате dd.mm.yyyy:\n')

    category = input('Категория: 1-покупка/2-продажа\n')
    while category != '1' and category != '2':
        if category != '1' and category != '2':
            print('нет такой категории')
            category = input('Категория: 1-покупка/2-продажа\n')
    if category == '1':
        category = 'покупка'
    else:
        category = 'продажа'

    while True:
        try:
            amount = int(input('Сумма операции\n'))
            break
        except ValueError:
            print('Поле поддерживает тлько числа')

    description = input('Описание\n')
    try:
        user.add_data(date, category, amount, description)
        print('Запись произведена')
    except Exception:  # Добраьотать обработку ошибок
        print('что то пошло не так!')


def search_in_note():
    try:
        search = int(input('Как ищем? 1-по категории,2-по дате,3-по сумме\n'))
        if search == 1:
            search_value = ['покупка', 'продажа']
            search = int(input('Категория: 1-покупка/2-продажа\n'))
            n = user.card_search('Категория', search_value[search - 1])

            for i in n:
                print(i)
        elif search == 2:
            while True:
                search = input('Введите дату в формате dd.mm.yyyy:\n')
                try:
                    time.strptime(search, '%d.%m.%Y')
                    break
                except ValueError:
                    print('Неверный формат!')
            print(user.card_search('Дата', search))

        elif search == 3:
            search = int(input('Операции по какой сумме ищем?\n'))
            user.card_search('Сумма', search)
        else:
            print('Такого нет в меню')
    except ValueError:
        print('Ошибка ввода, проверте поле ввода')


def editing_post_in_note():
    editing = int(input('1-Вывести весь список/удаление, 2-Искать для изменения\n'))
    if editing == 1:
        # Выводит весь список
        total = 1
        n = user.all_list()
        for item in n:
            print(total, item)
            total += 1
        operation = int(input('Действие над элементом: 1-Удалить, 0-выйти\n'))
        if operation == 1:

            question = int(input('Номер записи для удаления?\n'))
            try:
                user.editing_post(True, question - 1)
                time.sleep(1)
                print('Запись успешно удалена')
            except Exception:
                print('Что то пошло не так')
        elif operation == 0:
            pass
        else:
            print('Такого нет в меню')
    elif editing == 2:
        # вызов функции поиска и запрос на изменение
        try:
            search = int(input('Как ищем? 1-по категории,2-по дате,3-по сумме\n'))
            if search == 1:
                search_value_in = ['покупка', 'продажа']
                search = int(input('Категория: 1-покупка/2-продажа\n'))
                if search == 1 or search == 2:
                    n = user.card_search('Категория', search_value_in[search - 1])
                    total = 1
                    if len(n) == 0:
                        print('У вас нет записей с такой категорией')
                    else:
                        for i in n:
                            print(total, i)
                            total += 1
                        search1 = int(input('Укажите номер редактируемой операции:\n'))
                        changes = int(input('Что изменить? 1-Дата, 2-категория,3-сумма,4-Описание\n'))
                        search_value = ['Дата', 'Категория', 'Сумма', 'Описание']
                        # value = input('На что меняем?\n')
                        try:
                            user.editing_post(False, search1, 'Категория', search_value[changes - 1],
                                              search_value_in[search - 1])
                            print('Изменения приняты')
                        except Exception:
                            print('Не вышло')

                else:
                    print('Нет такой ктаегории')

            elif search == 2:
                while True:
                    search = input('Введите дату в формате dd.mm.yyyy:\n')
                    try:
                        time.strptime(search, '%d.%m.%Y')
                        break
                    except ValueError:
                        print('Неверный формат!')

                n = (user.card_search('Дата', search))
                if len(n) == 0:
                    print('Нет данных с такой датой')
                else:
                    total = 1
                    for i in n:
                        print(total, i)
                        total += 1
                    search1 = int(input('Укажите номер редактируемой операции:\n'))
                    if 0 < search1 < total:

                        changes = int(input('Что изменить? 1-Дата, 2-категория,3-сумма,4-Описание\n'))
                        search_value = ['Дата', 'Категория', 'Сумма', 'Описание']
                        if 0 < changes <= 4:
                            value = input('На что меняем?\n')
                            try:
                                user.editing_post(False, search1, 'Дата', search_value[changes - 1], search, value)
                                print('Изменения приняты')
                            except Exception:
                                print('Не вышло')
                        else:
                            print('Нет такого выбора')
                    else:
                        print('Нет данных с таким номером')

            elif search == 3:
                search = int(input('Операции по какой сумме ищем?\n'))
                n = user.card_search('Сумма', search)
                if len(n) == 0:
                    print('Нет данных с такой суммой')
                else:
                    total = 1
                    for i in n:
                        print(total, i)
                        total += 1
                    search1 = int(input('Укажите номер редактируемой операции:\n'))
                    if 0 < search1 < total:
                        changes = int(input('Что изменить? 1-Дата, 2-категория,3-сумма,4-Описание\n'))
                        if 0 < changes <= 4:
                            search_value = ['Дата', 'Категория', 'Сумма', 'Описание']
                            value = input('На что меняем?\n')
                            try:
                                user.editing_post(False, search1, 'Сумма', search_value[changes - 1], search, value)
                                print('Изменения приняты')
                            except Exception:
                                print('Не вышло')
                        else:
                            print('Нет такого выбора')
                    else:
                        print('Нет данных с таким номером')
        except ValueError:
            print('Ошибка ввода, проверте поле ввода')
    else:
        print('Такого в меню нет')