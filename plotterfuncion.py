import plotly.graph_objects as go
import numpy as np
import sympy as sp
import pandas as pd
#import plotly.express as px
import streamlit as st
from derivadas.derivadas import funcionOriginal,parsearFuncion

x,y,z,t,w,r = sp.symbols('x y z t w r')

def hex_rgba(c_hex: str = '',opa=0):
    if c_hex == '':
        c_hex = st.session_state['b_color'].lstrip('#')
    else:
        c_hex = c_hex.lstrip('#')
    rgba_str = [*[int(c_hex[i:i+2], 16) + 8
                     for i in (0, 2, 4)],opa]
    return rgba_str      # hax que encontre por ahi, mucho visaje para darle transparencia al color de fondo... 
    

def graficador(eq_funcion,diff_variables):
    f_ltx = funcionOriginal(eq_funcion)
    st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])
    return st.plotly_chart(plot_funcion(f_ltx[0], diff_variables,
                st.session_state['lim_inf'], st.session_state['lim_sup']), use_container_width=True)


def definir_limites():
    st.session_state['lim_inf'] = float(parsearFuncion(st.text_input(
       'x min:',value='-8.0')))
    st.session_state['lim_sup'] = float(parsearFuncion(st.text_input(
       'x max:', value='8.0')))


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
            
    
    xs = np.linspace(xa, xb, 600)
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
    ))

    return fig

    #return fig


'''
    xs = np.arange(-1,3,0.01)
    # Add traces, one for each slider step
    for step in np.arange(-2, 2, 0.1):
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#0dc40c", width=3),
                name="𝜈 = " + str(step),
                x=np.arange(-10, 10, 0.01),
                y=f(step * xs)))

    # Make 10th trace visible
    fig.data[10].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)}]#,
                #{"title": "Slider switched to step: " + str(i)}],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Rango: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

'''
