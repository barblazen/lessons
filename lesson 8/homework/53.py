# Ввод числовой оценки
score = float(input("Введите числовую оценку (например, 3.5): "))

# Определение буквенной оценки
if score >= 4.0:
    grade = "A+"
elif 3.85 <= score < 4.0:
    grade = "A"
elif 3.5 <= score < 3.85:
    grade = "A-"
elif 3.15 <= score < 3.5:
    grade = "B+"
elif 2.85 <= score < 3.15:
    grade = "B"
elif 2.5 <= score < 2.85:
    grade = "B-"
elif 2.15 <= score < 2.5:
    grade = "C+"
elif 1.85 <= score < 2.15:
    grade = "C"
elif 1.5 <= score < 1.85:
    grade = "C-"
elif 1.15 <= score < 1.5:
    grade = "D+"
elif 0.85 <= score < 1.15:
    grade = "D"
else:
    grade = "F"

# Вывод результата
print(f"Числовая оценка {score} соответствует буквенной оценке {grade}.")
