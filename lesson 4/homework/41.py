# Упражнение 41. Классификация треугольников
# Все треугольники могут быть отнесены к тому или иному классу (равнобедренные, равносторонние и разносторонние)
# на основании длин их сторон. Равносторонний треугольник характеризуется одинаковой длиной всех трех сторон,
# равнобедренный – двух сторон из трех, а у разностороннего треугольника все стороны разной длины.
# Напишите программу, которая будет запрашивать у пользователя длины всех трех сторон треугольника и выдавать сообщение о том,
# к какому типу следует его относить.
length_of_side_1 = int(input("Enter length of first side : "))
length_of_side_2 = int(input("Enter length of second side : "))
length_of_side_3 = int(input("Enter length of third side : "))
if length_of_side_1 == length_of_side_2 == length_of_side_3:
    print("Triangle is equilateral")
elif (length_of_side_1 == length_of_side_2 != length_of_side_3) or \
        (length_of_side_2 == length_of_side_3 != length_of_side_1) or \
        (length_of_side_1 == length_of_side_3 != length_of_side_2):
    print("Triangle is isosceles ")
else:
    print("Triangle is scalene")
