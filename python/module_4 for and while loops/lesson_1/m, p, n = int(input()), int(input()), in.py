m, p, n = int(input()), int(input()), int(input())
for i in range(n):
   print(i + 1, m * (1 + p / 100) ** i)

"""
На вход программе подается три натуральных числа m,p,n:
m: стартовое количество организмов;
p: среднесуточное увеличение в %;
n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно). 
Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.
"""