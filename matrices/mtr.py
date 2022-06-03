import numpy as np
import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

from derivadas.derivadas import parsearFuncion
transformations = (standard_transformations +
                   (implicit_multiplication_application,))



def mtr_nm(n,m):
    return np.array([[x for x in range(n)] for y in range(m)])

def tex_mtr(mtr_str='',sym='A'):
    mtr = sp.Matrix(parse_expr(mtr_str))
    return str(f'{sym} \;= '+sp.latex(mtr))



def equacion(expr,evaluar=False) -> st.latex:
    return st.latex(sp.latex(expr)) \
        if not evaluar else st.latex(sp.latex(parse_expr(expr)))


# otra interfaz para crear una matriz

def crear_matriz(sym : str ='A'):
    st.markdown('---')
    _, filas, columnas, _ = st.columns([0.5, 3, 3, 0.5])

    st.markdown('Ingrese matriz:')
    st.latex(sym)
    with filas:
        n_filas = int(st.text_input(
            f'Ingrese el número de filas de la matriz {sym}', '3'))

    with columnas:
        n_columnas = int(st.text_input(
            f'Ingrese el número de columnas de la matriz {sym}', '3'))

    columnas_mtr = st.columns(n_columnas)

    mtr_a = [[(i,j,sym) for j in range(n_columnas)] for i in range(n_filas)]

    idx = 0
    idy = 0
    for col in columnas_mtr:
        with col:
            for _ in range(n_filas):
                mtr_a[idy][idx] = parsearFuncion(
                    st.text_input('', '0', key=mtr_a[idy][idx]))
                idy += 1
        idy = 0
        idx += 1
    
    return mtr_a





def def_mtr(n=1,m=0):
    lineal_o_no = True

    opcion = st.selectbox('Seleccione una opción', 
    [
        'Sumar matrices',
        'Restar matrices',
        'Multiplicar matrices',
        'Producto Hadamard',
        'Determinante e Inversa',
        'Espacio Columna y Nulo',
        'Sistemas de Ecuaciones',
    
    ])

    operaciones = [
        lambda x,y: x+y, 
        lambda x,y: x-y, 
        lambda x,y: x*y
        ]
    
    if opcion == 'Sistemas de Ecuaciones':
        lineal_o_no = st.checkbox('¿Es un sistema lineal?', 
            value=True,help='Si el sistema no es lineal, se ingresa distinto.')


    if not lineal_o_no:
        num_e,vars_s = st.columns(2)
        with num_e:
            n_ecuaciones = st.number_input('Ingrese el número de ecuaciones',
            min_value=0,max_value=8,value=2)
        with vars_s:  
            variables = sp.symbols(st.text_input('Ingrese las variables', 'x,y',
            help='Separadas por coma, las variables en el sistema.'))
        ecuaciones = [0 for i in range(n_ecuaciones)]
        ejemplo_sistema = ['xy-1', ' 4*x**2 + y**2 - 5']

        for i in range(n_ecuaciones):
            ecuaciones[i] = parsearFuncion(st.text_input(f'Ingrese la ecuación {i+1}',
            value=ejemplo_sistema[i] if n_ecuaciones == 2 else ecuaciones[i]))
        
        st.markdown('---')
        st.markdown('Solución:')
        st.latex(sp.latex(sp.Matrix(variables))+'\enskip = \enskip'+sp.latex(sp.nonlinsolve(ecuaciones,variables)))
        
        return
    
    
    input_matriz = st.radio('Cómo ingresar la matriz',
        ('Ingresar manualmente','Ingresar desde una lista')
    )


    if input_matriz == 'Ingresar manualmente':
        mtr_A = crear_matriz('A')
        mtr_B = crear_matriz('B')

        A = sp.Matrix(mtr_A)
        B = sp.Matrix(mtr_B)

   
    if input_matriz == 'Ingresar desde una lista':
    
        st.markdown(
            'Nota: El número de columnas de la matriz A debe ser igual al número de filas de la matriz B')

        st.markdown('Ingrese la matriz de la forma:')
        st.markdown('[[a11,a12,a13,...],[a21,a22,a23,...],[a31,a32,a33,...]]')

        st.markdown('Ejemplo: [[1,2,3],[4,5,6]]')
        st.info('Si A es de dimensiones n x m, B espera ser m x k.')

        A_col, B_col = st.columns(2)
        A_col.subheader('Matriz A')
        B_col.subheader('Matriz B')
        mtr_A = A_col.text_input(
            'Ingrese A:', '[[t1,t2,t3],[u,v,w],[x,y,z]]')
        mtr_B = B_col.text_input('Ingrese B:', '[[e,f,g],[h,r,p],[q,V,k]]')

        A = sp.Matrix(parse_expr(mtr_A))
        B = sp.Matrix(parse_expr(mtr_B))


    if opcion != 'Sistemas de Ecuaciones':

        if input_matriz == 'Ingresar manualmente':
            _,A_col, B_col,_ = st.columns([1,3,3,1])
            A_col.latex('A \;=\; '+sp.latex(A))
            B_col.latex('B \;=\; '+sp.latex(B))
        else:
            A_col.latex(tex_mtr(mtr_A))
            B_col.latex(tex_mtr(mtr_B, 'B'))
        


    if opcion == 'Sumar matrices':
        st.subheader('Sumar matrices')
        if B.shape[1] != A.shape[0] or B.shape[0] != A.shape[1]:
            st.error('Las dimensiones de las matrices no coinciden')
            pass
        else:
            st.latex('A+B \enskip = \enskip '+sp.latex(operaciones[0](A, B)))

    if opcion == 'Restar matrices':
        st.subheader('Restar matrices')
        if B.shape[1] != A.shape[0] or B.shape[0] != A.shape[1]:
            st.error('Las dimensiones de las matrices no coinciden')
            pass
        else:
            st.latex('A-B \enskip = \enskip '+sp.latex(operaciones[1](A, B)))
    
    if opcion == 'Multiplicar matrices':
        st.subheader('Multiplicar matrices')
        if B.shape[0] != A.shape[1]:
            st.error('Las dimensiones de las matrices no coinciden')
            pass
        else:
            st.latex('A \cdot B \enskip = \enskip '+sp.latex(operaciones[2](A, B)))
    

    if opcion == 'Determinante e Inversa':

        st.subheader('Inversa')
        try:
            st.latex('A^{-1} \enskip = \enskip '+sp.latex(A.inv()))
            st.latex('B^{-1} \enskip = \enskip '+sp.latex(B.inv()))
        except:
            st.error('Matriz no invertible')

        st.subheader('Determinante de una matriz')
        st.latex('det\,A \enskip = \enskip '+sp.latex(A.det()))
        st.latex('det\,B \enskip = \enskip '+sp.latex(B.det()))
        st.markdown('---')
        st.write('La determinante de un producto de matrices es igual a la multiplicación de sus determinantes')
        st.latex('det(AB) \enskip = \enskip '+sp.latex((A*B).det()))
        st.latex('det(A) \cdot det(B) \enskip = \enskip '+sp.latex(A.det()*B.det()))



    if opcion == 'Espacio Columna y Nulo':
        st.subheader('Espacio Nulo de una matriz')
        st.latex('N(A) \enskip = \enskip '+sp.latex(A.nullspace()))
        st.latex('C(A) \enskip = \enskip '+sp.latex(A.columnspace()))

        with st.expander('Más sobre espacio nulo:'):
            st.write('Definición')
            st.markdown(r'''Sea $T:V\rightarrow W $ una transformación lineal.''')
            st.markdown(r'''
            El núcleo, kernel o espanio nulo de $T$ es el conjunto de vectores en $V$ 
            que terminan en 0 de $W$ al pasar por $T$. Es decir,
            $$
                N(T) = \{v \in V : T(v) = 0\}
            $$
            
            ''')


    if opcion == 'Producto Hadamard':
        st.subheader('Producto Hadamard')
        
        if A.shape != B.shape:
            st.error('Las dimensiones de las matrices no coinciden')
        else:
            try:
                st.latex('A \circ B \enskip = \enskip ' +
                 sp.latex(sp.matrix_multiply_elementwise(A, B)))
            except:
                st.info('Si una matriz contiene simbolos y la otra solo números,\
                     el producto falla (no debería)')
                st.success('Solución: Agregar un simbolo cualquiera a la matriz \
                        que no contenga simbolos')
        
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


def resolver_sistema(A,B):
    st.markdown('---')
    st.markdown('Sistema:')
    syms_dims = sp.symbols(
        ','.join([f'x_{i+1}' for i in range(A.shape[1])]))
    st.latex('Ax\;=\;b')
    st.latex(sp.latex(A*sp.Matrix(syms_dims)) +
            '\enskip = \enskip '+sp.latex(B))

    metodo = st.selectbox('Cómo quiere resolver el sistema',
                            ['Solución y ya', 'Gauss Jordan', 'Factorización LU'])

    if metodo == 'Solución y ya':
        st.latex('x \enskip = \enskip ' +
                    sp.latex(sp.linsolve((A, B), syms_dims)))

    if metodo == 'Gauss Jordan':
        st.latex('x\;=\;A^{-1}b')
        try:
            sols = A.gauss_jordan_solve(B)
            st.latex('x \; = \;' + sp.latex(A.inv()*B))
            if sols[1].shape[0] != 0:
                st.latex('x \; = \;'+sp.latex(sols))
        except:
            st.error('Matriz no invertible')

    if metodo == 'Factorización LU':
        try:
            st.latex(f'x = {sp.latex(A.LUsolve(B))}')
        except:
            st.error('Matriz no invertible')






