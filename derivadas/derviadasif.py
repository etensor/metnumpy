import streamlit as st
from derivadas.derivadas import *
from plotterfuncion import plot_funcion,graficador,definir_limites,plotter_principal


def derivadas_if():
    calc_derivadas = st.container()

    with calc_derivadas:
        eq_funcion,variables_f,_,_,col_diff = plotter_principal()
        diff_variables = ''
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
         

        with st.expander(' ',True):
            st.subheader('Derivadas ')

            derivadas = derivadasFuncion(eq_funcion, *diff_variables)
            col_spc,col_expr,col_spc2 = st.columns([0.2,4,0.2])
            
            for dfdx in derivadas:
                col_expr.latex(f"{sp.latex(dfdx[0])} \enskip = \enskip {sp.latex(dfdx[1])}")
            st.subheader('Gráficas')
            
            try:
                plots = [plot_funcion(derivadas[i][1],diff_variables,st.session_state['lim_inf'],st.session_state['lim_sup'],idx=i+1) for i in range(len(derivadas))]
                idx = 0
                intchr = r"'"
                for plot in plots:
                    st.latex(f'f{intchr*(idx+1)}({diff_variables})\;=\;'+sp.latex(derivadas[idx][1]))
                    st.plotly_chart(plot, use_container_width=True)
                    idx+=1
            except:
                st.warning('Depronto los parámetros de la función, o de la diferenciación no son correctos.')
        
        #plot = plot_funcion('exp(x/3)*sin(x)')
        #st.plotly_chart(plot,use_container_width=True)
    return calc_derivadas