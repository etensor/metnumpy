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
from integrales.newthonr import netwon_st

from estilos import escoger_tema

st.set_page_config(
    layout="wide",
    page_icon='🛠',
    initial_sidebar_state='expanded',
    menu_items={'About': "### Github:\n www.github.com/etensor/baseconvpy"}
    )

st.title('Calculadora')


opt_menu = st.sidebar.selectbox(
    "Navegador del proyecto",
    ("Presentación","Conversor de bases", "Derivadas", "Falsa posición", "Derivada de un polinomio", "Bisección", "Trapecios", "Rectangulo", "Simpson 1/3", "Solidos de revolción","Secante","Newthon Raphson")
)


if opt_menu == 'Presentación':
    st.subheader('Presentación')
    presentacion_if()

    with st.sidebar:
        with st.expander('Configuración'):
            escoger_tema()

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

    
#with open('../css/presentacion.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)