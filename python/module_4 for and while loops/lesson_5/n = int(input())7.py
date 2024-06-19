n = int(input())
a = 0
flag = True
while n != 0:
    digit = n % 10
    if digit >= a:
        a = digit
    else:
        flag = False
    n = n // 10
if flag == True:
    print('YES')
else:
    print('NO')