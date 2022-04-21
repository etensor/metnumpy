import streamlit as st
from solidoderevolucion import comenzarX

def solidoderevolucion_if():
    confirmar = True
    st.write('Solido de revolución')

    function = st.text_input('Función', value='')
    eje = st.radio('Eje de giro:',('x','y'))
    desde = int(st.slider('Desde', min_value=-50, max_value=50, value = 0))
    hasta = int(st.slider('Hasta', min_value=-50, max_value=50, value = 0))

    if function != '' and desde != '' and hasta != '' and confirmar:
        if eje == 'x':
            resultado = comenzarX(function, desde, hasta)
            st.success(f'Volumen: {resultado}') 

        elif eje == 'y':
            pass