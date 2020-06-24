# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("ex1.txt","w") as f_obj:
    while True:
        my_str = input('enter the line: ')
        my_str += "\n"
        f_obj.write(my_str)
        if my_str == "\n":
            break

print('Done...')