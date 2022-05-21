import streamlit as st
import toml

tema_verde = r'''
[theme]
primaryColor = "#81ad90"
backgroundColor = "#709178"
secondaryBackgroundColor = "#a3bbad"
textColor = "#f5f5f5"
font="sans serif"
'''

tema_noche = r'''
[theme]
primaryColor = "#0B3B08"
backgroundColor = "#B5B127"
secondaryBackgroundColor = "#6A710F"
textColor = "#000000"
font="sans serif"
'''

tema_claro = r'''
[theme]
primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"
'''

tema_azul = r'''
[theme]
primaryColor="#006e52"
backgroundColor="#002b36"
secondaryBackgroundColor="#586e75"
textColor="#fafafa"
font="sans serif"
'''



def temas_definidos(tema : str):
    file_t = open('.streamlit/config.toml', 'w')
    file_t.write(tema)
    file_t.close()
    st.success('Tema modificado!')
    return

def cambiar_fuente(sans=True):
    file_t = open('.streamlit/config.toml', 'r')
    config_tema = file_t.read()

    if 'font' in config_tema:
        if sans:
            st.session_state['fuente'] = '"serif"'
            config_tema = config_tema.replace(r'sans serif', r'serif')
        else:
            st.session_state['fuente'] = '"sans serif"'
            if '"sans serif"' in config_tema:
                pass
            else:
                config_tema = config_tema.replace(r'serif', r'sans serif')

    file_t.close()

    f_config = open('.streamlit/config.toml', 'w')
    f_config.write(config_tema)
    f_config.close()
    return


def escoger_fuente():
    st.markdown("<h3 style='text-align: center;'> Fuente </h3>",
                unsafe_allow_html=True)
    
    
    sel_fuentes = st.selectbox('seleccione: ',
        ('Sans', 'Serif','Code','Formal','Nítida'),
    )


    if sel_fuentes == 'Serif':
        cambiar_fuente(sans=True)
    if sel_fuentes == 'Sans':
        cambiar_fuente(sans=False)

    if sel_fuentes == 'Code':
        st.session_state['fuente']="""
            <style>
    @font-face {
    font-family: 'Fira Code';
    font-style: monospace;
    font-weight: 400;
    src: @import url('https://fonts.googleapis.com/css2?family=Fira+Code&display=swap');
    }

        html, body, [class*="css"]  {
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        }
        </style>
        """
    
    if sel_fuentes == 'Formal':
        st.session_state['fuente'] = """
            <style>
    @font-face {
    font-family: 'Playfair Display';
    font-style: serif;
    font-weight: 400;
    src: @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
    }

        html, body, [class*="css"]  {
        font-family: 'Playfair Display', serif;
        font-size: 16px;
        }
        </style>

        """
    if sel_fuentes == 'Nítida':
        st.session_state['fuente'] = """
            <style>
    @font-face {
    font-family: 'Quicksand';
    font-style: serif;
    font-weight: 400;
    src: @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap');
    }

        html, body, [class*="css"]  {
        font-family: 'Quicksand', sans-serif;
        font-size: 16px;
        }
        </style>

        """

    


#File_object.writelines(L) for L = [str1, str2, str3]

def escoger_tema():
    st.markdown("<h3 style='text-align: center;'>Tema</h3>",
                unsafe_allow_html=True)



    tema_1,tema_2,tema_3,tema_4 = st.columns(4)
    config_actual = toml.load('.streamlit/config.toml')

    if tema_1.button('Verde'):
        temas_definidos(tema_verde)
        st.experimental_rerun()
    
    if tema_2.button('Noche'):
        temas_definidos(tema_noche)
        st.experimental_rerun()
    
    if tema_3.button('Claro'):
        temas_definidos(tema_claro)
        st.experimental_rerun()
        
    if tema_4.button('Azul'):
        temas_definidos(tema_azul)
        st.experimental_rerun()


    prim,back = st.columns(2)
    sec,tex = st.columns(2)



    with prim:
        color_primario = st.color_picker('Color primario: ', 
        config_actual['theme']['primaryColor'])
    
    with back:
        color_background = st.color_picker('Color de fondo: ',
        config_actual['theme']['backgroundColor'])

    with sec:
        color_secundario = st.color_picker('Color secundario: ', 
        config_actual['theme']['secondaryBackgroundColor'])

    with tex:
        texto_color = st.color_picker('Color de texto',
        config_actual['theme']['textColor'])
    
    _,aceptar,reestablecer,_ = st.columns([1,3,3,1])

    with aceptar:
        if st.button('Aplicar cambios'):
            file_t = open('.streamlit/config.toml', 'w')
            fuente_conf = '"sans serif"'
            if st.session_state['fuente'] in ['"sans serif"', '"serif"']:
                fuente_conf = st.session_state['fuente']
            tema_definido = f'[theme]\n \
primaryColor = "{color_primario}"\n\
backgroundColor = "{color_background}"\n\
secondaryBackgroundColor = "{color_secundario}"\n\
textColor = "{texto_color}"\n\
font={fuente_conf}'

            file_t.write(tema_definido)
            file_t.close()
            st.success('Tema modificado!')
            st.experimental_rerun()

    with reestablecer:
        if st.button('Restablecer config'):
            file_t = open('.streamlit/config.toml', 'w')
            file_t.write(tema_verde)
            file_t.close()
            st.success('Tema reestablecido.')
            st.experimental_rerun()





def titulo_melo(titulo : str):
    estilo_lampara = r"""
    <style>
        .title h2{
            user-select: none;
            font-size: 28px;
            color: #000;
            text-align: center;
            background: linear-gradient(to left, #FFF 30%, #005030 40%, #006040 50%, #FFF 60%);
            background-size: 120% auto;
            text-fill-color: transparent;
            -webkit-text-fill-color: transparent;
            -webkit-background-clip: text;
            animation: shine 30s linear infinite;
        }
        
        @keyframes shine {
            0%{
            background-position-x: 0%;
            }
            100%{
            background-position-x: 600vw;
            }
        }
    </style> 
    """


    css_ti = estilo_lampara +  """
    <div class="title">
        <h2>""" + titulo + """</h2>
    </div>"""

    st.markdown(css_ti, unsafe_allow_html=True)
