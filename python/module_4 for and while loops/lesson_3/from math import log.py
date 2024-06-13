from math import log
total = 0
n = int(input())
for i in range(1, n):
    total = total + (1/(i + 1))
print(1 + total - log(n))

"""
На вход программе подается натуральное число n. 
Напишите программу, которая вычисляет значение выражения (1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
"""