from matplotlib import pyplot as plt
import streamlit as st
from integrales.trapeciosif import rectint
import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr,standard_transformations, implicit_multiplication_application, transformations

def trapecio_if():
    x = sp.Symbol('x')
    funct = st.text_input('Ingrese la función',
                                value='x**2-2*x+3')
    a = int(st.text_input('Ingrese extremo izquierdo: ',value='-5'))
    #a = -5
    b = int(st.text_input('Ingrese extremo derecho: ',value='10'))
    #b = 10
    rectangles = int(st.text_input('Ingrese numero de particiones:', value='15'))
    #tramos = 15
    funct = str(parse_expr(funct,transformations=transformations))
    funcion = sp.lambdify(x,funct,'numpy')

    col_expr, col_vals = st.columns(2)
    col_vals.write(' Integral:')
    print("FUNCIONN ", funcion)
    st.write(rectint(funcion, a, b,rectangles))

    muestras = rectangles + 1
    xi = np.linspace(a,b,muestras)
    fi = funcion(xi)
    # Linea suave
    muestraslinea = rectangles*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = funcion(xk)

    # Graficando
    plt.plot(xk,fk, label ='f(x)')
    plt.plot(xi,fi, marker='o',
            color='orange', label ='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Rectangulos')
    plt.legend()


    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')

    #plt.show()
    st.pyplot(plt,figsize=(2, 2))