import streamlit as st
from convbases.conversorbases import conversor_bases, binary64ToFloat, ieee32_to_decimal

def conversor_bases_if():
    menu_met = st.radio('Base :',('Decimal','Binaria','Octal', 'Hexadecimal', '32 bits', '64 bits'))
    #Bases
    if menu_met == 'Binaria':
        base = 2
    elif menu_met == 'Octal':
        base = 8
    elif menu_met == 'Decimal':
        base = 10
    elif menu_met == 'Hexadecimal':
        base = 16
    elif menu_met == '32 bits':
        base = '32 bits'
    elif menu_met == '64 bits':
        base = '64 bits'

    numero = st.text_input("Escribe el número en la base que seleccionaste", key=int, value='')
    denegado = False

    if numero != '':
        if base == 2:
            for x in numero:
                if x == '0' or x == '1' or x == '-' or x == '.':
                    pass
                else:
                    denegado = True
                    break
        
        if base == 8:
            for x in numero:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '-' or x == '.':
                    pass
                else:
                    denegado = True
                    break

        if base == 10:
            for x in numero:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '-' or x == '.':
                    pass
                else:
                    denegado = True
                    break

        if base == 16:
            for x in numero:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == 'A' or x == 'B' or x == 'C' or x == 'D' or x == 'E' or x == 'F' or x == 'a' or x == 'b' or x == 'c' or x == 'd' or x == 'e' or x == 'f' or x == '-' or x == '.':
                    pass
                else:
                    denegado = True
                    break

        if base == '32 bits':
            for x in numero:
                if x == '0' or x == '1' or ' ':
                    pass
                else:
                    denegado = True
                    break

        if base == '64 bits':
            for x in numero:
                if x == '0' or x == '1' or ' ':
                    pass
                else:
                    denegado = True
                    break
        elif base == '64 bits' and len(numero) >= 3 and ((numero[1] == ' ' and numero[2] == '1') or (numero[1] == '1')):
            pass
        elif base == '64 bits' and (len(numero) < 3):
            denegado = True

        if denegado == False:
            negativo = False
            if base != '32 bits' and base != '64 bits' and numero[0] == '-':
                negativo = True
                if numero.find('.') == -1:
                    numero = str(int(numero) * -1)
                else:
                    numero = str(float(numero) * -1.0)

            if base == '64 bits':
                if numero[0] == '1':
                    negativo = True
                    numero = numero[1::]
                    numero = numero.replace(' ', '')
                else:
                    numero = numero[1::]
                    numero = numero.replace(' ', '')

            

            if base == '32 bits':
                print("NUMERO ORIGI ", numero)
                numero = ieee32_to_decimal(numero)
                print("NUMEROOO", numero)
                if numero.find('.') != -1:
                    if float(numero[numero.find('.')+1::]) == 0:
                        numero = numero[:numero.find('.')]
                        print("NUMERO", numero)
                base = 10

            if base == '64 bits':
                numero = binary64ToFloat(numero)
                if numero.find('.') != -1:
                    if float(numero[numero.find('.')+1::]) == 0:
                        numero = numero[:numero.find('.')]
                base = 10

            if negativo == True:
                #ptoflotante, expontente, mantisa = floatingPoint(float(decimal)*-1)
                try:
                    binario, octal, decimal, hexadecimal, bits32, bits64 = conversor_bases(numero, base, '-')
                    st.success(f'Binario: -{binario}')
                    st.success(f'Octal: -{octal}')
                    st.success(f'Decimal: -{decimal}')
                    st.success(f'Hexadecimal: -{hexadecimal}')
                    st.success(f'32 bits: {bits32}')
                    st.success(f'64 bits: {bits64}')
                except:
                    pass
            else:
                try:
                    #ptoflotante, expontente, mantisa = floatingPoint(float(decimal))
                    binario, octal, decimal, hexadecimal, bits32, bits64 = conversor_bases(numero, base, '+')
                    st.success(f'Binario: {binario}')
                    st.success(f'Octal: {octal}')
                    st.success(f'Decimal: {decimal}')
                    st.success(f'Hexadecimal: {hexadecimal}')
                    st.success(f'32 bits: {bits32}')
                    st.success(f'64 bits: {bits64}')
                except:
                    pass

            with open('css/presentacion.css') as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

            #st.success(f'Punto flotante: {ptoflotante}')
            #st.success(f'Exponente: {expontente}')
            #st.success(f'Mantisa:  {mantisa}')

        else:
            st.write('Por favor ingresa caracteres validos.')
            st.write('Números validos:')
            st.write('Binario: 0, 1')
            st.write('Octal: 0, 1, 2, 3, 4, 5, 6, 7')
            st.write('Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
            st.write('Hexadecimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, A, B, C, D, E, F')