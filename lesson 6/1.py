#Калькулятор скидки
# Пользователь вводит стоимость товара и процент скидки.
# цена и скидка через пробел split
# Вычислите и выведите на экран окончательную цену товара после применения скидки.
added_numbers = input("Enter the price and discount : ").split()
price = int(added_numbers[0])
discount = int(added_numbers[1])
final_price = price - price * discount / 100
print(final_price)


