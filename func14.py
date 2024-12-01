
'''
Описать функцию DigitCount(K) целого типа, находящую количество цифр целого положительного числа K. 
Используя эту функцию, найти количество цифр для каждого из пяти данных целых положительных чисел.
'''
def DigitCount(K):
    c = 0 
    while K > 0:
        K //= 10
        c += 1
    return c

nums = []
for i in range(5):
    a = int(input())
    nums.append(a)

for K in nums:
 colvo = DigitCount(K)
 print(colvo)
