s = input()
total_one = 0
total_two = 0
for i in range(0, len(s)):
    if s[i] == '+':
        total_one += 1
    if s[i] == '*':
        total_two += 1
print('Символ + встречается', total_one, 'раз')
print('Символ * встречается', total_two, 'раз')

"""
На вход программе подается одна строка. Напишите программу, которая определяет, 
сколько раз в строке встречаются символы + и *.
"""