#Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
def print_of_name(name):
    print(f"Hello, {name}")
print_of_name("Lil")
print_of_name("MArk")

names = ["Alex", "Bob", "LEna", "Diana", "Eve"]
for name in names:
    print(f"Hello, {name}")