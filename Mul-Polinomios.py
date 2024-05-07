import tkinter as tk
import time
from Utils.Metodos import *
from Utils.libreria import *

def GraficarPolinomios(polinomioss, ley, position):
  canvas = FigureCanvasTkAgg(plot_function(polinomioss, leyenda=ley), master=window)
  canvas.draw()
  canvas.get_tk_widget().place(x=position[0],y=position[1])

def Mostrar_graficos(result):
  GraficarPolinomios(Lista_Polinomios, True, (int(0.7*width), int(0.10*height)))
  GraficarPolinomios([result], False, (int(0.7*width), int(0.5*height)))

def Mostrar_resultado(result):
  resultado.delete(1.0, tk.END)
  resultado.insert(tk.END, result)
  Mostrar_graficos(result)


def Limpiar_todo():
  Lista_Polinomios.clear()
  polinomios.delete(1.0, tk.END)
  resultado.delete(1.0, tk.END)
  tiempo_lagrange.delete(1.0, tk.END)
  tiempo_vander_r.delete(1.0, tk.END)
  tiempo_vander_i.delete(1.0, tk.END)
  tiempo_iterativo.delete(1.0, tk.END)
  GraficarPolinomios([[0]], False, (int(0.7*width), int(0.10*height)))
  GraficarPolinomios([[0]], False, (int(0.7*width), int(0.5*height)))

def IngresarPolinomio():
  pol = obtener_coeficientes(polinomio.get())
  Lista_Polinomios.append(pol)
  polinomio.delete(0, tk.END)
  polinomios.insert(tk.END, "--------------------------------------------------")
  polinomios.insert(tk.END, pol)
  polinomios.insert(tk.END, "\n")

def metodo_lagrange(estado=True):
  inicio = time.time()
  result = Lagrange(Lista_Polinomios)
  fin = time.time()
  tiempo_lagrange.delete(1.0, tk.END)
  tiempo_lagrange.insert(tk.END, round((fin - inicio)*1000, 3))
  if estado:
    Mostrar_resultado(result)

def metodo_vandermonde_R(estado=True):
  inicio = time.time()
  result = Vandermonde_R(Lista_Polinomios)
  fin = time.time()
  tiempo_vander_r.delete(1.0, tk.END)
  tiempo_vander_r.insert(tk.END, round((fin - inicio)*1000, 3))
  if estado:
    Mostrar_resultado(result)

def metodo_vandermonde_I(estado=True):
  inicio = time.time()
  result = Vandermonde_I(Lista_Polinomios)
  fin = time.time()
  tiempo_vander_i.delete(1.0, tk.END)
  tiempo_vander_i.insert(tk.END, round((fin - inicio)*1000, 3))
  if estado:
    Mostrar_resultado(result)

def todos_los_metodos():
  metodo_lagrange(estado=False)
  metodo_vandermonde_R(estado=True)
  metodo_vandermonde_I(estado=True)


#__________________________________________________________________________________________________________________________
#-----------------Creamos la ventana principal--------------------
window = tk.Tk()
window.title("MULTIPLICACION DE POLINOMIOS")
# Obtenemos las dimensiones de la pantalla
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(str(800)+'x'+str(510))
#------------------------------------------------------------------

#---------------------------------------------------------------CUERPO------------------------------------------------------
tk.Label(window,text='MULTIPLICACIÓN DE POLINOMIOS',fg='black',font="Courier 25 roman bold").place(x=int(0.35*width),y=20)

#===========================INGRESAR POLINOMIO==========================
tk.Label(window,text='INGRESE COEFICIENTES DEL POLINOMIO : ',fg='blue',font='Arial 15 bold').place(x=int(0.35*width),y=int(0.15*height))

Lista_Polinomios = []
polinomio = tk.Entry(window,width= 30, font="Courier 18 roman bold", bg='white')
polinomio.place(x=int(0.35*width),y=int(0.2*height))
#=======================================================================

tk.Label(window,text='POLINOMIOS: ',fg='red',font='Arial 15 bold').place(x=int(0.05*width),y=int(0.05*height))
polinomios = tk.Text(window,width="50",height="12", font="Courier 10 roman bold")
polinomios.place(x=int(0.05*width),y=int(0.10*height))

tk.Label(window,text='MÉTODOS: ',fg='red',font='Arial 15 bold').place(x=int(0.4*width),y=int(0.3*height))

tk.Label(window,text='tiempos de ejecución (ms): ',fg='blue',font='Arial 10 bold').place(x=int(0.5*width),y=int(0.32*height))

#=================================BOTONES===============================
button_clear = tk.Button(window, text='Limpiar todo', font='Arial 14 bold', command=Limpiar_todo)
button_clear.place(x=int(0.54*width),y=int(0.65*height))

button_add = tk.Button(window, text='ADD', font='Arial 15 bold', command=IngresarPolinomio)
button_add.place(x=int(0.58*width),y=int(0.25*height))

button1 = tk.Button(window, text='LAGRANGE', font='Courier 15 bold', command=metodo_lagrange)
button1.place(x=int(0.35*width),y=int(0.35*height))

button2 = tk.Button(window, text='VANDER R', font='Courier 15 bold', command=metodo_vandermonde_R)
button2.place(x=int(0.35*width),y=int(0.41*height))

button3 = tk.Button(window, text='VANDER I', font='Courier 15 bold', command=metodo_vandermonde_I)
button3.place(x=int(0.35*width),y=int(0.47*height))

button4 = tk.Button(window, text='ITERATIV', font='Courier 15 bold')
button4.place(x=int(0.35*width),y=int(0.53*height))

button4 = tk.Button(window, text='MOSTRAR TODO', font='Courier 15 bold', command=todos_los_metodos)
button4.place(x=int(0.35*width),y=int(0.59*height))

#================================TIEMPOS=================================
tk.Label(window,text='LA: ',fg='green',font='Courier 15 bold').place(x=int(0.5*width),y=int(0.35*height))
tiempo_lagrange = tk.Text(window,width="10",height="1", font="Courier 15 roman bold")
tiempo_lagrange.place(x=int(0.54*width),y=int(0.35*height))

tk.Label(window,text='VR: ',fg='green',font='Courier 15 bold').place(x=int(0.5*width),y=int(0.41*height))
tiempo_vander_r = tk.Text(window,width="10",height="1", font="Courier 15 roman bold")
tiempo_vander_r .place(x=int(0.54*width),y=int(0.41*height))

tk.Label(window,text='VI: ',fg='green',font='Courier 15 bold').place(x=int(0.5*width),y=int(0.47*height))
tiempo_vander_i = tk.Text(window,width="10",height="1", font="Courier 15 roman bold")
tiempo_vander_i.place(x=int(0.54*width),y=int(0.47*height))

tk.Label(window,text='IT: ',fg='green',font='Courier 15 bold').place(x=int(0.5*width),y=int(0.53*height))
tiempo_iterativo = tk.Text(window,width="10",height="1", font="Courier 15 roman bold")
tiempo_iterativo.place(x=int(0.54*width),y=int(0.53*height))

#========================================================================


#RESULTADO
tk.Label(window,text='RESULTADO: ',fg='red',font='Arial 20 bold').place(x=int(0.25*width),y=int(0.7*height))
resultado = tk.Text(window,width="80",height="4", font="Courier 12 roman bold")
resultado.place(x=int(0.10*width),y=int(0.75*height))

Limpiar_todo()

window.mainloop()
