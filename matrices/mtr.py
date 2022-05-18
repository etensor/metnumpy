import numpy as np
import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations +
                   (implicit_multiplication_application,))



def mtr_nm(n,m):
    return np.array([[x for x in range(n)] for y in range(m)])


def def_mtr(n=1,m=0):
    opcion = st.selectbox('Seleccione una opción', 
    [
        'Sumar matrices',
        'Restar matrices',
        'Multiplicar matrices',
        'Dividir matrices',
    
    ])

    operaciones = [
        lambda x,y: x+y, 
        lambda x,y: x-y, 
        lambda x,y: x*y, 
        lambda x,y: x/y
        ]
    
    st.markdown(
        'Nota: El número de columnas de la matriz A debe ser igual al número de filas de la matriz B')
    
    st.markdown(
        'Ingrese la matriz de la forma: [[a11,a12,a13,...],[a21,a22,a23,...],[a31,a32,a33,...]]')
    st.latex(sp.Matrix([['a11', 'a12', 'a13', '...'], [
            'a21', 'a22', 'a23','...'], ['a31', 'a32', 'a33', '...']]))

    st.markdown('Ejemplo: [[1,2,3],[4,5,6]]')

    A_col,B_col = st.columns(2)

    A_col.subheader('Matriz A')

    

    
    

    n = st.number_input('Ingrese el número de filas', value=1)
    m = st.number_input('Ingrese el número de columnas', value=1)

    if opcion == 'Sumar matrices':
        st.subheader('Sumar matrices')
        a = mtr_nm(n,m)
        b = mtr_nm(n,m)
        st.write(a)
        st.write(b)
        st.write(operaciones[0](a,b))
    
    if opcion == 'Restar matrices':
        pass









#def def_mtr():
#    #dims = int(st.text_input('Dimensiones matriz n x n '),value='3')
#    dims = int(input('dimensiones matriz n x n '))
#
#    nums = [x for x in range(9)]
#    mtr = np.array(nums).reshape((3,3))
#    mtr2 = np.array(nums[::-1]).reshape((3,3))
#    print(mtr, mtr2, sep='\n\n')
#    mul = mtr*mtr2
#    mul_2 = np.matmul(mtr,mtr2,)
#    suma = mtr+mtr2
#    print(f'mul: {mul}\n,{mul_2},\n{suma}')
#
#
#
#def_mtr()