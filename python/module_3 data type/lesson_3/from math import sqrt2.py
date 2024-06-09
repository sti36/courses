from math import sqrt

a, b = float(input()), float(input())

Sa = (a + b) / 2
Sg = sqrt(a * b)
SG = (2 * a * b) / (a + b)
Sk = sqrt((a ** 2 + b ** 2) / 2)

print(Sa, Sg, SG, Sk, sep='\n')

"""
В математике выделяют следующие средние значения:

среднее арифметическое чисел a и b
среднее геометрическое чисел a и b
среднее гармоническое чисел a и b
среднее квадратичное чисел a и b
"""