# Найдите сумму цифр трехзначного числа.
# Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
'''
# Вариант 1
j = int(input('Введите число '))
n = j # Фиксирую число чтоб потом вывести в выводе 
sum = 0
while j > 0:
    i = j % 10
    sum = sum + i
    j = j//10
print(f'Сумма цифр числа {n} = {sum}')
'''
# Вариант 2
j = str(input('Введите число '))
n = j # Фиксирую число чтоб потом вывести в выводе 
sum = 0
for i in j:
    sum = sum + int(i)
print(f'Сумма цифр числа {n} = {sum}')