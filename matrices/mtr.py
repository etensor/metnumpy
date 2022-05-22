import numpy as np
import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations +
                   (implicit_multiplication_application,))



def mtr_nm(n,m):
    return np.array([[x for x in range(n)] for y in range(m)])

def tex_mtr(mtr_str='',sym='A'):
    mtr = sp.Matrix(parse_expr(mtr_str))
    return str(f'{sym} \;= '+sp.latex(mtr))



def equacion(expr,evaluar=False):
    return st.latex(sp.latex(expr)) \
        if not evaluar else st.latex(sp.latex(parse_expr(expr)))


def def_mtr(n=1,m=0):
    opcion = st.selectbox('Seleccione una opción', 
    [
        'Sumar matrices',
        'Restar matrices',
        'Multiplicar matrices',
        'Producto Hadamard'
    
    ])

    operaciones = [
        lambda x,y: x+y, 
        lambda x,y: x-y, 
        lambda x,y: x*y
        ]
    
    st.markdown(
        'Nota: El número de columnas de la matriz A debe ser igual al número de filas de la matriz B')
    
    st.markdown('Ingrese la matriz de la forma:')
    st.markdown('[[a11,a12,a13,...],[a21,a22,a23,...],[a31,a32,a33,...]]')

    st.markdown('Ejemplo: [[1,2,3],[4,5,6]]')

    A_col,B_col = st.columns(2)

    A_col.subheader('Matriz A')
    
    mtr_A = A_col.text_input('Ingrese A:', '[[a,b],[c,d]]')

    #dimA_n,dimA_m = A_col.columns(2)

    #a_n = int(dimA_n.text_input('Ingrese dimensiones n x m', '2'))
    #a_m = int(dimA_m.text_input('Ingrese dimensiones n x m', '3'))
    A = sp.Matrix(parse_expr(mtr_A))
    A_col.latex(tex_mtr(mtr_A))

    B_col.subheader('Matriz B')
    mtr_B = B_col.text_input('Ingrese B:', '[[e,f],[g,h]]')
    B = sp.Matrix(parse_expr(mtr_B))
    B_col.latex(tex_mtr(mtr_B,'B'))
    

    if opcion == 'Sumar matrices':
        st.subheader('Sumar matrices')
        st.latex('A+B \enskip = \enskip '+sp.latex(operaciones[0](A, B)))
    
    if opcion == 'Restar matrices':
        st.subheader('Restar matrices')
        st.latex('A-B \enskip = \enskip '+sp.latex(operaciones[1](A, B)))
    
    if opcion == 'Multiplicar matrices':
        st.subheader('Multiplicar matrices')
        #st.latex(sp.latex(operaciones[2](A, B)))
        st.latex('A \cdot B \enskip = \enskip '+sp.latex(operaciones[2](A, B)))
    
    if opcion == 'Producto Hadamard':
        st.subheader('Producto Hadamard')
        st.latex('A \circ B \enskip = \enskip ' +
                 sp.latex(sp.matrix_multiply_elementwise(A, B)))
        
        with st.expander('Más sobre Hadamard'):
           
            st.write('A diferencia de la multiplicación de matrices, \
                el producto Hadamard requiere que sean de las mismas dimensiones \
                los objetos.')

            st.write('En los vectores se nota más su efecto, uno produce un escalar,\
                 hamadard otro vector del mismo tamaño, como multiplicar cada elemento por un escalar distinto.')
            st.latex(r'''
            c = \vec{x}^T \cdot \vec{y} =
        \begin{bmatrix}
               x_{1} \\
               x_{2} \\
               \vdots \\
               x_{n}
             \end{bmatrix}^T \cdot \begin{bmatrix}
               y_{1} \\
               y_{2} \\
               \vdots \\
               y_{n}
             \end{bmatrix} =
        x_1, x_2, \cdots, x_n] \cdot \begin{bmatrix}
               y_{1} \\
               y_{2} \\
               \vdots \\
               y_{n}
             \end{bmatrix} = \sum_{i=1}^n x_iy_i \in \mathbb{R}
            ''')
            st.latex(r'''\vec{z} = \vec{x} \odot \vec{y} =
            \begin{bmatrix}
               x_{1} \\
               x_{2} \\
               \vdots \\
               x_{n}
             \end{bmatrix} \odot \begin{bmatrix}
               y_{1} \\
               y_{2} \\
               \vdots \\
               y_{n}
             \end{bmatrix} =  \begin{bmatrix}
               x_1y_{1} \\
               x_2y_{2} \\
               \vdots \\
               x_ny_{n}
             \end{bmatrix} \in \mathbb{R}^n

            ''')


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