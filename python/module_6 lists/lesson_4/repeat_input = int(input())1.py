repeat_input = int(input())
mas = []

for _ in range(repeat_input):
    line = input()
    if line not in mas:
        mas.append(line)

print(*mas, sep='\n')

"""
На вход программе подается натуральное число n, а затем n строк. 
Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
"""