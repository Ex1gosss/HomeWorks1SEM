###1
import math

def find_min_angle_point(points):
    min_angle = float('inf')
    min_point = None
    
    for point in points:
        x, y = point
        angle = math.atan2(y, x)  # Угол в радианах
        
        if angle < 0:
            angle += 2 * math.pi  # Привести угол к диапазону [0, 2π]
        
        if angle < min_angle:
            min_angle = angle
            min_point = point
            
    return min_point

# Пример использования
points = [(x1, y1), (x2, y2), (z1, z2)]
min_angle_point = find_min_angle_point(points)

print("Координаты точки с минимальным углом:", min_angle_point)



###2
def is_palindrome(binary_str):
    return binary_str == binary_str[::-1]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_palindromic_binaries(n):
    result = []
    for num in range(2, n + 1):
        if is_prime(num):
            binary_str = bin(num)[2:]  # Получаем двоичную запись числа
            if is_palindrome(binary_str):
                result.append(num)
    return result

# Пример использования
n = 100  # Замените на ваше значение
prime_palindromic_binaries = find_prime_palindromic_binaries(n)

print("Простые числа с палиндромной двоичной записью до", n, ":", prime_palindromic_binaries)

