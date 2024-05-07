import math
import numpy as np

def unicidad(val, n):
    angulo = 2 * math.pi * val / n
    parte_real = round(math.cos(angulo))
    parte_imaginaria = round(math.sin(angulo))
    return complex(parte_real, parte_imaginaria)
n = 5
values = [unicidad(k,n) for k in range(n)]

matriz = np.vander(values, increasing=True)
print(matriz)
