#Выполнение задания. Вариант №14

'''
Элементы равностороннего треугольника пронумерованы следующим образом: 
1 — сторона a, 2 — радиус R1 вписанной окружности (R1 = a·(3)1/2/6), 
3 — радиус R2 описанной окружности (R2 = 2·R1), 4 — площадь S = a2·(3)1/2/4. 
Дан номер одного из этих элементов и его значение. 
Вывести значения остальных элементов данного треугольника (в том же порядке).

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''

import math
n = int(input())
zn = int(input())

a = 1
r1 = a * (math.sqrt(3) / 6)
r2 = r1 * 2
S = (a * a * math.sqrt(3)) / 4

if n == 1:
    a = zn
    a = 1
    r1 = a * (math.sqrt(3) / 6)
    r2 = r1 * 2
    S = (a * a * math.sqrt(3)) / 4
elif n == 2:
    r1 = zn
    a = 6 * r1 / math.sqrt(3)
    r2 = r1 * 2
    S = (a * a * math.sqrt(3)) / 4
elif n == 3:
    r2 = zn
    r1 = r2 / 2
    a = 6 * r1 / math.sqrt(3)
    S = (a * a * math.sqrt(3)) / 4
else:
    S = zn
    a = math.sqrt(S * 4 / math.sqrt(3))
    r1 = a * (math.sqrt(3) / 6)
    r2 = r1 * 2

print(f'Сторона: {a}, R1: {r1}, R2: {r2}, Площадь: {S}.')