x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())
if ((1 <= x <= 8) and (1 <= y <= 8) and (1 <= x1 <= 8) and (1 <= y1 <= 8)) and ((-1 <= (x - x1) <= 1) and (-1 <= (y - y1) <= 1)):
    print('YES')
else:
    print('NO')

"""Даны две различные клетки шахматной доски. Напишите программу,  
которая определяет, может ли король попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести «YES», 
если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае."""