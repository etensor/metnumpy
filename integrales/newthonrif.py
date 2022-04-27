import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.style.use('seaborn')

def graficar(f, x_i, x_f, num = 1000):
    """
    Gráfica de funciones algebraicas
    :param f: función, previamente definida
    :param x_i: límite inferior del intervalo
    :param x_f: límite superior del intervalo
    :param num: división del intervalo
    :return: gráfica de la función
    """
    x = np.linspace(x_i, x_f, num)
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(x, f(x))
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.annotate("", xy=(xmax, 0), xytext=(xmin, 0),arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    ax.annotate("", xy=(0, ymax), xytext=(0, ymin),arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    plt.show()
    return None
  
def newthonr(f,df,p_0,tol=10**4,n=50):
  

  # f: funcion
  # df: derivada de la funcion
  # p_0: semilla (punto inicial)
  # tol: tolerancia, critero de parada
  # n: numero max de iteraciones
  # retorna solucion exacta o aproximada
  #e_abs: error absoluto

  print('iteracion {:<2}: p{:<2}={:.7f}'.format(0,0,p_0))
  e_abs = 1
  i = 1
  while i <= n:
    if df(p_0) == 0:
      print('Solucion no encontrada = df(x)=0')
      return None
      
    p_1 = p_0 - (f(p_0))/(df(p_0)) #formula
    e_abs = abs(p_1-p_0)
    print('iteracion {:<2}: p{:<2}={:.7f}, e_abs={:.7f}'.format(i,i,p_1,e_abs))
  
    if e_abs < tol:
      print('Solucion x={:.7f}, iteraciones: {}'.format(p_1,i))
      return p_1
  
    p_0 = p_1
    i += 1
  
  print('solucion no encontrada, iteraciones agotadas: {}'.format(i-1))
  return None

def f(x):
  return x**x - 100

def df(x):
  
  
  return x**x * (np.log(x) + 1)

  

newthonr(f, df, 3.8, 10**-10)

#grafica
graficar(f,-10,10)
