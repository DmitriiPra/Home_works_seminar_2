"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.
"""
number = int(input("введите значение числа N: "))

if number <= 0:
    print("Введенo невернoе значение N")
else:
    k = 0
    print(number, "->", end=" ")
    while 2**k <= number:
        print(2**k, end=" ")
        k += 1
