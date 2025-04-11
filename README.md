# Máximo de la Función de Concentración \(C(t)\)

Este repositorio contiene un script en Python que modela la concentración de un medicamento a lo largo del tiempo según la siguiente ecuación:

![Ecuación](http://latex.codecogs.com/png.latex?C(t)%3D%5Cfrac%7BA%7D%7B%5Csigma_2-%5Csigma_1%7D%5Cleft(e%5E%7B-%5Csigma_1t%7D-e%5E%7B-%5Csigma_2t%7D%5Cright))

El objetivo es determinar numéricamente el máximo absoluto de \(C(t)\) y visualizar su comportamiento.

## Descripción

El script implementa:
- La definición de la función \(C(t)\) con parámetros \(A\), \(\sigma_1\) y \(\sigma_2\).
- Una rutina de optimización usando `scipy.optimize.minimize_scalar` para hallar el tiempo \(t^*\) en el que la función alcanza su máximo \(C_{\text{max}}\).
- La generación de una gráfica con `matplotlib` donde se muestra la curva de \(C(t)\) y se resalta el punto de máximo.

Este trabajo forma parte de un proyecto para la Jornada Científica Estudiantil de la Facultad de Matemática y Computación en la Universidad de La Habana en el cual se integran fundamentos teóricos del análisis matemático (específicamente, los teoremas de Weierstrass) con herramientas computacionales.

## Requisitos

Debe poseer instalado:
- Python (se recomienda versión 3.6 o superior)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [SciPy](https://www.scipy.org/)

Es posible instalar estas librerías usando `pip`:

```bash
pip install numpy matplotlib scipy
