# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("ex4_eng.txt") as eng_obj:
    with open("ex4_rus.txt", "w+") as rus_obj:
        for line in eng_obj:
            if line.split(' ')[0] == 'One':
                my_str = 'Один - 1\n'
            if line.split(' ')[0] == 'Two':
                my_str = 'Два - 2\n'
            if line.split(' ')[0] == 'Three':
                my_str = 'Три - 3\n'
            if line.split(' ')[0] == 'Four':
                my_str = 'Четыре - 4\n'
            rus_obj.write(my_str)
        rus_obj.seek(0)
        print(rus_obj.read())

