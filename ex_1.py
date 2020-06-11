print('hello')
print('what is the day today (dd.mm.yyyy)?')
current_date = input()
q_days = int(current_date[0:2]) + (int(current_date[3:5]) - 3)*30
print('days on quarantine:', q_days)
print('when were you born?')
city = input()
print('in', city, '100 days in quarantine more')
