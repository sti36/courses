ONE_LOWERS_LETTERS_ASCII = 97

n = int(input())
s = ''

for i in range(n):
    s += chr(ONE_LOWERS_LETTERS_ASCII + i)
    
print(list(s))
'''
Второй вариант решения с выводом элементов списка по отдельности
list_letters_ascii = 122
one_lowers_letters_ascii = 96
for i in range(1, n + 1):
    if i < one_lowers_letters_ascii:
        line = one_lowers_letters_ascii + i
    print(list(chr(line)), end=' ')
'''