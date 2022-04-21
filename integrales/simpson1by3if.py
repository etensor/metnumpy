from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
import sympy as sp
from simpson1by3 import empezar
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def simpson1by3_if():
    funcion = ''
    x = sp.Symbol('x')
    #function = st.text_input("Ingresa la función")
    function = st.text_input('Ingrese la función',
                                value='')
    izq = int(st.slider('Limite izquierdo', min_value=0, max_value=25, value = 0))
    der = int(st.slider('Limite derecho', min_value=0, max_value=25, value = 0))
    intervalos = int(st.number_input('Numero de intervalos',min_value=2,max_value=30, value = 2))

    if function != "":
        function = str(parse_expr(function,transformations=transformations))
        funcion = sp.lambdify(x,function,'numpy')

    if intervalos % 2 != 0:
        st.write('El numero de intervalos no debe ser impar')
        confirmar = False
    else:
        confirmar = True

    if izq >= der:
        st.write('El limite izquierdo no puede ser mayor al derecho')
        pasar = False
    else:
        pasar = True
    
    if confirmar and pasar and function != '':
        resultado = empezar(function, izq, der, intervalos)

        st.success(f'Valor integral definido: {resultado}')

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