import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def C(t, A, sigma1, sigma2):
    """
    Calcula la concentración del medicamento en función del tiempo t.
    
    Parámetros:
    - t: tiempo (float o array)
    - A: constante positiva específica del fármaco
    - sigma1: constante positiva (menor)
    - sigma2: constante positiva (mayor que sigma1)
    
    Retorna: valor(es) de la función C(t)
    """
    return (A / (sigma2 - sigma1)) * (np.exp(-sigma1 * t) - np.exp(-sigma2 * t))

# Parámetros del modelo
A = 100
sigma1 = 0.5
sigma2 = 1.0

# Definir la función en función de t para optimización
C_func = lambda t: C(t, A, sigma1, sigma2)

# Buscar el máximo aproximado (minimizamos el negativo de C(t))
resultado = minimize_scalar(lambda t: -C_func(t), bounds=(0, 20), method='bounded')
t_max = resultado.x
C_max = C_func(t_max)

print("Tiempo en el que se alcanza el máximo (t*):", t_max)
print("Máximo de la concentración (C_max):", C_max)

# Graficar la función C(t)
t_values = np.linspace(0, 20, 400)
C_values = C_func(t_values)

plt.figure(figsize=(8, 5))
plt.plot(t_values, C_values, label=r'$C(t)=\frac{A}{\sigma_2-\sigma_1}\left(e^{-\sigma_1t}-e^{-\sigma_2t}\right)$')
plt.plot(t_max, C_max, 'ro', label=r'Máximo ($t^*,\, C(t^*)$)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Concentración (C)')
plt.title('Concentración del Medicamento vs Tiempo')
plt.legend()
plt.grid(True)
plt.show()
