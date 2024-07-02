number = int(input())
mas = []

for i in range(number):
    digit = int(input())
    digit **= 3
    mas.append(digit)

print(mas)

"""
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.
"""