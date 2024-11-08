# Упражнение 35. Чет или нечет?
# Напишите программу, запрашивающую у пользователя целое число и выводящую на экран информацию о том,
# является введенное число четным или нечетным.
your_number = int(input("Enter an integer : "))
if your_number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")