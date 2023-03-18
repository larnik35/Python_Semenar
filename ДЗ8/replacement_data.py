def find_1(text): # поиск и изменения данных по фамилии
    #print('\n'*100)
    with open('file.txt', 'r', encoding="utf-8") as data:
        lines = data.readlines()
        
        for i in range(len(lines)):
            if  text in  lines[i]:
                 print(lines[i])
                 first_name = input("Введите имя: ")
                 mid_name = input("Введите отчество: ")
                 second_name = input("Введите фамилию: ")
                 number = input("Введите номер телефона: ")
                 item = [first_name, mid_name, second_name,  number]
                 s = ' '
                 m = str(s.join(item) + '\n')
                 lines[i]= m 
                 
                 with open('file.txt', 'w', encoding="utf-8") as data:
                    data.writelines(lines)
                 return
    print("Не найден!")
    data.close()
    print('\n')
