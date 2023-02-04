import csv

with open("2019.csv","r",encoding="utf8") as file:
    data = list(csv.reader(file))
    menu = data[0]
    data = data[1:]
    new_menu = menu[3:]
    menu_dict = {k:new_menu.index(k)+1 for k in new_menu }

print("Hello, select the indicator of interest!\n\n")
for k,v in menu_dict.items():
    print(f"If you need a <<{k}>> index,\nplease enter the {v}")
print()
ind = int(input("Your number: "))
print()
print("Please select the number of countries in the ranking(from 1 to 156)")
amount = int(input("Your number: "))
print()
if 0<ind<7 and 0<amount<157:
    my_dict = {}
    for el in data:
        my_dict[el[menu.index(menu[ind + 2])]] = el[1]
    print(f"{new_menu[ind-1]} first {amount}:\n")
    c = 1
    for k,v in sorted(my_dict.items(),reverse=True):
        print(f"{c}. {v} - {k}")
        c+=1
        if c==amount+1:
            break
else:
    print("Input Error")


