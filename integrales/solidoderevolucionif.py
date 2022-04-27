import streamlit as st
from integrales.solidoderevolucion import comenzarX
import numpy as np
import matplotlib.pyplot as plt

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

            np.seterr(divide='ignore', invalid='ignore')

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')


            ll, ul = 0, 1 
            u = np.linspace(ll, ul, 60)
            v = np.linspace(0, 2*np.pi, 60)
            U, V = np.meshgrid(u, v)

            Z = U

            X = np.sqrt(Z)*np.cos(V)
            Y = np.sqrt(Z)*np.sin(V)

            ax.set_xlabel('Y axis')
            ax.set_ylabel('X axis')
            ax.set_zlabel('Z axis')

            ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

            #plt.show()
            st.pyplot(plt,figsize=(2, 2))

            y = function
            