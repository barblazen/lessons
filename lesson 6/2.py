#Пользователь вводит свое имя, фамилию и возраст. Программа должна вывести строку формата:
# "Привет, [Имя] [Фамилия]! Тебе [Возраст] лет."
user_info = input("Enter your name, surname, age : ").split()
print(f"Hello {user_info[0]} {user_info[1]}! You are {int(user_info[2])}")
