num = int(input())
digit4 = num % 10
digit3 = (num % 100) // 10
digit2 = (num % 1000) // 100
digit1 = (num % 10000) // 1000
if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')

"""Напишите программу, которая проверяет, 
что для заданного четырехзначного числа выполняется следующее соотношение: 
сумма первой и последней цифр равна разности второй и третьей цифр."""