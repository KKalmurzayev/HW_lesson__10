print("*" * 10, "Задание №1 Реализуйте программу для отображения различных форматов даты и времени",  "*" *10)
'''1) текущая дата и время 
2) текущий год 
3) месяц года 
4) номер недели в году 
5) будний день недели 
6) день года
7) день месяца 
8) день недели'''

from datetime import datetime
date1 = datetime.now()

print(date1)
print(date1.year)
print(date1.month)
print(date1.strftime("%W"))
print(date1.strftime("%A"))
print(date1.strftime("%j"))
print(date1.strftime("%m"))
print(date1.strftime("%u"))
print()


from datetime import datetime

print("*" * 10, "Задание №2 Реализуйте программу, чтобы определить, является ли данный год високосным",  "*" *10)

date2 = datetime.now()
date21 = date2.year
if date21%4==0 and date21%100!=0 or date21%400==0:
    print("Текущий год високосный!")
else:
    print("Текущий год не високосный!")

print()

print("*" * 10, "Задание №3 Реализуйте программу, для преобразования строки в дату и время.",  "*" *10)

import datetime

date_str = '01 january 2014 14:43'
date_obj = datetime.datetime.strptime(date_str, '%d %B %Y %H:%M')

print('Date input:', date_str)
print('Date output:', date_obj.date(), date_obj.time())

print()



print("*" * 10, "Задание №4 Напишите программу на Python, чтобы узнать текущее время в Python",  "*" *10) 
from datetime import datetime

date4 = datetime.now()
print(date4.time())
