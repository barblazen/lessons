# Строка называется палиндромом, если она пишется одинаково в обоих направлениях.
# Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah».
# Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом.
def write_string():
    your_string = input("enter your string : ")
    reversed_string = your_string[::-1]
    if your_string == reversed_string:
        print("Your string is палиндром ")
    else:
        print("Your string is not палиндром")
write_string()
