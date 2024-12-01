#Выполнение задания. Вариант №14

'''
Дано число B (> 0) и набор из десяти чисел. 
Вывести минимальный из тех элементов набора, которые больше B, а также его номер. 
Если чисел, больших B, в наборе нет, то дважды вывести 0.

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''

numbers = [int(a) for a in input().split()]
B = int(input())

min_value = float('inf')
min_index = -1

for index, number in enumerate(numbers):
    if number > B:
        if number < min_value:
            min_value = number
            min_index = index

if min_index == -1:
    print("00")
else:
    min_value = int(min_value)
    print(f"Минимальное число, которое больше {B}: {min_value}, номер: {min_index + 1}")