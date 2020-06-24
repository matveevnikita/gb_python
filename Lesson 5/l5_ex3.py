# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# cредней величины дохода сотрудников.

from statistics import mean

emp_dict = {}

with open("ex3.txt") as f_obj:
    for line in f_obj:
        name = line.split(' ')[0]
        if name not in emp_dict.keys():
            emp_dict[name] = []
        emp_dict[name].append(int(line.split(' ')[1]))

print('month salary is: ', emp_dict, '\n')

for key, value in emp_dict.items():
    avg = mean(value)
    emp_dict[key] = avg
    if avg < 20:
        print('employee with average salaray less than 20k: ', key, '\n')

print('average salary is:', emp_dict)