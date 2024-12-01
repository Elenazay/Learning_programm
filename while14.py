#Выполнение задания. Вариант №14

'''
Дано число A (> 1). 
Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + … + 1/K будет меньше A, и саму эту сумму

Решение. Зайцева Е.С., 309ИС-22, КМПО, 08.11.2024
'''

A = int(input())
K = 0
S = 0
while True:
    K += 1
    S += 1 / K
    if S >= A:
        K -= 1
        S -= 1 / K
        break

print(f"Наибольшее целое число K: {K}")
print(f"Сумма: {S}")