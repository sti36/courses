number = int(input())
mas = []
sum_mas = []

for i in range(number):
    digit = int(input())
    mas.append(digit)

for j in range(len(mas) - 1):
    sum_mas.append(mas[j] + mas[j + 1])

print(sum_mas)

"""
На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел. Напишите программу, 
которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
"""