n = int(input())
total_three = 0
last_digit = n % 10
total_last_digit = 0
total_even_digit = 0
summ_five = 0
mult_seven = 1
total_null = 0
total_five = 0
while n != 0:
    digit = n % 10
    if digit == 3:
        total_three += 1 #количество цифр 3 в числе
    if digit == last_digit:
        total_last_digit += 1
    if digit % 2 == 0:
        total_even_digit += 1
    if digit > 5:
        summ_five += digit
    if digit > 7:
        mult_seven *= digit
    if digit == 0 or digit == 5:
        total_null += 1
    n //= 10
print(total_three, total_last_digit, total_even_digit, summ_five, mult_seven, total_null, sep='\n')