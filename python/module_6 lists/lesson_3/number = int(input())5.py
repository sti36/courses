number = int(input())  
mas = []

for i in range(number):
    digit = input()
    mas.append(digit)

index = int(input())
result = ''

for digit in mas:
    if len(digit) >= index:
        result += digit[index - 1]

print(result)

"""
На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
"""