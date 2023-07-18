import numpy as np

# исходные данные
x = np.array([0.4, 0.9, 0.99])
y = np.array([10, 100, 1000])

# Преобразование y в ln(y)
y = np.log(y)

# Выполнение линейной регрессии
coefficients = np.polyfit(x, y, 1)

# Преобразование коэффициентов обратно
a, b = np.exp(coefficients[1]), np.exp(coefficients[0])

print(f"a = {a}, b = {b}") #y = 0.5904697107153318 * (831.4352620676465)^x.