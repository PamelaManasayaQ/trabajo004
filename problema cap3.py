import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 + x + 1
def g1(x):
    return x**2  
def g2(x):
    return x  
def check_big_o(f, g, x_values, C):
    """
    Verifica si f(x) <= C * g(x) para los valores de x dados.
    """
    for x in x_values:
        if f(x) > C * g(x):
            return False  
    return True
x_values = np.linspace(1, 100, 1000)
C1 = 3  # Para O(x^2)
C2 = 1  # Para O(x)
is_big_o_x2 = check_big_o(f, g1, x_values, C1)
print(f"x^2 + x + 1 es O(x^2): {is_big_o_x2}")
is_big_o_x = check_big_o(f, g2, x_values, C2)
print(f"x^2 + x + 1 es O(x): {is_big_o_x}")
plt.plot(x_values, f(x_values), label="f(x) = x^2 + x + 1", color='b')
plt.plot(x_values, C1 * g1(x_values), label="C * x^2", linestyle='--', color='r')
plt.plot(x_values, C2 * g2(x_values), label="C * x", linestyle='--', color='g')
plt.xlabel("x")
plt.ylabel("Valor")
plt.title("Comparación de O(x^2) y O(x) para x^2 + x + 1")
plt.legend()
plt.grid(True)
plt.show()
