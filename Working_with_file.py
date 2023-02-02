# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке.



with open("trimushketera.txt", "r", encoding="utf8") as file:
    data = file.read()
symbols = """!"#$%&?:;><=()*-+,./0123456789XIV"""
for el in data:
    if el in symbols:
        data = data.replace(el, " ")

list_data = data.split()
count_words = str(len(list_data))
unic_set = set()
for el in list_data:
    unic_set.add(el.lower())
unic_list = list(unic_set)
count_unic_words = str(len(unic_list))
unic_list.sort()


with open("solutinTriMus.txt","w",encoding="utf8") as work:
    work.write("There are  " + count_words + " words\n")
    work.write("There are  " + count_unic_words + " unique words\n\n\n")
    work.write("The list of unique words:\n\n")
    for el in unic_list:
        work.write(el+"\n")





