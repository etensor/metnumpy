import plotly.graph_objects as go
import numpy as np
import sympy as sp
import pandas as pd
#import plotly.express as px
import streamlit as st
from derivadas.derivadas import funcionOriginal,parsearFuncion

# 3D: f(x,y) =  2y*cos(x/3)sin(3x)

x,y,z,t,w,r = sp.symbols('x y z t w r')

def hex_rgba(c_hex: str = '',opa=0):
    if c_hex == '':
        c_hex = st.session_state['b_color'].lstrip('#')
    else:
        c_hex = c_hex.lstrip('#')
    rgba_str = [*[int(c_hex[i:i+2], 16) + 8
                     for i in (0, 2, 4)],opa]
    return rgba_str      # hax que encontre por ahi, mucho visaje para darle transparencia al color de fondo... 
    

def pd_json(df):
    return df.to_json()


def graficador(eq_funcion,diff_variables):
    f_ltx = funcionOriginal(eq_funcion)
    st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])
    return st.plotly_chart(plot_funcion(f_ltx[0], diff_variables,
                st.session_state['lim_inf'], st.session_state['lim_sup']), use_container_width=True)



def graficador_3(eq_funcion,diff_variables):
    f_ltx = funcionOriginal(eq_funcion)
    st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])
    return st.plotly_chart(plot_funciones(f_ltx[0], diff_variables,
                                        st.session_state['lim_inf'],
                                        st.session_state['lim_sup']), 
                                        use_container_width=True)




def definir_limites():
    st.session_state['lim_inf'] = float(parsearFuncion(st.text_input(
       'x min:',value='-8.0')))
    st.session_state['lim_sup'] = float(parsearFuncion(st.text_input(
       'x max:', value='8.0')))







def plotter_principal(): # streamlit componente 
    col_eq, col_lims,col_ctrl = st.columns([2.5, 2, 2])
    with col_eq:
        st.write('\n')
        eq_funcion = st.text_input(
            #'Ingrese función: ', value='cos(xy) + 3x**3*y**-3 z**2 - sin(xz)')
            'Ingrese función: ', value='cos(x/4)sin(5x)')
        variables_f = st.text_input(
            'variables: ', value='x', help='Ingrese qué variables están en la función, separadas por coma.')


    with col_lims:
        st.write('\n')
        definir_limites()
        sola = st.checkbox('Gráfica sola', value=True,help='Con integral y derivada')

    try:
        if sola:
            graficador(eq_funcion, variables_f)
            with st.expander('Raices:'):
                # le agregué esto para conocer sus raices de una.
                try:
                    st.latex(
                    'x_r \;='+sp.latex(sp.solveset(parsearFuncion(eq_funcion), sp.symbols(variables_f))))
                except:
                    pass
        else:
            graficador_3(eq_funcion, variables_f)
    except:
        st.warning('No se pudo gráficar la función, revisa los parámetros ingresados.')

    return eq_funcion,variables_f,col_eq,col_lims,col_ctrl



def plot_funcion(f,diff_var=['x'],xa : float =-8.0,xb: float = 8.0,modo=True,auto_fondo= True,idx=0):  # funciona unicamente 2D]

    c_fondo = hex_rgba(opa=128)
   

    layoutF = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor= 'rgba('+','.join([str(c) for c in c_fondo]) + ')' if auto_fondo else '#AAAAAA',
        yaxis_title='f'+'\''*(idx)+f"({str(diff_var[0])})" if idx > 0 else f"f({str(diff_var[0])})",
        xaxis_title=str(diff_var[0]),
        yaxis_titlefont=dict(size=20),
        xaxis_titlefont=dict(size=20)
    )
    fig = go.Figure(layout=layoutF)
    
    if modo:
            f = sp.lambdify(sp.symbols(diff_var), f, 'numpy')     # ya recibe simbolos
    

    if len(diff_var) == 3:
        xs = np.outer(np.linspace(xa, xb, 200), np.ones(200))
        y = xs.copy().T
        Z = f(xs, y)
        fig.add_trace(go.Surface(
            contours={
                "x": {"show": True, "start": 1.5, "end": 2, "size": 0.03, "color": "white"},
                "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.04}
            },
            x=xs,
            y=y,
            z=Z
            ))

        fig.update_layout(
            scene={
                "xaxis": {"nticks": 12},
                "zaxis": {"nticks": 12},
                'camera_eye': {"x": -1, "y": -1, "z": 0.5},
                "aspectratio": {"x": 1, "y": 1, "z": 0.5}
            })

    if len(diff_var) == 5:
        X,Y,Z =  np.mgrid[xa:xb:30j,xa:xb:30j,xa:xb:30j]

        fig.add_trace(go.Volume(
            x=X.flatten(),
            y=Y.flatten(),
            z=Z.flatten(),
            value=f(X,Y,Z).flatten(),
            isomin=0.1,
            isomax=0.8,
            opacity=0.35,
            surface_count=30
        ))



    if len(diff_var) == 1:
        xs = np.linspace(xa, xb, 650)
        df = pd.DataFrame(
            dict(
                x=xs,
                y=f(xs)
            )
        )
    # rename para darle label de la variable que usa.
        df[f'{diff_var[0]}'] = df.pop('x')
        
        fig.update_layout(
            margin=dict(t=16),
        )
    
        fig.add_trace(go.Scatter(
            #ez:  x=t, y=np.sin(t), ...
            x=df.loc[:, f'{diff_var[0]}'],
            y=df.loc[:, 'y'],
            marker_color=st.session_state['p_color'],
            mode='lines',
            line=dict(width=3)
        ))

    return fig




def plot_funciones(f, diff_var=['x'], xa: float = -8.0, xb: float = 8.0, modo=True, auto_fondo=True, idx=0):

    c_fondo = hex_rgba(opa=128)

    layoutF = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba('+','.join([str(c) for c in c_fondo]
                                      ) + ')' if auto_fondo else '#AAAAAA',
        xaxis_title=str(diff_var[0]),
        yaxis_titlefont=dict(size=20),
        xaxis_titlefont=dict(size=20)
    )
    fig = go.Figure(layout=layoutF)

    if modo:
        # ya recibe simbolos
        dfdx = sp.lambdify(*diff_var,sp.diff(f,*diff_var),'numpy')
        F = sp.lambdify(*diff_var,sp.integrate(f,sp.symbols(diff_var[0])),'numpy')
        f = sp.lambdify(*diff_var, f, 'numpy')
        
        

    xs = np.linspace(xa, xb, 600)

    # Datos -> tabla para la gráfica
    df = pd.DataFrame(
        dict(
            x=xs,
            y=f(xs),
            integral=F(xs),
            derivada=dfdx(xs)
        )
    )
    # rename para darle label de la variable que usa.
    df[f'{diff_var[0]}'] = df.pop('x')
    # tocara validar cada argumento ? <== espera orden x,y?

    fig.update_layout(
        margin=dict(t=16),
    )

    fig.add_trace(go.Scatter(
        x=df.loc[:, f'{diff_var[0]}'],
        y=df.loc[:, 'integral'],
        marker_color=st.session_state['p_color'],
        mode='lines',
        line=dict(width=2),
        name=f'F({diff_var[0]})',

    ))
    fig.add_trace(go.Scatter(
        x=df.loc[:, f'{diff_var[0]}'],
        y=df.loc[:, 'derivada'],
        #marker_color="",
        mode='lines',
        line=dict(width=2),
        name=f'f\'({diff_var})',
    ))
    fig.add_trace(go.Scatter(
        x=df.loc[:, f'{diff_var[0]}'],
        y=df.loc[:, 'y'],
        #marker_color=st.session_state['p_color'],
        mode='lines',
        line=dict(width=2),
        name=f'f({diff_var[0]})',
    ))
    
    #st.session_state['df_plots'] = df

    return fig
