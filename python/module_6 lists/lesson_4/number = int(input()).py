number = int(input())
digits = []
mas_function = []

for i in range(number):
    digit = int(input())
    digits.append(digit)
    func = digit ** 2 + 2 * digit + 1
    mas_function.append(func)

print(*digits, '', *mas_function, sep='\n')

"""
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого 
введенного числа x выводит значение функции f(x)=x2+2x+1, каждое на отдельной строке.
"""