# {"cook_book ": [{'name': "...."}, {}, {}]}
import collections
from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingr_count = int(file.readline())
        dishes = []
        for _ in range(ingr_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dishes.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = dishes


def get_shop_list_by_dishes(dishes, person_count):
    sl_shop_list_by_dishes = {}
    quantity = 0
    for dishe, ingredients in cook_book.items():
        for n in ingredients:
            if dishe in dishes:
                if list(n.items())[0][1] not in sl_shop_list_by_dishes:
                    quantity = int(list(n.items())[1][1]) * person_count
                    sl_shop_list_by_dishes[list(n.items())[0][1]] = {list(n.items())[2][0]: list(n.items())[2][1], list(n.items())[1][0]: quantity}
                else:
                    quantity += int(list(n.items())[1][1]) * person_count
                    sl_shop_list_by_dishes[list(n.items())[0][1]] = {list(n.items())[2][0]: list(n.items())[2][1],list(n.items())[1][0]: quantity}
    return sl_shop_list_by_dishes


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))


