#Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
list = [2, 4, 7, 22, 55, 45, 66, 79, 88]
summa = 0
for element in list:
  if  element > 10:
      summa += element
print(summa)
