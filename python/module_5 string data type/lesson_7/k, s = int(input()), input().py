n, s = int(input()), input()
lowers_simvols = 122
one_lowers_simvols = 97
lowers_simvols_position = 96
for i in range(0, len(s)):
    de_code = ord(s[i]) - n
    if de_code < one_lowers_simvols:
        de_code = lowers_simvols - (lowers_simvols_position - de_code)
    print(chr(de_code), end='')

"""
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует 
шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают 
все тонкости довоенного мира, поэтому ученые из НКР не могут понять, как именно нужно декодировать данные 
сообщения. Напишите программу для декодирования этого шифра.

Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать 
сообщение, а не закодировать.
"""