sum = 0
i = int(input())
while i >= 0:
    sum += i
    i = int(input())
print(sum)

"""
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. 
Признаком окончания последовательности является любое отрицательное число, 
при этом в саму последовательность оно не входит. Напишите программу, 
которая выводит сумму всех членов данной последовательности.
Число 0 не является признаком окончания последовательности.
"""