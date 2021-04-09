from pprint import pprint
import os

path = os.path.abspath('1.txt')


def cook_book_func(file_path):
    """
    Функция принимает на вход путь к файлу.
    :param file_path: Путь к файлу с рецептами блюд
    :return: Функция возвращает словарь с рецептами
    """
    cook_book = {}
    key_ = ['ingredient_name', 'quantity', 'measure']  # Список с названиями для ключей вложенных словарей с рецептом
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()  # Получение Первого и следующих названий блюд
            counter = int(f.readline().strip())  # Получение счетчика итераций по рецепту
            keys_ = []
            for _ in range(int(counter)):
                q = f.readline().strip().split(' | ')  # Разделение строки по символу | на список
                dish_dict = dict(zip(key_, q))
                keys_ += [dish_dict]
            cook_book[dish_name] = keys_
            f.readline().strip()
        # pprint(cook_book)
    return cook_book


pprint(cook_book_func(path))  # При использовании print выведется словарь с правильным порядком
print()
cook_book_list = ['Омлет', 'Фахитос', 'Запеченный картофель']


def get_shop_list_by_dishes(dish_list, person_count):
    """

    :param dish_list: Список с необходимыми блюдами
    :param person_count: Количество персон
    :return: Словарь со списком покупок
    """
    cook_book = cook_book_func(path)  # Вызов функции для формирования словаря с рецептакми
    shop_dict = {}
    for dish in dish_list:
        for ingredients in cook_book[dish]:
            new_shop_dict = ingredients  # Временный список с ингридиентами по названию блюд из списка
            new_shop_dict['quantity'] = int(new_shop_dict['quantity']) * person_count
            if new_shop_dict['ingredient_name'] not in shop_dict:  # Если в конечном словаре нет такого ингридиента то +
                shop_dict[new_shop_dict['ingredient_name']] = {'measure': new_shop_dict['measure'],
                                                               'quantity': new_shop_dict['quantity']}
            else:  # Если в конечном словаре уже есть такой ингридиент, то плюсуем количество покупок
                shop_dict[new_shop_dict['ingredient_name']] = \
                    {'measure': shop_dict[new_shop_dict['ingredient_name']]['measure'],
                     'quantity': shop_dict[new_shop_dict['ingredient_name']]['quantity'] + new_shop_dict['quantity']}

    pprint(shop_dict)


get_shop_list_by_dishes(cook_book_list, 2)
