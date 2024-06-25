s = input()
flag = True
for i in range(0, len(s)):
    if s[i] in '0123456789':
        flag = False
if flag == True:
    print('Цифр нет')
else:
    print('Цифра')