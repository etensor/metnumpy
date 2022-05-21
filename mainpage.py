from pyparsing import Opt
import streamlit as st
from presentacionif import presentacion_if
from convbases.conversorbasesif import conversor_bases_if
from derivadas.derviadasif import derivadas_if
from integrales.falsaposicionif import falsa_posicion_if
from derivadas.derivadadeunpolinomioif import derivada_de_un_polinomio_if
from derivadas.biseccionif import biseccion_if
from derivadas.secanteif import secante_if
from integrales.trapeciosif import trapecios_if
from integrales.simpson1by3if import simpson1by3_if
from integrales.solidoderevolucionif import solidoderevolucion_if
from integrales.newthonrif import netwon_st
from matrices.mtr import mtr_nm,def_mtr

from estilos import escoger_tema,escoger_fuente,titulo_melo


###     ? Configuracion de la app

if 'fuente' not in st.session_state:
    st.session_state['fuente'] = '"sans serif"'


st.set_page_config(
    layout="wide",
    page_icon='🛠',
    initial_sidebar_state='expanded',
    menu_items={'About': "### Github:\n www.github.com/etensor/metnumpy"}
    )

# hax css para poner st.radio horizontal y centrado
st.write(r'''
<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>
<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:2px;}</style>
''', unsafe_allow_html=True)


if st.session_state['fuente'] in ['"sans serif"', '"serif"']:
    st.markdown('')
else:
    st.markdown(st.session_state['fuente'], unsafe_allow_html=True)



st.title('Calculadora')


opt_menu = st.sidebar.selectbox(
    "Navegador del proyecto",
    ("Presentación","Conversor de bases", "Derivadas", "Falsa posición", "Derivada de un polinomio", "Bisección", "Trapecios", "Rectangulo", "Simpson 1/3", "Solidos de revolción","Secante","Newthon Raphson","matrices")
)

with st.sidebar:
    with st.expander('Configuración'):
        titulo_melo('Configuración')
        escoger_fuente()
        escoger_tema()


if opt_menu == 'Presentación':
    st.subheader('Presentación')
    presentacion_if()



if opt_menu == 'Conversor de bases':
    st.subheader('Conversor de bases')
    conversor_bases_if()

if opt_menu == 'Derivadas':
    st.subheader('Calculadora de Derivadas')
    derivadas_if()

if opt_menu == 'Falsa posición':
    st.subheader('Falsa posición')
    falsa_posicion_if()

if opt_menu == 'Derivada de un polinomio':
    st.subheader('Derivada de un polinomio')
    derivada_de_un_polinomio_if()

if opt_menu == 'Bisección':
    st.subheader('Bisección')
    biseccion_if()

if opt_menu == 'Trapecios':
    st.subheader('Trapecios')
    trapecios_if()

if opt_menu == 'Rectangulo':
    st.subheader('Rectangulo')
    trapecios_if()

if opt_menu == 'Simpson 1/3':
    st.subheader('Simpson 1/3')
    simpson1by3_if()

if opt_menu == 'Solidos de revolción':
    st.subheader('Solidos de revolción')
    solidoderevolucion_if()

if opt_menu == 'Secante':
    st.subheader('Secante')
    secante_if()

if opt_menu == 'Newthon Raphson':
    st.subheader('Newthon Raphson')
    netwon_st()

if opt_menu == 'matrices':
    st.subheader('Matrices')
    def_mtr()
    
#with open('../css/presentacion.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)