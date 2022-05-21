import streamlit as st
import toml

tema_verde = r'''
[theme]
primaryColor = "#e6c320"
backgroundColor = "#355749"
secondaryBackgroundColor = "#709580"
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

tema_oscuro = r'''
[theme]
primaryColor = "#9a2100"
backgroundColor = "#000000"
secondaryBackgroundColor = "#191135"
textColor = "#f6ef7a"
font="serif"
'''

tema_matrix = r'''
[theme]
primaryColor = "#06af87"
backgroundColor = "#08080e"
secondaryBackgroundColor = "#192106"
textColor = "#64d503"
font="serif"
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
    
    
    sel_fuentes = st.selectbox('seleccione la óptima: ',
        ('Sans', 'Serif','Code','Formal','Nítida'),
        help='Presione en [ Aplicar cambios ] si los cambios no se efectuan.'
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

        html, body,[class*="css"]  {
        font-family: 'Quicksand', sans-serif;
        font-size: 16px;
        }
        </style>

        """

    
config_actual = toml.load('.streamlit/config.toml')
#File_object.writelines(L) for L = [str1, str2, str3]

def escoger_tema(config = config_actual):
    st.markdown("<h3 style='text-align: center;'>Tema</h3>",
                unsafe_allow_html=True)


    tema_1,tema_2,tema_3,tema_4 = st.columns(4)
    _,tema_5,tema_6,_ = st.columns([1,2,2,1])
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

    if tema_5.button('Oscuro'):
        temas_definidos(tema_oscuro)
        st.experimental_rerun()
    
    if tema_6.button('Matrix'):
        temas_definidos(tema_matrix)
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
        if st.button('Aplicar cambios',help='Guarda los cambios en el tema'):
            file_t = open('.streamlit/config.toml', 'w')
            fuente_conf = '"sans serif"'
            st.session_state['b_color'] = color_background
            st.session_state['p_color'] = color_primario
            if st.session_state['fuente'] in ['"sans serif"', '"serif"']:
                fuente_conf = st.session_state['fuente']
            tema_definido = f'[theme]\n\
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
            color: rgb(40,40,40);
            text-align: center;
            background: linear-gradient(to left, rgb(40,40,40) 30%, #005030 40%, #006040 50%, rgb(40,40,40) 60%);
            background-size: 120% auto;
            
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


def titulo_melo2(titulo: str):  # css es re chimba :o
    st.markdown(r'''             
    <style>
    .metnum h2 {
    font-size: 40px;
    font-weight: 500;
    user-select: none;
    background: transparent;
    -webkit-background-clip: text;
    -webkit-text-fill-color: #''' + config_actual['theme']['textColor'] + r''';
    text-shadow:
        -4px -2px 5px #000000,
        3px 2px 8px #EEEEEE,
        -16px -8px 5px '''+st.session_state['p_color']+r''',
        0px 0px 10px '''+st.session_state['p_color']+r''',
        0px 0px 15px '''+st.session_state['p_color']+r''',
        0px 0px 25px '''+st.session_state['p_color']+r''';
    text-align: center;
    }
    max-height: 50%;
    </style>

    <div class="metnum">
        <h2>'''+titulo+'''</h2>
    </div>
    ''',unsafe_allow_html=True)