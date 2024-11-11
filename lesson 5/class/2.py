#Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
addition = int(input("Enter number n :"))
for number in range(1, 101):
    if number % addition == 0:
        print(number)
