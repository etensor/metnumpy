import streamlit as st
from derivadas.secante import secante
from plotterfuncion import plot_funcion
from sympy import lambdify, Symbol
import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from derivadas.derivadas import transformations
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import sympy as sp

transformations = (standard_transformations +
                   (implicit_multiplication_application,))

x = sp.Symbol('x')
def secante_if():
    f = st.text_input('Ingrese la función',
                            value='exp(-x)+2*log(x)*-1')
    a = int(st.text_input('Ingrese rango inferior: ',value='1'))
    b = int(st.text_input('Ingrese rango superior: ',value='2'))
    xa = float(st.text_input('Ingrese xa:', value='1.5'))
    tolera = float(st.text_input('Ingrese tolerancia:', value='0.001'))
    tramos = int(st.text_input('Ingrese tramos que desea:', value='10'))

    fx = str(parse_expr(f,transformations=transformations))
    f = sp.lambdify(x,f,'numpy')

    tabla = secante(fx,xa,tolera)
    n = len(tabla)
    raiz = tabla[n-1,2]

    np.set_printoptions(precision=4)
    st.write('[0 = xa ,\t 1 = xb , \t 2 = xc , \t 3= tramo]')
    for i in range(0,n,1):
        st.write(tabla[i])
    st.write('raiz en: ', raiz)

    # Calcula los puntos a graficar
    xi = np.linspace(a,b,tramos+1)
    fi = f(xi)
    dx = (b-xa)/2
    pendiente = (f(xa+dx)-f(xa))/(xa+dx-xa)
    b0 = f(xa) - pendiente*xa
    tangentei = pendiente*xi+b0

    fxa = f(xa)
    xb = xa + dx
    fxb = f(xb)

    plt.plot(xi,fi, label='f(x)')

    plt.plot(xi,tangentei, label='secante')
    plt.plot(xa,f(xa),'go', label='xa')
    plt.plot(xa+dx,f(xa+dx),'ro', label='xb')
    plt.plot((-b0/pendiente),0,'yo', label='xc')

    plt.plot([xa,xa],[0,fxa],'m')
    plt.plot([xb,xb],[0,fxb],'m')

    plt.axhline(0, color='k')
    plt.title('Método de la Secante')
    plt.legend()
    plt.grid()
    #plt.show()
    st.pyplot(plt,figsize=(2, 2))