import numpy as np
import math

#------------------------------funciones auxiliares----------------------------------

def interpolacionLagrange(x, y):
    n = len(x)
    polinomio = np.poly1d(0.0)

    for i in range(n):
        Li = np.poly1d(1.0)
        for j in range(n):
            if i != j:
                # Calcular el término de Lagrange Li(x)
                coeficientes_Li = np.array([1.0, -x[j]], dtype=np.float64)
                Li *= np.poly1d(coeficientes_Li) / (x[i] - x[j])
        polinomio += y[i] * Li

    # Redondear los coeficientes del polinomio resultante
    polinomio_redondeado = np.poly1d(np.round(polinomio.coefficients).astype(int))

    return polinomio_redondeado

def unicidad(val, n):
    angulo = 2 * math.pi * val / n
    parte_real = round(math.cos(angulo))
    parte_imaginaria = round(math.sin(angulo))
    return complex(parte_real, parte_imaginaria)
#------------------------------------------------------------------------------------

#_________________________________METODOS____________________________________________

def Lagrange(polinomios):
    cantidad = sum(pol.order for pol in polinomios) + 1
    values = np.arange(round(-(cantidad/4)), 0.5 * cantidad - round(cantidad/4), 0.5, dtype=np.float64)
    #1.=================================EVALUACION:
    PQw = np.array([[pol(value) for value in values] for pol in polinomios])
    #2.=================================MUL. PUNTO:
    Mw = np.prod(PQw, axis=0)
    #3.==============================INTERPOLACION:
    return interpolacionLagrange(values, Mw)


def Vandermonde_R(polinomios):
    cantidad = sum(pol.order for pol in polinomios) + 1
    values = np.arange(round(-(cantidad/4)), 0.5 * cantidad - round(cantidad/4), 0.5, dtype=np.float64)
    #-=============Creamos-la-matriz-Vandermonde-R:
    matriz = np.vander(values, increasing=True)
    #1.=================================EVALUACION:
    PQw = [np.dot(matriz, np.pad(pol.coefficients[::-1], (0, cantidad - pol.order - 1), 'constant')) for pol in polinomios]
    #2.=================================MUL. PUNTO:
    Mw = np.prod(PQw, axis=0)
    #3.==============================INTERPOLACION:
    matriz_inversa = np.linalg.inv(matriz)
    polinomio_resultante = np.dot(matriz_inversa, Mw)[::-1]

    return np.poly1d(np.round(polinomio_resultante).astype(int))

def Vandermonde_I(polinomios):
    cantidad = sum(pol.order for pol in polinomios) + 1
    values = [unicidad(k,cantidad) for k in range(cantidad)]
    #-=============Creamos-la-matriz-Vandermonde-R:
    matriz = np.vander(values, increasing=True)
    determinante = np.linalg.det(matriz)
    if abs(determinante) < 1e-15:
      return "La matriz es singular. No se puede calcular la inversa."
    #1.=================================EVALUACION:
    PQw = [np.dot(matriz, np.pad(pol.coefficients[::-1], (0, cantidad - pol.order - 1), 'constant')) for pol in polinomios]
    #2.=================================MUL. PUNTO:
    print(PQw)
    Mw = np.prod(PQw, axis=0)
    print(Mw)
    #3.==============================INTERPOLACION:
    matriz_inversa = np.linalg.inv(matriz)
    polinomio_resultante = np.dot(matriz_inversa, Mw)[::-1]

    return np.poly1d(np.round(np.real(polinomio_resultante)).astype(int))

def Iterativo(polinomios):
    cantidad = sum(pol.order for pol in polinomios) + 1
    #1.===============================COEFICIENTES:
    coeficientes_pad = [np.pad(np.array(polinomio)[::-1], (0, cantidad - len(polinomio)), 'constant') for polinomio in polinomios]
    #1.=================================EVALUACION:
    DFTs = [np.fft.fft(coef) for coef in coeficientes_pad]
    #2.=================================MUL. PUNTO:
    Mw = np.prod(DFTs, axis=0)
    #3.================================CONVOLUCION:
    polinomio_resultante = np.fft.ifft(Mw)
    return np.poly1d(np.round(polinomio_resultante).astype(int)[::-1])
#____________________________________________________________________________________
