import streamlit as st
from derivadas.biseccion import biseccion
from plotterfuncion import plot_funcion
from sympy import lambdify, Symbol
import numpy as np

from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def biseccion_if():
    value = 'cos(x)-exp(-x**2) + 0.5'
    funcion = st.text_input('Ingrese la función f(x) :',value = value)
    x = Symbol('x')

    funcion = lambdify(x,str(parse_expr(funcion, transformations=transformations)),'numpy')
    lim_inf = lim_sup = 0
    
    izq,der = st.columns(2)
    
    with izq:
        lim_inf = int(st.number_input('Rango inferior',
                      min_value=-50, max_value=50, value=-2))
    
    with der:                
        lim_sup = int(st.number_input('Rango superior', min_value=-
                    50, max_value=50, value=3))
    iter_max = int(st.number_input('Cuantas iteraciones? : ',min_value=1,max_value=300,value = 7))
    
    #raiz_biseccion = biseccion(eval('lambda x: '+funcion),lim_inf,lim_sup,20)
    raiz_biseccion = biseccion(funcion , lim_inf, lim_sup, iter_max)

    
    st.write(raiz_biseccion)
    st.subheader('Gráfica')
    plot = plot_funcion(funcion,
                        'x', lim_inf, lim_sup, modo=False)
    st.plotly_chart(plot)