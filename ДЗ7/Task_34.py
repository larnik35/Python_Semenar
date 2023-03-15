
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
# 

verse = input(' Введите стих Винни-Пуха ')
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
list_1 = verse.split()
itog = list()
for item in list_1:
    n = 0
    for letter in item:
        if letter in volwes:
            n += 1
    itog.append(n)
if len(set(itog)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')