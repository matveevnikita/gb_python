# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

print('input time in seconds')
sec = input()
mnt = int(sec) // 60
hr = mnt // 60
mnt = mnt % 60
sec = int(sec) % 60
print('time in hh:mm:ss is:', hr, ':', mnt, ':', sec)
