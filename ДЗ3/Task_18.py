# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите длинну масиива: '))
array = list()
print()
for i in range(n):
     k = int(input(f'Введите {i + 1}-й элемент массива '))
     array.append(k)
print(f'Введены массив {array} ')
print()
x = int(input('Введите число которое надо найти '))
diff = 0
min = 10000
index = 0
for i in array:
    diff = abs(i - x) # находим  авсалютную 1разницу элемента массива от загаданного
    if diff <= min:
        min = diff
        index = i
print(f'Число {x} ближе всего к {index}')
