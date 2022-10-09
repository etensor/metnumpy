import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import sympy as sp
import pandas as pd
# import plotly.express as px
import streamlit as st
from derivadas.derivadas import funcionOriginal, parsearFuncion
import cplot
import matplotlib.pyplot as plt


# 3D: f(x,y) =  2y*cos(x/3)sin(3x)


x, y, z, t, w, r = sp.symbols('x y z t w r')


def hex_rgba(c_hex: str = '', opa=0):
    if c_hex == '':
        c_hex = st.session_state['b_color'].lstrip('#')
    else:
        c_hex = c_hex.lstrip('#')
    rgba_str = [*[int(c_hex[i:i+2], 16) + 8
                     for i in (0, 2, 4)], opa]
    # hax que encontre por ahi, mucho visaje para darle transparencia al color de fondo...
    return rgba_str


def pd_json(df):
    return df.to_json()


# CACHE

# @st.cache(suppress_st_warning=True)

# @st.experimental_memo(suppress_st_warning=True)
def graficador(eq_funcion, diff_variables):
    f_ltx = funcionOriginal(eq_funcion)
    st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])

    if diff_variables != 'z':
        return st.plotly_chart(
            plot_funcion(f_ltx[0], diff_variables,
                    st.session_state['lim_inf'], st.session_state['lim_sup'],
                    template=st.session_state['tema_plots']),
            use_container_width=True)
    else:
        return st.pyplot(plot_funcion(
                    f_ltx[0],
                    diff_variables,
                    st.session_state['lim_inf'],
                    st.session_state['lim_sup'],
                    ),
                use_container_width=True)


def graficador_3(eq_funcion, diff_variables):
    f_ltx = funcionOriginal(eq_funcion)
    st.latex(f'f({diff_variables})\;=\;' + f_ltx[1])

    return st.plotly_chart(
        plot_funciones(f_ltx[0], diff_variables,
                st.session_state['lim_inf'],
                st.session_state['lim_sup'],
                template=st.session_state['tema_plots']),
                use_container_width=True)


def graficador_complex(eq_funcion):
    func_z = sp.lambdify('z', eq_funcion, 'numpy')
    zplot, ax = plt.subplots(clear=True)  # ,sharey=True)
    ax = cplot.plot(func_z,
    x_range=(st.session_state['lim_inf'],
        st.session_state['lim_sup'], 420),
    y_range=(st.session_state['lim_inf'], st.session_state['lim_sup'], 420)
    # abs_scaling=lambda x: x / (x + 1),  # how to scale the lightness in domain coloring
    # contours_abs=2.0,
    # contours_arg=(-np.pi / 2, 0, np.pi / 2, np.pi),
    # emphasize_abs_contour_1: bool = True,
    # add_colorbars: bool = True,
    # add_axes_labels: bool = True,
    # saturation_adjustment: float = 1.28,
    # min_contour_length = None,
    )

    return zplot


def definir_limites():
    st.session_state['lim_inf'] = float(parsearFuncion(st.text_input(
       'x min:', value='-3pi')))
    st.session_state['lim_sup'] = float(parsearFuncion(st.text_input(
       'x max:', value='3pi')))


def plotter_principal():  # streamlit componente
    col_eq, col_lims, col_ctrl = st.columns([2.5, 2, 2])

    # fundamental structure of the user input form

    if 'tema_plots' not in st.session_state:
        st.session_state['tema_plots'] = 'plotly_dark'
    if 'vertical_mode' not in st.session_state:
        st.session_state['vertical_mode'] = False
    with col_eq:
        st.write('\n')
        eq_funcion = st.text_input(
            # 'Ingrese función: ', value='cos(xy) + 3x**3*y**-3 z**2 - sin(xz)')
            'Ingrese función: ', value='cos(x/4)sin(5x)')
        variables_f = st.text_input(
            'Variables: ', value='x',
            help=r'Ingrese qué variables están en la función, separadas por coma. \
                Si la función es compleja, espera como argumento $z$. La unidad imaginaria $i$ que espera es $j$.',
            key='variables_f'
            ).replace(' ', '')

    with col_lims:
        st.write('\n')
        definir_limites()
        sola = st.checkbox('Gráfica sola', value=True,
                           help='Con integral y derivada')
        if not sola:
            st.checkbox('Vertical', value=False,
                help="Agrupar gráficas en modo vertical o horizontal.\
                    No recomendado en modo móvil.",
                key='vertical_mode')

    try:
        if sola:
            graficador(eq_funcion, variables_f)
            if len(variables_f) < 3:
                with st.expander('Raices y extremos:'):
                    # le agregué esto para conocer sus raices
                    # y sus extremos locales de una.
                    try:
                        st.latex(
                        r'\text{Raices en}\;:\;' +
                            sp.latex(
                                sp.solveset(
                                    parsearFuncion(eq_funcion),
                                    sp.symbols(variables_f),
                                    domain=sp.S.Reals if variables_f != 'z' else sp.S.Complexes
                            )))

                        st.latex(r'\text{Extremos en}\;:\;' +
                            sp.latex(
                                sp.solveset(
                                    sp.diff(parsearFuncion(
                                        eq_funcion), variables_f[0]),
                                    sp.symbols(variables_f),
                                    domain=sp.S.Reals if variables_f != 'z' else sp.S.Complexes,
                        )))

                        # Singularidades tambien son importantes de indagar
                        #   sobretodo si f: C -> C

                        st.latex(
                            r'\text{Singularidades en}\;:\;' +
                            sp.latex(
                                sp.singularities(
                                    parsearFuncion(eq_funcion),
                                    sp.symbols(variables_f))
                                )
                        )

                    except:
                        pass
        else:
            graficador_3(eq_funcion, variables_f)  # if variables_f != 'z'
    except Exception as e:
        st.warning(
            'No se pudo gráficar la función, revisa los parámetros ingresados. \n Error: ')
        st.error(e)

    return eq_funcion, variables_f, col_eq, col_lims, col_ctrl


def plot_funcion(f, diff_var=['x'], xa: float = -8.0, xb: float = 8.0, modo=True, auto_fondo=True, idx=0, template='plotly_dark'):

    # c_fondo = hex_rgba(opa=128)

    # plots de funciones complejas hechos con cplot:
    # https://github.com/nschloe/cplot

    if diff_var == 'z':
        return graficador_complex(f)

    else:
        layoutF = go.Layout(
            paper_bgcolor='rgba(0,0,0,0.12)',  # .4)',
            # plot_bgcolor= 'rgba('+','.join([str(c) for c in c_fondo]) + ')' if auto_fondo else '#AAAAAA',
            plot_bgcolor=st.session_state['b_color'] if auto_fondo else '#AAAAAA',
            yaxis_title='f'+'\'' * \
                (idx)+f"({diff_var})" if idx > 0 else f"f({str(diff_var[0])})",
            xaxis_title=str(diff_var[0]),
            yaxis_titlefont=dict(size=20),
            xaxis_titlefont=dict(size=20),
            height=620 if len(diff_var) == 1 else 820,

        )
        fig = go.Figure(layout=layoutF)

        fig.update_layout(template=template)

        # esto es por si recibe una funcion ya y no una expresion
        # se podria quitar pues no se usa not modo ya que plot_funcion no se llama sola

        if modo:
            # ya recibe simbolos
            f = sp.lambdify(sp.symbols(diff_var), f, 'numpy')

        if len(diff_var) == 3:
            xs = np.outer(np.linspace(xa, xb, 200), np.ones(200))
            y = xs.copy().T
            Z = f(xs, y)
            fig.add_trace(go.Surface(
                contours={
                    "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.04}
                },
                x=xs,
                y=y,
                z=Z
                ))

            fig.update_traces(
                contours_z=dict(
                    show=True, usecolormap=True,
                    highlightcolor="seashell",
                    project_z=True
                ))

            fig.update_layout(
                scene={
                    "xaxis": {"nticks": 12},
                    "zaxis": {"nticks": 12},
                    # "yaxis": {"gridcolor": "gray"},
                    'camera_eye': {"x": -1, "y": -1, "z": 0.5},
                    "aspectratio": {"x": 1, "y": 1, "z": 0.5},
                })

        if len(diff_var) == 5:
            X, Y, Z = np.mgrid[xa:xb:30j, xa:xb:30j, xa:xb:30j]

            fig.add_trace(go.Volume(
                x=X.flatten(),
                y=Y.flatten(),
                z=Z.flatten(),
                value=f(X, Y, Z).flatten(),
                isomin=0.1,
                isomax=0.8,
                opacity=0.35,
                surface_count=30,
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
                # ez:  x=t, y=np.sin(t), ...
                x=df.loc[:, f'{diff_var[0]}'],
                y=df.loc[:, 'y'],
                marker_color=st.session_state['p_color'],
                mode='lines',
                line=dict(width=3)
            ))

        return fig


def plot_funciones(f, diff_var=['x'], xa: float = -8.0, 
            xb: float = 8.0, modo=True, auto_fondo=True, 
            idx=0, template='plotly_dark'):

    layoutF = go.Layout(
        paper_bgcolor='rgba(0,0,0,0.12)',
        # plot_bgcolor='rgba('+','.join([str(c) for c in c_fondo]
        #                              ) + ')' if auto_fondo else '#AAAAAA',
        plot_bgcolor=st.session_state['b_color'] if auto_fondo else '#AAAAAA',
        xaxis_title=str(diff_var[0]),
        yaxis_titlefont=dict(size=20),
        xaxis_titlefont=dict(size=20),
        height=960, width=800
    )
    fig = go.Figure(layout=layoutF)

    fig.update_layout(template=template)

    if modo:    # deriva e integra con respecto a la primera variable de diferenciacion
        # ya recibe simbolos
        dfdx = sp.lambdify(sp.symbols(diff_var),
                           sp.diff(f, diff_var[0]), 'numpy')
        F = sp.lambdify(sp.symbols(diff_var), sp.integrate(
            f, sp.symbols(diff_var[0])), 'numpy')
        f = sp.lambdify(sp.symbols(diff_var), f, 'numpy')

    if len(diff_var) == 3:
        xs = np.outer(np.linspace(xa, xb, 200), np.ones(200))
        y = xs.copy().T
        # Z = f(xs, y)
        # Z_diff = dfdx(xs, y)
        # Z_int = F(xs, y)
        funciones = [f(xs, y), dfdx(xs, y), F(xs, y)]
        colorscal = ['Blues', 'Electric', 'Viridis']
        dims : tuple
        specs = []
        vert = st.session_state['vertical_mode']
        if vert:
            dims = (1, 3)
            specs = [[{'type': 'surface'},
                      {'type': 'surface'},
                      {'type': 'surface'}]]
        else:
            dims = (3, 1)
            specs = [[{'type': 'surface'}],
                     [{'type': 'surface'}],
                     [{'type': 'surface'}]]

        fig = make_subplots(rows=dims[0], cols=dims[1], figure=fig,
                            specs=specs,
                            subplot_titles=['f(x,y)', r"f'(x,y)", 'F(x,y)'],
                            vertical_spacing=0.1,
                            horizontal_spacing=0.1
                            )

        # 3, 1,figure=fig,x_title=st.session_state['variables_f'])  # ,figure=fig)

        ix = iy = 1
        for func_xy in funciones:
            fig.add_trace(go.Surface(
                # colorscale=colorscal[ix],
                showscale=False,
                contours={
                    "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.04}
                },
                x=xs,
                y=y,
                z=func_xy
            ), row=ix, col=iy)
            if vert: iy += 1
            else: ix += 1

        fig.update_traces(
            contours_z=dict(
                show=True, usecolormap=True,
                highlightcolor="seashell",
                project_z=True
            ))

        fig.update_layout(
            scene={
                "xaxis": {"nticks": 12},
                "zaxis": {"nticks": 12},
                # "yaxis": {"gridcolor": "gray"},
                'camera_eye': {"x": -1, "y": -1, "z": 0.5},
                "aspectratio": {"x": 1, "y": 1, "z": 0.5},
            })

    if len(diff_var) == 5:
            X, Y, Z = np.mgrid[xa:xb:30j, xa:xb:30j, xa:xb:30j]

            funciones = [
                f(X, Y, Z).flatten(),
                dfdx(X, Y, Z).flatten(),  # + max(f(X, Y, Z)),
                F(X, Y, Z).flatten()  # + max(dfdx(X, Y, Z))
                ]

            dims : tuple
            specs = []
            vert = st.session_state['vertical_mode']

            if vert:
                dims=(1,3)
                specs = [[{'type': 'volume'},
                          {'type': 'volume'},
                          {'type': 'volume'}]]
            else:
                dims=(3,1)
                specs = [[{'type': 'volume'}],
                         [{'type': 'volume'}],
                         [{'type': 'volume'}]]

            

            fig = make_subplots(rows=dims[0], cols=dims[1], figure=fig,
                                specs=specs,
                                subplot_titles=['f(x,y,z)', r"f'(x,y,z)", 'F(x,y,z)'],
                                vertical_spacing=0.1,
                                )

            ix = iy = 0
            for func_xyz in funciones:
                fig.add_trace(go.Volume(
                    x=X.flatten(),
                    y=Y.flatten(),
                    z=Z.flatten(),
                    value=func_xyz,#.flatten(),
                    isomin=0.1,
                    isomax=0.8,
                    opacity=0.35,
                    surface_count=30,
                ), row=ix, col=iy)
                if vert:
                    iy += 1
                else:
                    ix += 1


    if len(diff_var) == 1:

        xs = np.linspace(xa, xb, 620)

        funciones = [
            f(xs),
            dfdx(xs),
            F(xs)
        ]

        fig.update_layout(
            margin=dict(t=16),
        )

        fs = ['f', r"f'", 'F']

        for idx,func_x in enumerate(funciones):
            fig.add_trace(go.Scatter(
                x=xs,
                y=func_x,
                # marker_color=st.session_state['p_color'],
                mode='lines',
                line=dict(width=2),
                name=f"{fs[idx]}({diff_var[0]})",
            ))

    # st.session_state['df_plots'] = df

    return fig
