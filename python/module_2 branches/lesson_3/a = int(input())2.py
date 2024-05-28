a = int(input())
if a == 0:
    print('зеленый')
elif ((0 < a <= 10) and a % 2 == 0) or ((10 < a <= 18) and a % 2 != 0) or ((18 < a <= 28) and a % 2 == 0) or ((28 < a <= 36) and a % 2 != 0):
    print('черный')
elif ((0 < a <= 10) and a % 2 != 0) or ((10 < a <= 18) and a % 2 == 0) or ((18 < a <= 28) and a % 2 != 0) or ((28 < a <= 36) and a % 2 == 0):
    print('красный')
else:
    print('ошибка ввода')