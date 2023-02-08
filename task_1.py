# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

season_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето',
               'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
i = int(input("Введите номер месяца: "))
if i <= 12:
    print(f'Результат через список: ' + season_list[i - 1])
elif i > 12:
    print('В году только 12 месяцев')

season_dict = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна',
               '5': 'Весна', '6': 'Лето','7': 'Лето','8': 'Лето','9': 'Осень',
               '10': 'Осень','11': 'Осень', '12': 'Зима'}
i = input("Введите номер месяца: ")
print(f'Результат через словарь: ' + season_dict[i])
