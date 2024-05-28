a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    ab = b
else:
    ab = a
if c > d:
    cd = d
else:
    cd = c
if ab > cd:
    min = cd
else:
    min = ab
print(min)

#Напишите программу, которая определяет наименьшее из четырёх чисел.