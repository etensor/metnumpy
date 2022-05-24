import streamlit as st
from sympy import *
import sympy as sp
from math import *
from sympy.parsing.sympy_parser import parse_expr
from derivadas.derivadas import transformations
from integrales.newthonr import root

def netwon_st():
  x = sp.Symbol('x')
  f = st.text_input('Ingrese la funcion f(x)',value='(x**3)+(3*x**2)+(12*x+8)')
  df=sp.diff(f)
  f=sp.lambdify(x,f)
  df=sp.lambdify(x,df)
  
  x0 = int(st.text_input('x0',value='-5'))
  tol = float(st.text_input('Tolerancia',value='0.0001'))
  root(f,df,x0,tol)   