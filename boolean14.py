#Выполнение задания. Вариант №14

'''
Даны три целых числа: A, B, C. 
Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''
A, B, C = map(int, input('Введите 3 целых числа через пробел: ').split())

pr = A > 0 or B > 0 or C > 0
print(pr)