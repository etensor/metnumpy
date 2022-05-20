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
font="serif"

'''

tema_claro = r'''
[theme]
primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="serif"

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
            config_tema = config_tema.replace(r'font="sans serif"', 'font="serif"')
        else:
            config_tema = config_tema.replace('font="serif"', r'font="sans serif"')

    file_t.close()

    f_config = open('.streamlit/config.toml', 'w')
    f_config.write(config_tema)
    f_config.close()
    return


def escoger_fuente():
    st.subheader('Cambie la fuente de la aplicación')
    fuente_1, fuente_2 = st.columns(2)

    if fuente_1.button('Sans'):
        cambiar_fuente(sans=True)
    if fuente_2.button('Serif'):
        cambiar_fuente(sans=False)
    
    #st.experimental_rerun()

    


#File_object.writelines(L) for L = [str1, str2, str3]

def escoger_tema():
    st.subheader('Cambie el tema de la aplicación')



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
            tema_definido = f'[theme]\n \
                primaryColor = "{color_primario}"\n \
                backgroundColor = "{color_background}"\n \
                secondaryBackgroundColor = "{color_secundario}"\n \
                textColor = "{texto_color}"\n'

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


'''
h1 { color: #111; font-family: 'Helvetica Neue', sans-serif; font-size: 275px; font-weight: bold; letter-spacing: -1px; line-height: 1; text-align: center; }


h2 { color: #111; font-family: 'Open Sans', sans-serif; font-size: 30px; font-weight: 300; line-height: 32px; margin: 0 0 72px; text-align: center; }


p { color: #685206; font-family: 'Helvetica Neue', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; }

'''


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
