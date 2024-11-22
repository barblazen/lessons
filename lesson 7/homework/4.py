#Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем "Winter".
def month_to_season(month):
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    return "Invalid month number"
print(month_to_season(2))
