import streamlit as st

tema_original = '''
[theme]
primaryColor = "#81ad90"
backgroundColor = "#709178"
secondaryBackgroundColor = "#a3bbad"
textColor = "#f5f5f5"

'''

def escoger_tema():
    st.subheader('Cambie el tema de la aplicación')
    st.info('Mejore el estilo a su gusto.')

    prim,back = st.columns(2)
    sec,tex = st.columns(2)

    with prim:
        color_primario = st.color_picker('Color primario: ', '#81ad90')
    
    with back:
        color_background = st.color_picker('Color de fondo: ', '#709178')

    with sec:
        color_secundario = st.color_picker('Color secundario: ', '#a3bbad')

    with tex:
        texto_color = st.color_picker('Color de texto', '#f5f5f5')
    
    _,aceptar,reestablecer,_ = st.columns(4)

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

    with reestablecer:
        if st.button('Restablecer'):
            file_t = open('.streamlit/config.toml', 'w')
            file_t.write(tema_original)
            file_t.close()
            st.sucess('Tema reestablecido.')
        


#
#[theme]
#primaryColor = "#81ad90"
#backgroundColor = "#709178"
#secondaryBackgroundColor = "#a3bbad"
#textColor = "#f5f5f5"
#