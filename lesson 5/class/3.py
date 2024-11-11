#Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while
add_number = int(input("Enter number n : "))
summa = 0
counter = 1
while counter <= add_number:
   summa  += counter ** 3
   counter += 1
print(summa)