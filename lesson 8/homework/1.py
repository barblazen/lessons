#Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
# В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None.
# Получим, например, следующее сообщение:
#Переданы аргументы: var1 = 2, var3 = 10.
def three_args(var1=None, var2=None, var3=None):
    # Составляем список переданных значений, игнорируя None
    args = []

    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")

    # Формируем сообщение
    if args:
        print("Переданы аргументы:", ", ".join(args))
    else:
        print("Аргументы не были переданы.")


# Примеры вызова функции
three_args(var1=2, var3=10)  # Пример с двумя аргументами
three_args(var2=5)  # Пример с одним аргументом
three_args()  # Пример без аргументов
