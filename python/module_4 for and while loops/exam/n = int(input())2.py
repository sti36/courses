n = int(input())
one_digit = 0
two_digit = 0
three_digit = 0
while n != 0:
    three_digit = two_digit
    two_digit = one_digit
    one_digit = n % 10
    n //= 10
print(three_digit)