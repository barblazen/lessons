# randomnaya genererac chisel
import random
random_number = random.randint(0, 5)
tries = 3
while tries != 0:
    your_number = int(input("Try to guess the number: "))
    if random_number == your_number:
        print("Числа равны")
        break
    elif random_number > your_number:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")