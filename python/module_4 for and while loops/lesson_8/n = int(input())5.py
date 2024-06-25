n = int(input())
factorial = 1
sum_factorial = 0
for i in range(1, n + 1):
    factorial *= i
    sum_factorial += factorial
print(sum_factorial)

"""
Дано натуральное число n. Напишите программу, которая выводит значение суммы: 1!+2!+3!+…+n!
"""