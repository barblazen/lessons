#Пользователь вводит число N. Напишите программу, которая выводит все простые числа до N включительно
# (простое число делится только на 1 и само на себя).
# number = int(input("Enter number N : "))
# for i in range(number+1):
#     if  i !=0 and (i % i == 0) and (i % 1 == 0) :
#         print("The number is simple")
#         print(i)




import math

# Оптимизированная функция для проверки, является ли число простым
def IsPrime(n):
    if n < 2:  # Числа меньше 2 не являются простыми
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

# Основная программа
number = int(input("Enter number N: "))

print(f"Prime numbers up to {number}:")
for i in range(2, number + 1):
    if IsPrime(i):
        print(i)
