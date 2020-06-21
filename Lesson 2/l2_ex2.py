# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('enter the first list elemenet:')
l = list(input())
while True:
    print('do you want input more (y/n)')
    a = input()
    if a == 'y':
        l.append(input())
    if a =='n':
        break
i = 0
print('your list is: ', l)
while i < len(l)-1:
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp
    i = i+2
print('the new list is: ', l)



