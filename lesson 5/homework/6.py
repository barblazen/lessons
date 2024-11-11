#Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ,
#из этих чисел составляется первый список. Далее таким же образом вводятся второй и третий списки.
#Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем
first_list_of_numbers = []
second_list_of_numbers = []
third_list_of_numbers = []
result_list = []
while True:
    adding = input("Enter a number : ")
    if adding.isdigit():
        number = int(adding)
        first_list_of_numbers.append(number)
    else:
        break
print(first_list_of_numbers)
while True:
    adding = input("Enter a number : ")
    if adding.isdigit():
        number = int(adding)
        second_list_of_numbers.append(number)
    else:
        break
print(second_list_of_numbers)
while True:
    adding = input("Enter a number : ")
    if adding.isdigit():
        number = int(adding)
        third_list_of_numbers.append(number)
    else:
        break
print(third_list_of_numbers)
for element in first_list_of_numbers :
    print(element)
    if element in second_list_of_numbers and element not in third_list_of_numbers:
        result_list.append(element)
print(result_list)