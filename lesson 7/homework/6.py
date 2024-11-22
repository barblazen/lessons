#Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
# Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
# Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
# причем сам себе человек не может подарить,дубликаты тоже не допустимы.

import random
def secret_santa(participants):
    # Реализует распределение подарков для игры 'Тайный Санта'.
    # :param participants: list - список имен участников.
    # :return: dict - пары "кто -> кому".
    if len(participants) < 2:
        raise ValueError("Участников должно быть не менее двух.")

    givers = participants[:]  # Копируем список дарящих
    receivers = participants[:]  # Копируем список получателей

    random.shuffle(receivers)  # Перемешиваем список получателей

    # Перемешиваем до тех пор, пока не получится валидное распределение
    while any(giver == receiver for giver, receiver in zip(givers, receivers)):
        random.shuffle(receivers)

    # Формируем пары в виде словаря
    pairs = {giver: receiver for giver, receiver in zip(givers, receivers)}
    return pairs


# Пример использования
participants = ["Alex", "Bob", "Charlie", "Diana", "Eve"]
pairs = secret_santa(participants)

# Вывод результатов
for giver, receiver in pairs.items():
    print(f"{giver} -> {receiver}")
