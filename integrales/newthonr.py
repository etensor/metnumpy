from xxlimited import new
from integrales.newthonrif import graficar, newthonr
import streamlit as st
from derivadas.derivadas import parsearFuncion

#newthonr(f, 3.8, 10**-10)

#grafica
#graficar(f,-10,10)

def netwon_st():
    newton = st.container()

    with newton:
        funcion = st.text_input('Ingrese la funcion f(x)')
        if funcion == '':
            funcion = 'cos(x/3)sin(3x)'
        funcion = str(parsearFuncion(funcion))
        resultado = newthonr(funcion, 3.8, 10**-10)
        graf = graficar(funcion, -10, 10)
        st.write('Resultado : ',resultado)
        
        st.pyplot(graf)

