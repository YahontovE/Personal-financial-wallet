import time

from src import Wallet
from utils import add_a_note, search_in_note, editing_post_in_note

'''Необходимо доделать функционал'''


# 3. Оформить readme file и выложить проект на Git


def main():
    user = Wallet()
    if not user.all_list():
        option = int(input('У вас пока нет записей,создать? 1-ДА, 2-НЕТ \n'))
        if option == 1:
            add_a_note()
            print('Выбирите интересующую вас категорию из меню:\n'
                  '1. Вывод баланса.\n'
                  '2. Добавление записи.\n'
                  '3. Редактирование записи.\n'
                  '4. Поиск по записям.\n'
                  '0. Завершить')
            choice = input()
            while choice != 0:

                # user = Wallet()

                if choice == '1':
                    '''Выбор  вывести баланс'''
                    data = user.card_balance()
                    if 0 < len(data) < 4:
                        print('Ваш баланс:', data[0], 'руб\nВаши доходы', data[1], 'руб\nВаши расходы', data[2], 'руб')
                    else:
                        print(data)

                elif choice == '2':
                    '''Выбор  добавление записи'''
                    add_a_note()

                elif choice == '4':
                    '''Выбор  поиск по записям'''
                    search_in_note()

                elif choice == '3':
                    '''Выбор  редактирование записи'''
                    editing_post_in_note()

                elif choice == '0':
                    '''Выбор выйти из программы'''
                    break
                else:
                    print('Такого пункта нет в меню')

                time.sleep(1)
                print('\nВыбирите интересующую вас категорию из меню:\n'
                      '1. Вывод баланса.\n'
                      '2. Добавление записи.\n'
                      '3. Редактирование записи.\n'
                      '4. Поиск по записям.\n'
                      '0. Завершить')
                choice = input()
            time.sleep(1)
            print('Хорошего дня ')
        else:
            print('До новых встреч')


if __name__ == '__main__':
    main()
