n = int(input())
last_digit = n % 10
flag = True
while n != 0:
    digit = n % 10
    if last_digit != digit:
        flag = False
    n = n // 10
if flag == True:
    print('YES')
else:
    print('NO')

#Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.