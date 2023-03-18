def find(text):
    print('\n')
    data = open('file.txt', 'r', encoding="utf-8")
    lines = data.readlines()
    index = 0
    for line in range(len(lines)):
        if text in lines[line] :
            print(lines[line])
            index =+ 1
    
    data.close()
    if index == 0:
        print("Не найден!")
        print('\n')