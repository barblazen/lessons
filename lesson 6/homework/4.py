#Таблица умножения
# Напишите программу, которая выводит таблицу умножения для чисел от 1 до 10.
# Каждое число должно быть умножено на числа от 1 до 10.
# example    число 10 : 10, 20, 30 ...
# Генерация таблицы умножения
for i in range(1, 11):  #числа от 1 до 10
    for j in range(1, 11):  #умножение на числа от 1 до 10
        print(f"{i * j:4}", end=" ")  #вывод результата с выравниванием
    print()  #переход на новую строку после каждой строки таблицы
