# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from statistics import mean
from json import dump

comp_dict = {}
avg_dict = {'average': 0}
avg = []

with open('ex7.txt') as f_obj:
    for line in f_obj:
        words = line.split(' ')
        name = words[0]
        revenue = int(words[2])
        costs = int(words[3])
        profit = revenue - costs
        comp_dict[name] = profit
        if profit > 0:
            avg.append(profit)
    avg_dict['average'] = mean(avg)
    my_list =[comp_dict, avg_dict]

with open('ex7_res.txt', 'w+') as res_obj:
    dump(my_list, res_obj)
    res_obj.seek(0)
    print(res_obj.read())




