s = input()
t = s.find('f', s.find('f') + 1, len(s))
if s.count('f') == 0:
    print('-2')
elif s.count('f') == 1:
    print('-1')
else:
    print(t)

"""
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения 
буквы «f». Если буква «f» встречается только один раз, выведите число −1, а если не встречается ни разу, 
выведите число −2.
"""