
# Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.


a = int(input())
b = int(input())
c = int(input())

if a >= b and b >= c:
    bol = a
    mal = c
elif a >= b and c <= b:
    bol = a
    mal = b
elif b >= a and a >= c:
    bol = b
    mal = c
elif b >= c and c >= a:
    bol = b
    mal = a
elif c >= a and a >= b:
    bol = c
    mal = b
else:
    bol = c
    mal = a

print(f'Наибольшее: {bol}, наименьшее: {mal}')