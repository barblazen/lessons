# Найти значение выражений:
# x = 17 / 2 * 3 + 2
# x = 2 + 17 / 2 * 3
# x = 19 % 4 + 15 / 2 * 3
# x = (15 + 6) - 10 * 4
# x = 17 / 2 % 2 * 3
#
# Расставить скобки так, чтобы значение выражений поменялось.
#
# #27.5 27.5 25.5 -19 1.5
# x = (17 / 2) * (3 + 2)
# a = (2 + 17) / 2 * 3
# b = (19 % 4) + (15 / (2 * 3))
# c = 15 + (6 - 10) * 4
# d = (17 / 2) % (2 * 3)
# print(x, a, b, c, d)


#Создать три переменные, содержащие возраст трех ваших друзей, в качестве имен переменных использовать имена друзей, найти сумму и вывести ее на экран.
# nika = 27
# elle = 31
# maks = 45
# summ = nika + elle + maks
# print(summ)
# sredne = summ / 3
# print(int(sredne))


#Найти в списке ниже количество не уникальных элементов:
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
#
# my_set = set(my_list)
# len_list = len(my_list)
#
# len_set = len(my_set)
# print(len_list, len_set)
# #8 5
# print(my_set)
# #{1, 2, 5.0, 'python3', 'python'}
# print(len_list - len_set)
# #3


#Взять список из предыдущей задачи, извлечь элементы со 2-го по 4-й включительно и вывести их в обратном порядке.
# slice = my_list[2:5]
# print("Slice of list is :" , slice)
# print(slice[::-1])
# print(list(reversed(slice)))

# №7
#Создать переменную содержащую сторону квадрата, создать новый список, в котором будут периметр квадрата, площадь квадрата и диагональ квадрата.
# import math
# side_of_square = 5
# perimeter = side_of_square * 4
# square = side_of_square ** 2
# dialonal = side_of_square * math.sqrt(2)