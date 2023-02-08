# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#

my_list = []
while input('Добавить товар? (да/нет) ') == "да":
    count = int(input('Введите номер товара '))
    base_dict = {}
    while input("Хотите добавить параменты товара (да/нет)") == "да":
        base_dict['Название'] = input('Введите название товара ')
        base_dict['Цена'] = int(input('Введите цену товара '))
        base_dict['Количество'] = int(input('Введите количество товара '))
        base_dict['Ед'] = input('Введите ед измерения кол-ва товара ')
        print(count, base_dict)
        break
    my_list.append(tuple([ count, base_dict]))
print(my_list)




