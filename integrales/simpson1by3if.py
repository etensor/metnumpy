from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
import sympy as sp
from integrales.simpson1by3 import empezar
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def simpson1by3_if():
    funcion = ''
    x = sp.Symbol('x')
    #function = st.text_input("Ingresa la función")
    function = st.text_input('Ingrese la función',
                                value='')
    izq = int(st.text_input('Limite izquierdo', value = 0))
    der = int(st.text_input('Limite derecho', value = 0))
    intervalos = int(st.text_input('Numero de intervalos', value = 0))

    if function != "":
        function = str(parse_expr(function,transformations=transformations))
        funcion = sp.lambdify(x,function,'numpy')

    if izq >= der:
        st.write('El limite izquierdo no puede ser mayor al derecho')
        pasar = False
    else:
        pasar = True
    
    if pasar and function != '' and intervalos > 0:
        resultado = empezar(function, izq, der, intervalos)

        st.success(f'Valor integral definido: {resultado}')
        st.write("Intervalo: [", izq, ", ", der, "]")

        muestras = intervalos + 1
        xi = np.linspace(izq,der,muestras)
        fi = funcion(xi)
        # Linea suave
        muestraslinea = intervalos*10 + 1
        xk = np.linspace(izq,der,muestraslinea)
        fk = funcion(xk)
        # Graficando
        plt.plot(xk,fk, label ='f(x)')
        plt.plot(xi,fi, marker='o',
                color='orange', label ='muestras')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Integral: Regla de Simpson')
        plt.legend()


        plt.fill_between(xi,0,fi, color='g')
        for i in range(0,muestras,1):
            plt.axvline(xi[i], color='w')

        #plt.show()
        st.pyplot(plt, figsize=(2, 2)) 