import json
import os
import datetime
import time
from json import JSONDecodeError


# current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
# print(current_time)


class Wallet:
    def __init__(self):
        self.data_first = []

    def add_data(self, date, category, amount, description):
        '''Возможность добавления новой записи о доходе или расходе'''
        if os.stat("wallet.json").st_size != 0 and os.path.exists("wallet.json"):
            with open('wallet.json', encoding='utf8') as f:
                data = json.load(f)
                # data["values"] += list(a_dict)
                data.append({
                    'Дата': date,
                    # 'Время': self.current_time,
                    'Категория': category,
                    'Сумма': amount,
                    'Описание': description,
                })
            with open('wallet.json', 'w', encoding='utf8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            with open('wallet.json', 'w', encoding='utf8') as file:
                self.data_first.append({
                    'Дата': date,
                    # 'Время': self.current_time,
                    'Категория': category,
                    'Сумма': amount,
                    'Описание': description,
                })
                json.dump(self.data_first, file, indent=2, ensure_ascii=False)

    def card_balance(self):
        '''Показать текущий баланс, а также отдельно доходы и расходы'''
        try:
            with open('wallet.json') as f:
                res = 0
                buying, selling = 0, 0
                result = []
                data = json.load(f)
                if len(data) > 0:
                    for i in data:
                        if i['Категория'] == "продажа":
                            res += int(i['Сумма'])
                            buying += int(i['Сумма'])
                        else:
                            res -= int(i['Сумма'])
                            selling += int(i['Сумма'])
                    result = [res, buying, selling]
                else:
                    print('Пока у вас нет записей')
                    rez = 'Ваш баланс: 0 руб'
                    return rez
                return result
        except JSONDecodeError:
            print('Пока у вас нет записей')
            rez = 'Ваш баланс: 0 руб'
            return rez

    def card_search(self, field, search_value):
        '''Поиск по записям: Поиск записей по категории, дате или сумме'''
        with open('wallet.json') as f:
            result = []
            data = json.load(f)
            for i in data:
                if i[field] == search_value:
                    result.append(i)
            return result

    def editing_post(self, flag, elem, search_category=None, category=None, old_value=None, value=None):
        '''Редактирование записи: Изменение существующих записей о доходах и расходах.'''

        if flag:
            with open('wallet.json') as f:
                data = json.load(f)
                # for item in data:
                del data[elem - 1]
            # print(data[elem])
        else:
            with open('wallet.json') as f:
                data = json.load(f)
                a = []
                v = 0
                for item in data:
                    if item[search_category] == old_value:
                        a.append(v)
                    v += 1
                if category == 'Дата':
                    try:
                        time.strptime(value, '%d.%m.%Y')
                        data[a[elem - 1]][category] = value
                    except ValueError:
                        print('Неверный формат!')
                elif category == 'Сумма':
                    try:
                        value = int(value)
                        data[a[elem - 1]][category] = value
                    except ValueError:
                        print('Неверный формат!')
                elif category == 'Категория':
                    li = ['покупка', 'продажа']
                    if data[a[elem - 1]][category] == 'покупка':
                        data[a[elem - 1]][category] = 'продажа'
                    else:
                        data[a[elem - 1]][category] = 'покупка'
                    # try:
                    #     if value in li:
                    #         data[a[elem - 1]][category] = value
                    #     else:
                    #         raise Exception("File is empty")
                    # except Exception:
                    #     print('Неверный формат!')
                else:
                    data[a[elem - 1]][category] = value
        with open('wallet.json', 'w', encoding='utf8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def all_list(self):
        with open('wallet.json') as f:
            try:
                data = json.load(f)
                return data
            except JSONDecodeError:
                return None

