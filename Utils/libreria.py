import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def obtener_coeficientes(string):
  return np.poly1d(list(map(int, string.split()))[::-1])

def plot_function(polynomials, leyenda = True):
    # Generar valores de x
    x_values = np.linspace(-4, 4, 100)
    # Crear una figura de Matplotlib
    fig = Figure(figsize=(4, 3), dpi=100)
    # Agregar un subplot a la figura
    plot = fig.add_subplot(1, 1, 1)

    for polynomial in polynomials:
        # Calcular valores de y para el polinomio
        y_values = np.polyval(polynomial, x_values)
        
        # Graficar el polinomio
        plot.plot(x_values, y_values, label=f"Polinomio: {polynomial}")
    
    if leyenda == True:
      plot.legend()
    # Graficar la función
    plot.plot(x_values, y_values)
    # Agregar líneas X e Y
    plot.axhline(0, color='black',linewidth=0.5)
    plot.axvline(0, color='black',linewidth=0.5)

    # Agregar título al gráfico
    #plot.title('Gráfico de dispersión')

    # Limitar los ejes X e Y
    #plot.set_ylim(-1000, 1000)

    return fig