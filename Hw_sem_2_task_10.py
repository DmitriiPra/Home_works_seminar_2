'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
'''
import random

mount = int(input('введите количество монет: '))
coins = []
for i in range(mount):
    coins.append(random.randint(0, 1))
print(coins)

avers, revers = 0, 0
for i in range(mount):
    if coins[i] == 0:
        avers += 1
    else:
        revers += 1
if avers < revers:
    print (f'нужно перевернуть {avers} монеты')
else:
    print (f'нужно перевернуть {revers} монеты')