# {"cook_book ": [{'name': "...."}, {}, {}]}
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
    print(cook_book)
