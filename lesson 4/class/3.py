# randomnaya genererac chisel
import random
random_number = random.randint(0, 5)
your_number = int(input("Try to guess the number: "))
if random_number == your_number:
    print("Cool")
else:
    print("Bad")