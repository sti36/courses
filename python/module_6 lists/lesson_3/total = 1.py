total = 1
one_lower_letter_ascii = 97
last_lower_letter_ascii = 122
mas = []

for i in range(one_lower_letter_ascii, last_lower_letter_ascii + 1): 
    one_lower_letter_ascii = chr(one_lower_letter_ascii) #перевод в систему char
    mas.append(one_lower_letter_ascii * total) #добавление записи в список
    one_lower_letter_ascii = ord(one_lower_letter_ascii) #перервод в систему ord
    one_lower_letter_ascii += 1 #переход на следующий символ
    total += 1
print(mas)

"""
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
"""