s = input()
h_one = s.find('h')
h_two = s.rfind('h')
print(s[:h_one + 1] + s[h_two - 1:h_one:-1] + s[h_two:])

"""
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. 
Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, 
заключенную между первым и последним вхождением буквы «h».
"""