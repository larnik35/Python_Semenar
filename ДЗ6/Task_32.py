#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list_1 = list()
flag = bool(True)
n = 1
print('Введите элементы массива , для завершения введите 999')
print(flag)
while flag :
    n = int(input('Введите элемент массива '))
    if n == 999:
       flag = False 
    list_1.append(n)
list_1.pop()    
print(list_1)
min_Num = int(input('Введите минимальное значение '))
max_Num = int(input('Введите максимальное значение '))
for i in range(len(list_1)):
    if min_Num <= list_1[i] <= max_Num:
        print(f' {list_1[i]}')


