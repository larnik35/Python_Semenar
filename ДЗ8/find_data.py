def find(text):
    print('\n')
    data = open('file.txt', 'r', encoding="utf-8")
    lines = data.readlines()
    for line in range(len(lines)):
        if text in lines[line] :
            print(lines[line])

    data.close()
    return
    print("Не найден!")
    data.close()
    print('\n')
