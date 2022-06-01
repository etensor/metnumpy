from symtable import Symbol
from matplotlib import pyplot as plt
import streamlit as st
import sympy as sp
import numpy as np
#from sympy.parsing.sympy_parser import parse_expr,standard_transformations, implicit_multiplication_application, transformations
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))


def trapecios_if():
    # Integración: Regla de los trapecios
    # Usando una función fx()
    # INGRESO
    fx = st.text_input('Ingrese la función:',
                            value='x**2-2*x+3')
    #fx = lambda x: x**2-2*x+3
    x = sp.symbols('x')
    # intervalo de integración
    a = float(parse_expr(st.text_input('Ingrese extremo izquierdo: ',value='-5'),transformations=transformations))
    b = float(parse_expr(st.text_input('Ingrese extremo derecho: ',value='10'),transformations=transformations))
    #b = 10
    particiones = int(st.text_input('Ingrese numero de particiones:', value='15'))
    #tramos = 15
    fx = str(parse_expr(fx,transformations = transformations))
    funcion = sp.lambdify(x,fx,'numpy')

    #ya tengo la de rectangulo con grafica tambien
    #https://replit.com/join/qalniwjdxi-sergioangel
    #ahi esta
    #jaajaja
    # suave ya se puede ver hasta el mouse en replit xD
    # ya me pongo a meter esta mierda en streamlit 
    # poder pasarle datos a lo que seria una funcion
    # dinamica


    # PROCEDIMIENTO
    # Regla del Trapecio
    # Usando tramos equidistantes en intervalo
    h = (b-a)/particiones
    xi = a
    suma = funcion(xi)
    for i in range(0,particiones-1,1):
        xi = xi + h
        suma = suma + 2*funcion(xi)
    suma = suma + funcion(b)
    area = h*(suma/2)

    # SALIDA
    #col_expr, col_vals = st.columns(2)
    #st.write('Particion:')
    #col_vals.write('Integral:')
    st.write("Valor integral definido: ", area)
    st.write("Intervalo: [", a, ", ", b, "]")


    # GRAFICA
    # Puntos de muestra
    muestras = particiones + 1
    xi = np.linspace(a,b,muestras)
    fi = funcion(xi)
    # Linea suave
    muestraslinea = particiones*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = funcion(xk)

    # Graficando
    #plt.plot(xk,fk, label ='f(x)')
    #plt.plot(xi,fi, marker='o',
            # color='orange', label ='muestras')
    plt.plot(xk,fk, label ='f(x)')
    plt.plot(xi,fi, marker='o',
            color='orange', label ='muestras')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Trapecios')
    plt.legend()

    # Trapecios
    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')
    
    st.pyplot(plt,figsize=(2, 2))