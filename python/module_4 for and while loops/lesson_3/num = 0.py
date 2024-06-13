num1 = 1
num2 = 0

n = int(input())
for i in range(1, n + 1):
    num3 = num1
    num1 = num3 + num2
    num2 = num3
    print(num3, end=' ')

"""
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
"""