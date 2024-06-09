city1, city2, city3 = input(), input(), input()
length_city1 = len(city1)
length_city2 = len(city2)
length_city3 = len(city3)
if length_city1 < length_city2 < length_city3:
    print(city1, city3, sep='\n')
elif length_city1 < length_city3 < length_city2:
    print(city1, city2, sep='\n')
elif length_city2 < length_city1 < length_city3:
    print(city2, city3, sep='\n')
elif length_city2 < length_city3 < length_city1:
    print(city2, city1, sep='\n')
elif length_city3 < length_city2 < length_city1:
    print(city3, city1, sep='\n')
else:
    print(city3, city2, sep='\n')

"""
Даны названия трёх городов. Напишите программу, которая определяет самое короткое и 
самое длинное название города.
"""