#
def count_numbers(number_1, number_2):
    if number_1 % 2 == 0 and number_2 % 2 == 0:
        print("oba chetnye")
    elif number_1%2 !=0 and number_2 %2 !=0:
        print("oba nechetnye")
    else:
        print("odno nechetnoye")
count_numbers(7, 9)
