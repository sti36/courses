s = input()
n = int(s)
summ_digit = 0
while n != 0:
    digit = n % 10
    summ_digit += digit
    n //= 10
print(summ_digit)

"""
На вход программе подается одна строка состоящая из цифр. Напишите программу, 
которая считает сумму цифр данной строки.
"""