#Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.

#  def get_numbers(*args):
#     sum_of_numbers = 0
#     for i in args:
#         if isinstance(i, str) and not i.isdigit():
#             print("Error")
#             continue
#         sum_of_numbers += int(i)
#     print(sum_of_numbers)
#     # max_number = max(args)
#     # print(max_number)
# get_numbers(2, 3, 5, 7, 9, "Hello", 10, "100")

def max_number(*args):
    new_sequence = []
    for i in args:
        if isinstance(i,(int, float)) or isinstance(i, str) and i.isdigit():
            new_sequence.append(float(i))
    print(new_sequence)
    print(max(new_sequence))

max_number(3, 6, 9.5, "hello", "100")
