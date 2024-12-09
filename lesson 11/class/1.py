import functools
from functools import reduce
list_of_numbers = [i for i in range(1, 22) if i%2 ==0]
sum_of_numbers = reduce(lambda x, y: x+y)
# def square_of_numbers(list):
#     list_of_squared_numbers= []
#     for i in list:
#         list_of_squared_numbers.append(i**2)
#     print(list_of_squared_numbers)
# square_of_numbers(list_of_numbers)
sorted_list = list(filter(lambda number: number <15, list_of_numbers))
squared_list_of_numbers = list(map(lambda number: number**2, list_of_numbers))
print(squared_list_of_numbers)
print(sorted_list)


# lambda number
# print(next(list_of_numbers))
# print(next(list_of_numbers))

# list_of_numbers = []
# for i in range(1, 22):
#     if i%2 == 0:
#         list_of_numbers.append(i)
# print(list_of_numbers)