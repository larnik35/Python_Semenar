from show_data import *
from find_data import *
from replacement_data import *
from delete_data import *

def menuHello():
    print('\n')
    print("1.Добавить ")
    print("2.Вывести всех ")
    print("3.Поиск по фамилии ")
    print('4.Изменение данных ')
    print('5.Удаление данных ')
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        printAll()
        return True
    if userInput == 3:
        find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        find_1(input("Введите фамилию данные о которой хотите изменить "))
        return True
    if userInput == 5:
        find_2(input("Введите фамилию данные о которой хотите удалить  "))
        return True
    if userInput == 6:
        return False

def addData():
    data = open('file.txt', 'a', encoding="utf-8" )
    print('\n'*100) 
    first_name = input("Введите имя: ")
    mid_name = input("Введите отчество: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    item = [first_name, mid_name, second_name,  number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*100)

