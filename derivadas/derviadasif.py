import streamlit as st
from derivadas.derivadas import *
from plotterfuncion import plot_funcion,graficador,definir_limites
from sympy import latex

def derivadas_if():
    calc_derivadas = st.container()

    with calc_derivadas:
        col_eq,col_lims,col_diff = st.columns([2.5,2,2])
        diff_variables = ''

        with col_eq:
            st.write('\n')
            eq_funcion = st.text_input(
                #'Ingrese función: ', value='cos(xy) + 3x**3*y**-3 z**2 - sin(xz)')
                'Ingrese función: ', value='cos(x/4)sin(5x)')
            variables_f  = st.text_input('variables: ', value='x',help='Ingrese qué variables están en la función,separadas por coma.')
        
        with col_lims:
            definir_limites()

        with col_diff:
            st.write('Derivada en:')
            tipo_diff = st.radio(
                '',
                ('Una variable','Varias variables'))
            
            if tipo_diff == 'Una variable':
                diff_variables = st.selectbox(
                    'Diferenciar sobre:',
                    ('x','y','z','t','r','v','w'),
                )
            else:
                diff_variables = st.text_input('Respecto a qué variable derivar, y cuantas veces:',
                    value='x,2 ; y ; z ; z',
                    help='x,2 ; y <-- Derivará dos veces en x, luego una en y.')
                diff_variables = diff_variables.split(';')


        st.write('\n')
        try:
            graficador(eq_funcion,variables_f)
        except:
            st.warning('No se pudo gráficar la función, revisa los parámetros ingresados.')

        with st.expander(' ',True):
            st.subheader('Derivadas ')

            derivadas = derivadasFuncion(eq_funcion, *diff_variables)
            col_spc,col_expr,col_spc2 = st.columns([0.2,4,0.2])
            
            for dfdx in derivadas:
                col_expr.latex(f"{latex(dfdx[0])} \quad = \quad {latex(dfdx[1])}")
            st.subheader('Gráficas')
            
            try:
                plots = [plot_funcion(derivadas[i][1],diff_variables,st.session_state['lim_inf'],st.session_state['lim_sup'],idx=i+1) for i in range(len(derivadas))]
                idx = 0
                intchr = r"'"
                for plot in plots:
                    st.latex(f'f{intchr*(idx+1)}({diff_variables})\;=\;'+latex(derivadas[idx][1]))
                    st.plotly_chart(plot, use_container_width=True)
                    idx+=1
            except:
                st.warning('Depronto los parámetros de la función, o de la diferenciación no son correctos.')
        
        #plot = plot_funcion('exp(x/3)*sin(x)')
        #st.plotly_chart(plot,use_container_width=True)
    return calc_derivadas