""" 
Задумано два натуральных числа X и Y (X,Y≤1000), надо их отгадать. 
Для этого есть две подсказки: сумма этих чисел S и их произведение P.
Программы должны отгадать задуманные числа.
"""
summa_numbers_S = int(input("введите значение суммы чисел X + Y = "))
product_numbers_P = int(input("введите значение произведения чисел X * Y = "))

if summa_numbers_S <= 0 or product_numbers_P <= 0:
    print("Введены неверные значения")
else:
    first_term, second_term, res = 0, 0, 0
    for i in range(1, int(summa_numbers_S / 2)):
        first_term = i
        second_term = summa_numbers_S - first_term
        # print (first_term, second_term)
        if first_term * second_term == product_numbers_P:
            res = 1
            print(f"задуманные числа: {first_term} и {second_term}")
            break
    if res == 0:
        print("задачa не имеет решения")