#Подсчет букв и цифр
#Пользователь вводит строку. Напишите программу, которая подсчитает и выведет количество букв и цифр в этой строке.
# Например, для строки "Привет123" результатом должно быть "Букв: 6, Цифр: 3".
string = input("Enter a string of letters and numbers : ")
letters = sum(1 for char in string if char.isalpha())
digits = sum(1 for char in string if char.isdigit())
# digits = 0
# for char in string:
#     if char.isdigit():
#         digits+= 1
print(f"Букв : {letters}, Цифр : {digits}")