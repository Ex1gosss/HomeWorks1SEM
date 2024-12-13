# ###1
# import math

# R = float(input("Введите радиус R в сантиметрах: "))
# range = 2 * math.pi * R
# area = math.pi * R ** 2

# range = round(range, 2)
# area = round(area, 2)

# print(f"Длина окружности: {range} см")
# print(f"Площадь круга: {area} см²")


# ###2

# x = 10
# y = 55

# print(f"До замены: x = {x}, y = {y}")

# x, y = y, x

# print(f"После замены: x = {x}, y = {y}")

###3
import math

g = 9.81

L = float(input("Введите длину маятника в метрах: "))

T = 2 * math.pi * math.sqrt(L / g)

print(f"Период колебания маятника: {T:.2f} секунд")
