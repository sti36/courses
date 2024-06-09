m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m == n:
    print(m)
else:
    for i in range(m, n - 1, -1):
        print(i)

"""
Даны два целых числа m и n. Напишите программу, которая выводит все целые числа от m до n включительно 
в порядке возрастания, если m<n, или в порядке убывания в противном случае.
"""