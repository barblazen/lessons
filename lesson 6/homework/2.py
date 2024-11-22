#Пользователь вводит число N. Напишите программу, которая выводит все простые числа до N включительно
# (простое число делится только на 1 и само на себя).
number = int(input("Enter number N : "))
for i in range(number+1):
    if  i !=0 and (i % i == 0) and (i % 1 == 0) :
        print("The number is simple")
        print(i)

