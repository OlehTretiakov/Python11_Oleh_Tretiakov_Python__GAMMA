import datetime

"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

print(new_sample1 := datetime.datetime.strptime(sample1,"%b %d %Y %I:%M%p"))
print(new_sample2:= datetime.datetime.strptime(sample2,"%H:%M %y/%m/%d") )
print(new_sample3:= datetime.datetime.strptime(sample3,"%A, %B %d, %Y").date())
print(new_sample4:= datetime.datetime.strptime(sample4,"%d.%m.%Y - %H:%M:%S"))

print("\n","-"*20,"\n")



# Write a program to print yesterdays, today and tomorrow dates
full_date = datetime.datetime.now()
ddelta = datetime.timedelta(days=1)
today = full_date.date()
yesterday = today-ddelta
tomorrow = today+ddelta
print(yesterday,today,tomorrow,sep="\n")

print("\n","-"*20,"\n")




# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
d = datetime.datetime.utcfromtimestamp(some_day).strftime('%d.%m.%Y')
print(d)

print("\n","-"*20,"\n")


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

# Решил двумя способами тест 1675080873
# Перекручено в решении потому что невнимательно прочитал задание
def get_to_past(n):
    today = datetime.datetime.fromtimestamp(n)
    two_weeks_ago = today - datetime.timedelta(weeks=2)
    return two_weeks_ago.timestamp()
n = float(input())
print(get_to_past(n))
def get_to_past(x):
    two_weeks_ago =datetime.datetime.fromtimestamp(x - (14*24*3600))
    return two_weeks_ago.timestamp()
x = float(input())
print(get_to_past(x))

