m, n = int(input()), int(input())
for i in range(m % 2 - 1 + m, n - 1, -2):
    print(i)

"""
Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные целые числа от 
m до n включительно в порядке убывания.
"""