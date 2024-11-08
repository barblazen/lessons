# 1
# x = 2
# y= 3
# print("Если умножить", x, "на", y, "получится", x * y)

# 2
# import math
# y = 4
# z = math.sqrt(y)
# print(z)

#3
# Запрашиваем у пользователя имя и фамилию
# first = input("Введите имя: ")
# last = input("Введите фамилию: ")
# # Конкатенируем строки
# both = last + ", " + first
#  # Отображаем результат
# print(both)

#4
# Запрашиваем имя пользователя
# first = input("Введите имя: ")
# middle = input("Введите отчество: ")
# last = input("Введите фамилию: ")
#  # Извлекаем первый символ из всех трех переменных и собираем их вместе
# initials = first[0] + middle[0] + last[0]
#  # Выводим инициалы
# print("Ваши инициалы:", initials)





# Упражнение 2. Приветствие
#  Напишите программу, запрашивающую у пользователя его имя.
#  В ответ на ввод на экране должно появиться приветствие с обращением по имени, введенному с клавиатуры ранее.
# name = input("Введите ваше имя: ")
# print("Здравствуйте,", name, "!")


# Упражнение 3. Площадь комнаты

# Напишите программу, запрашивающую у пользователя длину и ширину комнаты.
# После ввода значений должен быть произведен расчет площади комнаты и выведен на экран.
# Длина и ширина комнаты должны вводиться в формате числа с плавающей запятой.
# Дополните ввод и вывод единицами измерения, принятыми в вашей стране.  метры.

# length = float(input("Enter the length of your room (m) : "))
# width = float(input("Enter the width of your room (m) : "))
# square_of_room = length * width
# print("The square of room is: ", square_of_room, "square m")

#  Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину садового участка в футах.
# Выведите на экран площадь участка в акрах.
# Подсказка. В одном акре содержится 43 560 квадратных футов

length_of_plot = float(input("Enter the length of plot (f)  : "))
width_of_plot = float(input("Enter the width of plot (f)  : "))
square_of_plot_f = length_of_plot * width_of_plot
print("The square of plot in (square foot) is  : " ,  square_of_plot_f)
# in order to get the square of plot measured in acres we need to divide square of plot measured in square foot by 43 560
square_of_plot_acres = square_of_plot_f / 43560
print("The square of plot in acres is  : " ,  square_of_plot_acres)