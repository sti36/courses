repeat_input = int(input())  
mas = []

for _ in range(repeat_input):
    line = input()
    mas.append(line)

search = input()

for letters in mas:
    if search.lower() in letters.lower():
        print(letters)

"""
На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. 
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
"""