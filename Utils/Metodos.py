import numpy as np

#------------------------------funciones auxiliares----------------------------------

def interpolacionLagrange(x, y):
    n = len(x)
    #===== Inicializar el polinomio como 0
    polinomio = np.poly1d(0.0)

    for i in range(n):
        #===Calcular el término de Lagrange Li(x)
        Li = np.poly1d([1.0])
        for j in range(n):
            if i != j:
                Li *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])
        #===Sumar el término de Lagrange multiplicado por y[i]
        polinomio += y[i] * Li

    return polinomio

#------------------------------------------------------------------------------------

#_________________________________METODOS____________________________________________

def Lagrange(polinomios):
    cantidad = 1
    for pol in polinomios:
        cantidad += pol.order
    values = [k for k in range(cantidad)]
    
    #1.=================================EVALUACION:
    PQw = []
    for pol in polinomios:
        PQw.append([pol(value) for value in values])

    #2.=================================MUL. PUNTO:
    Mw = []
    for i in range(cantidad):
        prod_punto = 1
        for j in range(len(PQw)):
            prod_punto *= PQw[j][i]
        Mw.append(prod_punto)

    #3.==============================INTERPOLACION:
    return interpolacionLagrange(values, Mw)

def Vandermonde_R(polinomios):
    cantidad = 1
    for pol in polinomios:
        cantidad += pol.order
    values = [k for k in range(cantidad)]

    #-=============Creamos-la-matriz-Vandermonde-R:
    matriz = np.vander(values, increasing=True)

    #1.=================================EVALUACION:
    PQw = []
    for pol in polinomios:
        coef = np.pad(pol.coefficients[::-1], (0, len(values) - pol.order - 1), 'constant')
        PQw.append(np.dot(matriz, coef))

    #2.=================================MUL. PUNTO:
    Mw = []
    for i in range(cantidad):
        prod_punto = 1
        for j in range(len(PQw)):
            prod_punto *= PQw[j][i]
        Mw.append(prod_punto)

    #3.==============================INTERPOLACION:
    matriz_inversa = np.linalg.inv(matriz)
    polinomio_resultante = np.dot(matriz_inversa,Mw)[::-1]

    return np.poly1d(polinomio_resultante)
    
#____________________________________________________________________________________