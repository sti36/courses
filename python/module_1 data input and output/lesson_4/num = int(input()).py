num = int(input())
digit1 = num % 10
digit2 = (num % 100) // 10
digit3 = num // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)

#Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трехзначного числа.