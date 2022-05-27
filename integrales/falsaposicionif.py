import streamlit as st
from integrales.falsaposicion import falsa_pos

def falsa_posicion_if():
    st.markdown('Nota: Ingresa la funcion, rangos (inferior, superior) y tolerancia.')
    funcion = st.text_input('Ingrese la función',
                            value='exp(x-2)-log(x) -2.5')
    a = int(st.text_input('Ingrese rango inferior: ',value='3'))
    b = int(st.text_input('Ingrese rango superior: ',value='4'))
    tol = float(st.text_input('Ingrese tolerancia:', value='0.0005'))

    tabla,raices = falsa_pos(funcion,a,b,tol)
    st.write('Acerca:')
    col_expr, col_vals = st.columns(2)
    
    col_expr.latex(r'x_{a}')
    col_vals.write('\n')
    col_vals.write(' limite inferior')
    col_expr.latex(r'x_{b}')
    col_vals.write('\n')
    col_vals.write(' limite superior')
    col_expr.latex(r'x_{r}')
    col_vals.write('\n')
    col_vals.write(' raiz encontrada')
    
 
    for i in range(0, len(tabla)):
        st.write('------------------------------------------------------')
        col_expr.write(f'Iteración #: {i+1} ')
        col_expr.latex(r'x_{a},x_{r},x_{b}')
        col_expr.write('\n')
        col_expr.write('\n')
        col_expr.write('\n')
        col_vals.write(tabla[i, 0:3])
        col_expr.write('\n')
        col_expr.latex(r'f(x_{a}),f(x_{c}), f(x_{b}): ')
        col_expr.write('\n')
        col_vals.write(tabla[i, 3:6])
        col_expr.write('\n')
        col_expr.write('\n')
        col_expr.markdown(
            "<h6 style='text-align: center; color: Green;'>Raíz</h6>", unsafe_allow_html=True)
        col_expr.markdown(
            "<h6 style='text-align: center; color: Green;'>Error</h6>", unsafe_allow_html=True)
        col_vals.write(raices[i])
        col_vals.write(tabla[i,6])