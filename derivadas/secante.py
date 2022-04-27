import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from derivadas.derivadas import transformations

x = sp.Symbol('x')
def secante(f,xa,tolera):
    f = str(parse_expr(f,transformations=transformations))
    fx = sp.lambdify(x,f,'numpy')
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)