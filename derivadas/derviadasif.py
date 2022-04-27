import streamlit as st
from derivadas.derivadas import *
from plotterfuncion import plot_funcion

def derivadas_if():
    calc_derivadas = st.container()

    with calc_derivadas:
        col_eq,col_diff = st.columns([4,1])
        diff_variables = ''

        with col_eq:
            st.write('\n')
            st.write('\n')
            eq_funcion = st.text_input(
                #'Ingrese función: ', value='cos(xy) + 3x**3*y**-3 z**2 - sin(xz)')
                'Ingrese función: ', value='cos(x/4)sin(5x)')

        with col_diff:
            st.write('Derivada en:')
            tipo_diff = st.radio(
                '',
                ('Una variable','Varias varibales'))
            
            if tipo_diff == 'Una variable':
                diff_variables = st.selectbox(
                    'Diferenciar sobre:',
                    ('x','y','z','t','r','v','w'),
                )
            else:
                diff_variables = st.text_input('Respecto a qué variable derivar, y cuantas veces:',
                    value='x,2 ; y ; z ; z',
                    help='Utilice ; para separar argumentos, \n puede diferenciar n veces x y luego z asi: x,n;z')
                diff_variables = diff_variables.split(';')

        with st.expander(' ',True):
            st.subheader('Derivadas ')
            derivadas = derivadasFuncion(eq_funcion, *diff_variables)
            col_spc,col_expr,col_spc2 = st.columns(3)
            
            for dfdx in derivadas:
                col_expr.latex(f"{dfdx[0]} \quad = \quad {dfdx[1]}")

            st.subheader('Gráficas')
            lim_inf = int(st.number_input('x min:',min_value=-100,max_value=100,value=-8))
            lim_sup = int(st.number_input('y max:', min_value=-100,max_value=100, value=8))
            
            f_ltx = funcionOriginal(eq_funcion)
            st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])
            st.plotly_chart(plot_funcion(f_ltx[0], diff_variables,
                            lim_inf, lim_sup), use_container_width=True)

            plots = [plot_funcion(derivadas[i][2],diff_variables,lim_inf,lim_sup) for i in range(len(derivadas))]
            idx = 0
            intchr = r"'"
            for plot in plots:
                st.latex(f'f{intchr*(idx+1)}({diff_variables})\;=\;'+derivadas[idx][1])
                st.plotly_chart(plot, use_container_width=True)
                idx+=1
        
        #plot = plot_funcion('exp(x/3)*sin(x)')
        #st.plotly_chart(plot,use_container_width=True)
    return calc_derivadas