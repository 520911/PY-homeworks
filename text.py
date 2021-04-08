from pprint import pprint
import os

path = os.path.abspath('1.txt')


def cook_book_func(file_path):
    cook_book = {}
    key_ = ['ingredient_name', 'quantity', 'measure']
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            counter = int(f.readline().strip())
            keys_ = []
            for _ in range(int(counter)):
                q = f.readline().strip().split(' | ')
                dish_dict = dict(zip(key_, q))
                keys_ += [dish_dict]
            cook_book[dish_name] = keys_
            f.readline().strip()
        # pprint(cook_book)
    return cook_book


pprint(cook_book_func(path))
print()
cook_book_list = ['Омлет', 'Фахитос', 'Запеченный картофель']


def get_shop_list_by_dishes(dish_list, person_count):
    cook_book = cook_book_func(path)
    shop_dict = {}
    for dish in dish_list:
        for ingredients in cook_book[dish]:
            new_shop_dict = ingredients
            new_shop_dict['quantity'] = int(new_shop_dict['quantity']) * person_count
            if new_shop_dict['ingredient_name'] not in shop_dict:
                shop_dict[new_shop_dict['ingredient_name']] = {'measure': new_shop_dict['measure'],
                                                               'quantity': new_shop_dict['quantity']}
            else:
                shop_dict[new_shop_dict['ingredient_name']] = \
                    {'measure': shop_dict[new_shop_dict['ingredient_name']]['measure'],
                     'quantity': shop_dict[new_shop_dict['ingredient_name']]['quantity'] \
                                 + new_shop_dict['quantity']}

    pprint(shop_dict)


get_shop_list_by_dishes(cook_book_list, 2)
