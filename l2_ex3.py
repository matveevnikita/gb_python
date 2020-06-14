# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('enter month number: ')
month = int(input())
s_list = ['winter', 'spring','summer','autumn']

if month < 12:
    print('month', month, 'is in ', s_list[month // 3])
if month == 12:
        print('month', month, 'is in ', s_list[0])

s_dict = {0:'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}

if month < 12:
    print('month', month, 'is in ', s_dict.get(month // 3))
if month == 12:
        print('month', month, 'is in ', s_dict.get(0))