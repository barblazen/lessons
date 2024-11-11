#Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
import random
while True:
    random_number = random.randint(1, 10)
    if random_number == 7:
        break
    print(random_number)