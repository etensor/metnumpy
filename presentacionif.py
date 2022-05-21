import streamlit as st
import streamlit.components.v1 as components


def presentacion_if():

    nombres,espacio,visaje = st.columns([3,1,4])
    nombres.markdown(r'''
    ---
    ##### Equipo: ''')
    nombres.write('''
     Jean Pierre Vargas\n
     David Penilla\n
     Juan Camilo Bolaños\n
     Sergio Andres Angel\n
     Santiago Abadia
    ''')

    with visaje:
        st.markdown(r'''
        <iframe 
            width="800" height="400" 
            src="https://www.youtube.com/embed/1q3lCglaveE" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write;
             encrypted-media; gyroscope; 
             picture-in-picture" allowfullscreen>
        </iframe>''',unsafe_allow_html=True)    


    st.write('\n')
    st.markdown('---')
    st.markdown('En python hacer una gráfica responsiva de una función sigue siendo una tarea no trivial, javascript permite animaciones elegantes, por ejemplo esta aplicación: https://graphtoy.com/')
    components.iframe("https://graphtoy.com/",height=1300,scrolling=True)
