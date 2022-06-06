import streamlit as st
from derivadas.derivadas import derivadasFuncion,parsearFuncion
import sympy as sp
from plotterfuncion import plot_funcion #, graficador, definir_limites, plotter_principal


### derivadas_if recibe la funcion, pero lo interesante esta
## en que recibe la columna col_diff que le da los controles especificos
## para derivadas. El componente del graficador está constuituido por 3 columnas
### La últoma libre, sirve para las variables especificas del método en el menu.


def derivadas_if(eq_funcion, col_diff):
    calc_derivadas = st.container()

    with calc_derivadas:
        #eq_funcion,variables_f,_,_,col_diff = plotter_principal()

        diff_variables = ''
        with col_diff:
            st.write('Derivada en:')

            tipo_diff = st.radio(
                '',
                ('Las 3 primeras derivadas',)
                    if len(st.session_state['variables_f']) == 1 \
                    else ('Una variable una vez', 'Varias variables'),
            help=r'''Si $f: \Reals^{n} \rightarrow \Reals^{m}\;$ \
                y $ n \geq 2 $, ralentiza el proceso sacar las 3 gráficas.
                La calculadora grafica $f$ dado que $ m \leq 3 $.'''
            
            )

            if tipo_diff in ('Las 3 primeras derivadas','Una variable una vez'):
                diff_variables = st.selectbox(
                    'Diferenciar sobre:',
                    ('x', 'y', 'z', 't', 'r', 'v', 'w'),
                )
            else:
                diff_variables = st.text_input('Respecto a qué variables derivar:',
                                               value='x,x,y',
                                               help='x,x,z <-- derivará 2 veces en x y una vez en z, en ese orden.')
                diff_variables = diff_variables.split(',')

        st.write('\n')

        with st.expander(' ', True):
            st.subheader('Derivadas ')

            derivadas = derivadasFuncion(eq_funcion, *diff_variables)
            col_spc, col_expr, col_spc2 = st.columns([0.1, 4, 0.1])

            for dfdx in derivadas:
                col_expr.latex(
                    f"{sp.latex(dfdx[0])} \enskip = \enskip {sp.latex(dfdx[1])}")
            st.subheader('Gráficas')


            # peor alternativa pero más segura (llega hasta donde pueda graficar)
            plots = []
            idx = 0
            
            for fdxn in derivadas:
                try:
                    plots.append(
                        plot_funcion(
                            fdxn[1], st.session_state['variables_f'],
                            st.session_state['lim_inf'],
                            st.session_state['lim_sup'],
                            idx=idx
                        )
                    )
                    idx += 1
                except:
                    break
                

            # plots = [plot_funcion(
            # derivadas[i][1],
            # st.session_state['variables_f'],
            #    st.session_state['lim_inf'],st.session_state['lim_sup'],
            #    idx=i) for i in range(len(derivadas))]

            idx = 0
            intchr = r"'"
            for plot in plots:
                try:
                    st.latex(
                        f'f{intchr*(idx+1)}({st.session_state["variables_f"]})\;=\;'+sp.latex(derivadas[idx][1]))
                    if diff_variables == 'z':
                        st.pyplot(plot, use_container_width=True)
                    else:
                       st.plotly_chart(plot, use_container_width=True)
                except:
                    st.warning('La función no se puede gráficar ahora, \
                    puede que los paramétros de la función o de diferenciación no sean correctos.')
                idx += 1

    return calc_derivadas
