n = int(input())
one_lowers_letters_ascii = 97
s = ''

for i in range(n):
    s += chr(one_lowers_letters_ascii + i)
    
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