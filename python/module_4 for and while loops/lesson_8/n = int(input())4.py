n = int(input())
while n > 9:
    total = 0
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n //= 10
    n = total
print(n)

"""
На вход программе подается натуральное число n. Напишите программу, 
которая находит цифровой корень данного числа. Цифровой корень числа n получается следующим образом: 
если сложить все цифры этого числа, затем все цифры найденной суммы и повторять этот процесс до тех пор, 
пока в результате не будет получено однозначное число (цифра), которое и называется цифровым корнем 
первоначального числа n.
"""