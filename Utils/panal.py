import numpy as np

# Definir la matriz dada
matriz = np.array([[ 1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j],
                   [ 1.+0.j,  1.+1.j,  0.+2.j, -2.+2.j, -4.+0.j, -4.-4.j,  0.-8.j],
                   [ 1.+0.j,  0.+1.j, -1.+0.j, -0.-1.j,  1.-0.j,  0.+1.j, -1.+0.j],
                   [ 1.+0.j, -1.+0.j,  1.-0.j, -1.+0.j,  1.-0.j, -1.+0.j,  1.-0.j],
                   [ 1.+0.j, -1.+0.j,  1.-0.j, -1.+0.j,  1.-0.j, -1.+0.j,  1.-0.j],
                   [ 1.+0.j,  0.-1.j, -1.-0.j, -0.+1.j,  1.+0.j,  0.-1.j, -1.-0.j],
                   [ 1.+0.j,  1.-1.j,  0.-2.j, -2.-2.j, -4.+0.j, -4.+4.j,  0.+8.j]])

# Calcular el determinante
determinante = np.linalg.det(matriz)

# Verificar si la matriz es singular (determinante cercano a cero)
if abs(determinante) < 1e-15:
    print("La matriz es singular. No se puede calcular la inversa.")
else:
    # Calcular la inversa
    inversa = np.linalg.inv(matriz)
    print("La inversa de la matriz dada es:")
    print(inversa)
