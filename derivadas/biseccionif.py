import streamlit as st
from derivadas.biseccion import biseccion
from plotterfuncion import plot_funcion
from sympy import lambdify, Symbol
import numpy as np
import sympy as sp
import math

from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def biseccion_if():
    value = 'sp.cos(x)-math.exp(-x**2) + 0.5'
    funcion = st.text_input('Ingrese la función f(x) :',value = value)
    x = Symbol('x')

    #funcion = lambdify(x,str(parse_expr(funcion, transformations=transformations)),'numpy')
    #lim_inf = lim_sup = 0
    
    izq,der = st.columns(2)
    
    with izq:
        xa = int(st.number_input('Cota inferior',
                      min_value=-50, max_value=50, value=-2))
    
    with der:                
        xb = int(st.number_input('Cota superior', min_value=-
                    50, max_value=50, value=3))
    tolerancia = int(st.number_input('Tolerancia : ',min_value=1,max_value=300,value = 7))
    
    def f(x):
        return eval(funcion)

    iter =0
    f_c = 999999

    while abs(f_c)>=tolerancia:
        puntoMedio = (xa + xb)/2
        f_a = f(xa)
        f_b = f(xb)
        f_c = f(puntoMedio)
        iter += 1
        st.write("xa:", xa,"xb: ", xb,"c: ", puntoMedio, "f_c: ", f_c, "N.iter: ", iter) 

        if (f_a * f_c)<0:
            xb = puntoMedio
        elif (f_b * f_c)<0:
            xa = puntoMedio

        if abs(f_c)<tolerancia:
            break
        
    st.write("La raiz buscada es: ", puntoMedio)