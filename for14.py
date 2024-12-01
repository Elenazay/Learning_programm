#Выполнение задания. Вариант №14
'''
Дано целое число N (> 0). Найти квадрат данного числа, используя для его вычисления следующую формулу:

N2 = 1 + 3 + 5 + … + (2·N − 1).

После добавления к сумме каждого слагаемого выводить текущее значение суммы 
(в результате будут выведены квадраты всех целых чисел от 1 до N).

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''
n = int(input())
s = 0
for i in range(1, n+1):
    s += 2 * i - 1
    print(s)