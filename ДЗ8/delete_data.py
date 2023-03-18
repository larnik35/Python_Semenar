def find_2(text): # поиск и изменения данных по фамилии
    #print('\n'*100)
    with open('file.txt', 'r', encoding="utf-8") as data:
        lines = data.readlines()
        index = int(len(lines))
        for i in range(index - 2):
            if  text in  lines[i]:
                lines.pop(i) 
                print(lines) 
                print('\n')
        with open('file.txt', 'w', encoding="utf-8") as data:
            data.writelines(lines)
        return
    print("Не найден!")
    data.close()
    print('\n')
