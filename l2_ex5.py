# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
# тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например,
# my_list = [7, 5, 3, 3, 2].

# my_list = [7, 5, 3, 3, 2]
# print('the rating is: ', my_list)
# print('enter new number: ')
# n = int(input())
# pos = 0
# if n < my_list[len(my_list)-1]:
#     my_list.append(n)
# else:
#     for i in my_list:
#         if n >= i:
#             my_list.insert(pos,n)
#             break
#         pos = pos + 1
# print('the new rating is: ', my_list)

# Task 5
my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(request) < int(number):
        continue
    my_list.insert(index, request)
    print(my_list)
    break
else:
    my_list.append(request)
    print(my_list)
