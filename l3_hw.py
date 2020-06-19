# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа
# запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return ("zero divison")

print(division(3,4))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def one_string (name, surname, birth, city, email, phone):
    print(name, surname, birth, city, email, phone)

one_string (name = 'Nikita', surname = 'Matveev', birth = '28.04.1990',
            email = 'matveevnikita@yahoo.com', phone = '### #### ###', city = 'Moscow')

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = list()
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list.sort()
    return(my_list[1], my_list[2])

print(my_func(5,2,6))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    print ('operator **:', x ** y)
    z = x
    for i in range(1, -y+2):
        x = x / z
    print('loop:', x)

my_func(9,-3)

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
# выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

my_sum = 0
my_break = False
while True:
    str = input('enter numbers divided by space, enter q to quit: ')
    my_list = str.split(' ')
    for i in my_list:
        if i.isnumeric():
            my_sum += int(i)
        elif i.lower() == 'q':
            my_break = True
        else:
            print ('wrong symbol, try again')
    if my_break == True:
        break
    else:
        print('sum of entered numbers is: ', my_sum)
print('sum of entered numbers is: ', my_sum)

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(func_word):
    return func_word.title()


my_word = 'text'
print(int_func(my_word))

my_str = 'hello world nikita'
my_words = my_str.split(' ')
print('initial string is: ', my_str)
print('new string is: ', end='')
for i in range(0, len(my_words)):
    print(int_func(my_words[i]), end=' ')