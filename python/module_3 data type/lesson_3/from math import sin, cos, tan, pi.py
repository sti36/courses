from math import sin, cos, tan, pi

x = float(input())
r = x * pi / 180
s = sin(r) + cos(r) + tan(r) ** 2
print(s)

"""
Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + tan^2 x
по заданному числу градусов x.
"""