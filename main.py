# spisok = [1, 1, 2, 0, -1, 3, 4, 4, 6, 6]
# # list = []
# # for i in range(0, len(spisok)):
# #     if spisok[i] not in list:
# #         list.append(spisok[i])
# # print(len(list))

# list = set(spisok)
# print(len(list))

spisok = [1, 2, 3, 4, 5, 6, 7]
k = int(input('Введите число сдвига: '))
temp = None
for i in range(0, k):
    for j in range(len(spisok)-1, 0, -1):
        temp = spisok[j]
        spisok[j] = spisok[j-1]
        spisok[j-1]= temp
print(spisok)

listOfDictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
list = []
for i in listOfDictionary:
    
    for j in i.values():
        
        if j not in list:
            list.append(j)
print(list)
