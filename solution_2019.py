import csv

with open("2019.csv","r",encoding="utf8") as file:
    data = list(csv.reader(file))
    menu = data[0]
    data = data[1:]


my_dict = {}
for el in data:
    my_dict[el[menu.index("Social support")]] = el[1]
print("Social support rating first ten:\n")
c = 1
for k,v in sorted(my_dict.items(),reverse=True):
    print(f"{c}. {v} - {k}")
    c+=1
    if c==11:
        break




