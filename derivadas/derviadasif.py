import streamlit as st
from derivadas.derivadas import *
from plotterfuncion import plot_funcion,graficador,definir_limites,plotter_principal

def derivadas_if(eq_funcion,col_diff):
    calc_derivadas = st.container()
    varias_var = False

    with calc_derivadas:
        #eq_funcion,variables_f,_,_,col_diff = plotter_principal()
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
                diff_variables = st.text_input('Respecto a qué variables derivar:',
                    value='x,x,y',
                    help='x,x,z <-- derivará 2 veces en x y una vez en z')
                diff_variables = diff_variables.split(',')
                varias_var = True

        st.write('\n')
         

        with st.expander(' ',True):
            st.subheader('Derivadas ')

            derivadas = derivadasFuncion(eq_funcion, *diff_variables)
            col_spc,col_expr,col_spc2 = st.columns([0.1,4,0.1])
            
            for dfdx in derivadas:
                col_expr.latex(f"{sp.latex(dfdx[0])} \enskip = \enskip {sp.latex(dfdx[1])}")
            st.subheader('Gráficas')

            # peor alternativa pero más segura.
            plots = []
            idx = 0
            for f in derivadas:
                try:
                    plots.append(
                        plot_funcion(
                            f[1],st.session_state['variables_f'],
                            st.session_state['lim_inf'],
                            st.session_state['lim_sup'],
                            idx=idx
                        )
                    )
                except:
                    break
                idx += 1

            #plots = [plot_funcion(
            #derivadas[i][1],
            #st.session_state['variables_f'],
            #    st.session_state['lim_inf'],st.session_state['lim_sup'],
            #    idx=i) for i in range(len(derivadas))]


            idx = 0
            intchr = r"'"
            for plot in plots:
                try:
                    st.latex(f'f{intchr*(idx+1)}({st.session_state["variables_f"]})\;=\;'+sp.latex(derivadas[idx][1]))
                    st.plotly_chart(plot, use_container_width=True)
                except:
                    st.warning('La función no se puede gráficar ahora, \
                    puede que los paramétros de la función o de diferenciación no sean correctos.')
                idx+=1
            

    return calc_derivadas