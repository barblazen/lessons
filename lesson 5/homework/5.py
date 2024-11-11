#Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
n = int(input("Enter number n : "))
m = int(input("Enter number m : "))
sum_of_cubes = 0
for number in range(n, m+1):
    sum_of_cubes += number ** 3  # возведение числа в куб и добавление к сумме
#sum_of_cubes += number ** 3 — это сокращенная форма записи для sum_of_cubes = sum_of_cubes + number ** 3.
#Здесь к текущему значению переменной sum_of_cubes добавляется результат возведения number в куб.
# Например, если sum_of_cubes было 0 и number равно 2, то после выполнения этой строки sum_of_cubes станет 8.
print("Сумма кубов натуральных чисел от", n, "до", m, "равна:", sum_of_cubes)