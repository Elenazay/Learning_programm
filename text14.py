#Выполнение задания. Вариант №14

'''
Дан непустой текстовый файл. Удалить из него последнюю строку.

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''
#in.txt - случайное имя файла взятое из примера из варианта 9

f = open('in.txt', 'r')
lines = f.readlines()
lines = lines[:-1]
f.close() 

f = open('in.txt', 'w')
f.writelines(lines)
f.close()
