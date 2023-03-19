# {"cook_book ": [{'name': "...."}, {}, {}]}
# Задача №1
import os.path
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

# Задача №2
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

def merging_files(file_to_write, folder):
    listfiles = {}
    path = os.getcwd() + '\\' + folder
    for i in os.listdir(path):
        if i.endswith('.txt') and file_to_write != i:
            file_txt = path + '\\' + i
            listfiles[i] = count_rows(file_txt)
    listfiles = dict(sorted(listfiles.items(), key=lambda x: x[1][0]))
    file_to_write = os.getcwd() + '\\' + folder + '\\' + file_to_write
    open_file = open(file_to_write, 'a')
    for file, it in listfiles.items():
        count = 1
        for str in it[1]:
            open_file.write(f'строка № {count} в файле {file} : {str}')
            count += 1
        open_file.writelines('\n')
    open_file.close()
def count_rows(file):
    with open(file, 'r', encoding='utf8') as f:
        s = sum(1 for _ in f)
        f.seek(0)
        text = f.readlines()
        return s, text


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
# в параметрах: имя итогового файла, и имя папки с исходными файлами и результирующим
merging_files('rezult.txt', 'folder_files_txt')