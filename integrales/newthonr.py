import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

def root(f,df,x0,tol):
    error=1e3
    n=1
    while error>tol:
        x0 = x0-f(x0)/df(x0)
        error=abs(f(x0))
        n+=1

        st.text(error)

    st.write('Raiz aproximada',x0)
    st.write('Numero de iteraciones',n)


def graficar(f, x_i, x_f, num = 1000):
    """
    Gráfica de funciones algebraicas
    :param f: función, previamente definida
    :param x_i: límite inferior del intervalo
    :param x_f: límite superior del intervalo
    :param num: división del intervalo
    :return: gráfica de la función
    """
    f,df = root(f) # ??? aqui iba fs pero no se que es :(
    x = np.linspace(x_i, x_f, num)
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(x, f(x))
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.annotate("", xy=(xmax, 0), xytext=(xmin, 0),arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    ax.annotate("", xy=(0, ymax), xytext=(0, ymin),arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    return plt

        
