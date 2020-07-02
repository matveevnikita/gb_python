# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
from statistics import mean


my_list = []
for i in range(1, 100):
    my_list.append(random.randint(0, 1000))

with open('ex5.txt', 'w') as f_obj:
    for i in my_list:
        f_obj.write(str(i))
        f_obj.write(' ')
avg = 0

with open('ex5.txt', 'r') as f_obj:
    file_list = f_obj.read()
    for i in file_list.split(' '):
        if i != '':
            avg = avg + int(i)
    avg = avg / len(file_list.split(' '))

print(avg)




