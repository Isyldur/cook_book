import os
from pprint import pprint

# Первая задача

def read_cook_book(cook_book_file):
    with open(cook_book_file) as book:
        cook_book = {}
        for recipe in book:
            cook_book[recipe.replace('\n', '')] = []
            for i in range(int(book.readline())):
                line_list = book.readline().split('|')
                cook_book[recipe.replace('\n', '')].append(
                    {'ingredient_name': line_list[0].replace('\n', ''), 'quantity': int(line_list[1]),
                     'measure': line_list[2].replace('\n', '')})
            book.readline()
        return cook_book
pprint(read_cook_book('file.txt'))

# Вторая задача

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book('file.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity']
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity * person_count
                else:
                    shop_list[name] = {'measure': measure, 'quantity': (quantity * person_count)}
        else:
            return "There's no such dish in our menu!"
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 7))
# Третья задача

def compose(dir_path):
    try:
        files_list = os.listdir(dir_path)
        os.chdir(dir_path)
        data_list = []
        data_dict = {}

        def create_composed_file(filename):
            if filename not in files_list:
                with open(filename, 'w', encoding='utf-8') as file:
                    for data in sorted(data_list):
                        result = data_dict[tuple(data)] + '\n' + str(len(data)) + '\n'
                        for i in data:
                            result += i
                        file.write(result+'\n')
            else:
                create_composed_file('new_' + filename)

        for file in files_list:
            with open(file) as filedata:
                ddata = filedata.readlines()
                data_list.append(ddata)
                data_dict[tuple(ddata)] = file
        create_composed_file('composed_file.txt')

    except Exception as err:
        print("Ошибка", err)


compose('txtfiles')
