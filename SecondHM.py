###1
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
try:
    result = num1 / num2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")



###2 
total_amount = float(input("Введите сумму покупки (в у.е.): "))
discount_rate = 0.35
discount = 0
if total_amount > 20:
    discount = total_amount * discount_rate
final_amount = total_amount - discount
final_amount = round(final_amount, 2)
discount = round(discount, 2)
print(f"Размер предоставленной скидки: {discount} у.е.")
print(f"Итоговая стоимость покупки: {final_amount} у.е.")


###3 
months = {
    1: ("Январь", "Зима"),
    2: ("Февраль", "Зима"),
    3: ("Март", "Весна"),
    4: ("Апрель", "Весна"),
    5: ("Май", "Весна"),
    6: ("Июнь", "Лето"),
    7: ("Июль", "Лето"),
    8: ("Август", "Лето"),
    9: ("Сентябрь", "Осень"),
    10: ("Октябрь", "Осень"),
    11: ("Ноябрь", "Осень"),
    12: ("Декабрь", "Зима"),
}

month_number = int(input("Введите номер месяца (от 1 до 12): "))
if month_number in months:
    month, season = months[month_number]
    print(f"{month} - {season}")
else:
    print("Ошибка: Введено недопустимое число. Пожалуйста, введите число от 1 до 12.")
