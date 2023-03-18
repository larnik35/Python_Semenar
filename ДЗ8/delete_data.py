def find_2(text): # поиск и изменения данных по фамилии
    #print('\n'*100)
    with open('file.txt', 'r', encoding="utf-8") as data:
        lines = data.readlines()
        
        for i in range(len(lines)):
            if  text in  lines[i]:
                 lines.pop(i) 
                 
                 with open('file.txt', 'w', encoding="utf-8") as data:
                    data.writelines(lines)
                 return
    print("Не найден!")
    data.close()
    print('\n')
