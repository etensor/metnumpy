from pyparsing import Opt
import streamlit as st
from presentacionif import presentacion_if
from convbases.conversorbasesif import conversor_bases_if
from derivadas.derviadasif import derivadas_if
from integrales.falsaposicionif import falsa_posicion_if
from derivadas.derivadadeunpolinomioif import derivada_de_un_polinomio_if
from derivadas.biseccionif import biseccion_if
from derivadas.secanteif import secante_if
from derivadas.derivadas import parsearFuncion
from integrales.trapeciosif import trapecios_if
from integrales.simpson1by3if import simpson1by3_if
from integrales.solidoderevolucionif import solidoderevolucion_if
from integrales.newthonrif import netwon_st
from matrices.mtr import mtr_nm,def_mtr
from integrales.minimocudradoif import minimo_cuadrado_if

from estilos import escoger_tema,escoger_fuente,titulo_melo,titulo_melo2,config_actual
from plotterfuncion import plotter_principal,pd_json


###     ? Configuracion de la app

if 'fuente' not in st.session_state:
    st.session_state['fuente'] = '"sans serif"'
    st.session_state['tema_plots'] = 'plotly_dark'
    st.session_state['variables_f'] = ['x']

if 'lim_inf' not in st.session_state:    
    st.session_state['lim_inf'] = -5
    st.session_state['lim_sup'] = 5


st.set_page_config(
    layout="wide",
    page_title='metnumpy',
    page_icon='🛠',
    initial_sidebar_state='expanded',
    menu_items={'About': "### Github:\n www.github.com/etensor/metnumpy"}
    )

# hax css para poner st.radio horizontal y centrado
st.write(r'''
<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>
<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:4px;padding-right:4px}</style>
''', unsafe_allow_html=True)


if 'p_color' not in st.session_state:
    st.session_state['p_color'] = config_actual['theme']['primaryColor']

if 't_color' not in st.session_state:
    st.session_state['t_color'] = config_actual['theme']['textColor']

if 'b_color' not in st.session_state:
    st.session_state['b_color'] = config_actual['theme']['backgroundColor']

# una vez grafique recordara que funcion trata,
#   # Podemos usar esto para aplicar las mismas funciones
#   # a diferentes metodos sin reescribirlos! :o :D
#  requeriria un refactoring minimo
#if 'df_plots' not in st.session_state:
#    st.session_state['df_plots'] = {}


#st.title('Calculadora')
st.markdown('''
 <p style="text-align: center; font-size: 36px"> Calculadora: metnumpy</p>
''', unsafe_allow_html=True)



if st.session_state['fuente'] in ['"sans serif"', '"serif"']:
    st.markdown('')
else:
    st.markdown(st.session_state['fuente'], unsafe_allow_html=True)


with st.sidebar:  # gif epa + titulo XD
    st.markdown(r''' 
        <iframe style="font-align: center; border-radius: 200px" src="https://giphy.com/embed/3owzW5c1tPq63MPmWk" 
        width="240" height="80" 
        frameBorder="0"></iframe>
    ''', unsafe_allow_html=True)
    titulo_melo2('metnumpy')
  

opt_menu = st.sidebar.selectbox(
    "Navegador del proyecto",
    ("Presentación",
    "Conversor de bases",
    "Ecuaciones",
    "Integrales",
    "Matrices"
    )
)

menu_ecuaciones = st.sidebar.selectbox(
    'Métodos de ecuaciones',
    ("Derivadas",
     "Falsa posición",
     "Derivada de un polinomio",
     "Newton Raphson",
     "Secante",
     "Bisección"
     )) if opt_menu == 'Ecuaciones' else None


menu_integrales = st.sidebar.selectbox(
    'Métodos de integrales',
    (
        "Trapecios",
        "Rectangulo", 
        "Simpson 1/3",
        "Minimo cuadrado", 
        "Sólidos de revolución",
    )) if opt_menu == 'Integrales' else None


st.sidebar.markdown('---')


if opt_menu == 'Presentación':
    st.subheader('Presentación')
    presentacion_if()


if opt_menu == 'Conversor de bases':
    st.subheader('Conversor de bases')
    conversor_bases_if()

if opt_menu in ('Ecuaciones','Integrales'):
    eq_funcion, variables_f, _, _, col_diff=plotter_principal()


if opt_menu == 'Ecuaciones':
    if menu_ecuaciones == 'Derivadas':
        st.subheader('Calculadora de Derivadas')
        derivadas_if(eq_funcion,col_diff)

    if menu_ecuaciones == 'Falsa posición':
        st.subheader('Falsa posición')
        falsa_posicion_if()

    if menu_ecuaciones == 'Derivada de un polinomio':
        st.subheader('Derivada de un polinomio')
        derivada_de_un_polinomio_if()

    if menu_ecuaciones == 'Bisección':
        st.subheader('Bisección')
        biseccion_if()
    
    if menu_ecuaciones == 'Secante':
        st.subheader('Secante')
        secante_if()

    if menu_ecuaciones == 'Newthon Raphson':
        st.subheader('Newthon Raphson')
        netwon_st()


if opt_menu == 'Integrales':
    if menu_integrales == 'Trapecios':
        st.subheader('Trapecios')
        trapecios_if()

    if menu_integrales == 'Rectangulo':
        st.subheader('Rectangulo')
        trapecios_if()

    if menu_integrales == 'Simpson 1/3':
        st.subheader('Simpson 1/3')
        simpson1by3_if()

    if menu_integrales == 'Minimo cuadrado':
        st.subheader('Minimo cuadrado')
        minimo_cuadrado_if()

    if menu_integrales == 'Sólidos de revolución':
        st.subheader('Sólidos de revolución')
        solidoderevolucion_if()

    

if opt_menu == 'Matrices':
    st.subheader('Matrices')
    def_mtr()
    





#? config + musica en la barra de al lado

with st.sidebar:
    #if st.sidebar.checkbox("Datos de la función", value=False):
    #st.dataframe(st.session_state['df_plots'])

    with st.expander('Configuración'):
        titulo_melo('Configuración')
        escoger_fuente()
        st.markdown('---')
        st.radio(
            'Tema de los gráficos',
            ('plotly_dark', 'ggplot2', 'seaborn','presentation'),
            key='tema_plots',
            help='Cambie aquí como se ven las gráficas, \
                se ve más el cambio en superficies y volumenes 3D.'
            )
        st.markdown('---')
        escoger_tema()
        

    with st.expander('Música'):
        musica_file = open('extras/vivaldi-RV34_bflat.ogg', 'rb')
        sonido = musica_file.read()
        st.markdown(r'''<style>
            .musc p {
                text-align: right;
                 right; font-size: 12px;
                }</style> <div class="musc"> <p>Vivaldi RV34 III. Largo </p> </div>''', unsafe_allow_html=True)
        st.audio(sonido, format='audio/ogg')
        st.markdown(r'''
        <iframe width="260" height="190" 
        src="https://www.youtube-nocookie.com/embed/videoseries?list=PLt-bqDWZA6oo_jubLNjbkPmCgef6AZlhF" 
        title="YouTube video player" frameborder="0" allow="accelerometer; 
        autoplay; clipboard-write; encrypted-media; gyroscope; 
        picture-in-picture" allowfullscreen>
        </iframe>
        ''', unsafe_allow_html=True)






#with open('../css/presentacion.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)