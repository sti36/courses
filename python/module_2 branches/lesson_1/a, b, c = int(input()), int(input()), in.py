a, b, c = int(input()), int(input()), int(input())
if a >= 0:
    sum = a
else:
    sum = 0
if b >= 0:
    sum = sum + b
else:
    sum = sum + 0
if c >= 0:
    sum = sum + c
else:
    sum = sum + 0
print(sum)    

"""Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел."""