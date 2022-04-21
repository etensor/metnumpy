from matplotlib import pyplot as plt
import streamlit as st
import numpy as np

def  derivada_de_un_polinomio_if():
    coefs = st.text_input('Ingrese los coeficientes de la función',
                            value='1.25,-7.4,-10.43,25.86,-3.15')

    coefs = coefs.split(',')
    coeficientes = [float(i) for i in coefs]

    fx = np.poly1d(np.array(coefs))
    xs = np.linspace(-10, 10, 200)

    raices = np.roots(coefs)
    idx = 0
    textos,vals = st.columns(2)
    for raiz in raices:
        textos.latex(f'x_{{{idx}}}')
        vals.write('\n')
        vals.write(raiz)
        idx+=1
    
    polinomio = np.poly1d(coeficientes)

    fig, ax = plt.subplots()
    ax.plot(xs, polinomio(xs))
    st.subheader('Gráfica')
    st.pyplot(fig)