num = int(input())
digit4 = num % 10
digit3 = (num % 100) // 10
digit2 = (num % 1000) // 100
digit1 = (num % 10000) // 1000
print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)

#Напишите программу для нахождения цифр четырёхзначного числа.