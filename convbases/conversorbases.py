from ibm2ieee import ibm2float32, ibm2float64

from email.policy import strict
import math
import struct
import numpy 
#nuevo
from ibm2ieee import ibm2float32, ibm2float64

# base(number, input_base, output_base)
#Binario a decimal (str)
#Decimal a octal (int)
#Decimal a hexadecimal (int)
def conversor_bases(num, base):
    si = num
    if si.find('.') != -1:
        dec = num[num.find('.')+1:len(num)]
        num = num[0:num.find('.')]

        binarioF = convertir_fraccion(dec, 2)
        octalF = convertir_fraccion(dec, 8)
        decimalF = convertir_fraccion(dec, 10)
        hexadecimalF = convertir_fraccion(dec, 16)

    if base == 2:
        num = int(num)
        binario = str(num)
        octal = binario_a_decimal(str(num))
        octal = decimal_a_octal(octal)
        decimal = binario_a_decimal(str(num))
        hexadecimal = decimal_a_hexadecimal(decimal)

    elif base == 8:
        num = int(num)
        binario = octal_a_decimal(str(num))
        binario = decimal_a_binario(binario)
        octal = str(num)
        decimal = octal_a_decimal(str(num))
        hexadecimal = decimal_a_hexadecimal(num)

    elif base == 10:
        num = int(num)
        binario = decimal_a_binario(num)
        octal = decimal_a_octal(num)
        decimal = str(num)
        hexadecimal = decimal_a_hexadecimal(num)

    elif base == 16:
        binario = hexadecimal_a_decimal(num)
        binario = decimal_a_binario(binario)
        octal = hexadecimal_a_decimal(num)
        octal = decimal_a_octal(octal)
        decimal = hexadecimal_a_decimal(num)
        hexadecimal = num

    if si.find('.') != -1:
        binario = binario + '.' + binarioF
        octal = octal + '.' + octalF
        decimal = decimal + '.' + decimalF
        hexadecimal = hexadecimal + '.' + hexadecimalF

    return binario, octal, decimal, hexadecimal

def remplazo16(num):
        num=int(num)
        if num==10:
            return 'A'
        elif num==11: 
            return  'B'
        elif num==12:
            return  'C'
        elif num==13:
            return  "D"
        elif num==14:
            return  "E"
        elif num==15:
            return  "F"
        else:
            return str(num)

def convertir_fraccion(dec, base):
    msj=""
    dec = dec[::-1] + ".0"
    dec = dec[::-1]
    auxiliar= float(dec)
    for i in range(0,8):
        operacion=auxiliar*base
        msj= msj+""+str(remplazo16(int(operacion)))
        decimal=str(operacion).split('.')
        auxiliar=float("0."+decimal[1])
    return msj

def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def fraccion(num, base, baseA):
    pass

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "F": 15,
        "E": 14,
        "D": 13,
        "C": 12,
        "B": 11,
        "A": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    hexadecimal = hexadecimal.upper()
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal


def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
        
    return decimal


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def conversor_bases(num, base, signo):
    if num.find('.') == -1:
        binario, octal, decimal, hexadecimal = entero(num, int(base))
        if signo == '-':
            sign_bit, exp_str, mant_str = floatingPoint32(int(decimal)*-1)
            ieee_32 = str(sign_bit) + ' ' + exp_str + ' ' + mant_str
            sign_bit64, exp_str64, mant_str64 = floatToBinary64(int(decimal)*-1)
            ieee_64 = str(sign_bit64) + ' ' + exp_str64 + ' ' + mant_str64
        else:
            sign_bit, exp_str, mant_str = floatingPoint32(int(decimal))
            ieee_32 = str(sign_bit) + ' ' + exp_str + ' ' + mant_str
            sign_bit64, exp_str64, mant_str64 = floatToBinary64(int(decimal))
            ieee_64 = str(sign_bit64) + ' ' + exp_str64 + ' ' + mant_str64
        return binario, octal, decimal, hexadecimal, ieee_32, ieee_64

    else:
        def proceso(num):
            frac = num[num.find('.')+1::]
            num = num[:num.find('.')]
            binario, octal, decimal, hexadecimal = entero(num, int(base))
            fraccionBinario, fraccionOctal, fraccionDecimal, fraccionHexadecimal = fraccion(frac, base)
            if signo == '-':
                sign_bit, exp_str, mant_str = floatingPoint32(float(decimal + '.' + fraccionDecimal)*-1.0)
                ieee_32 = str(sign_bit) + ' ' + exp_str + ' ' + mant_str
                sign_bit64, exp_str64, mant_str64 = floatToBinary64(float(decimal + '.' + fraccionDecimal)*-1.0)
                ieee_64 = str(sign_bit64) + ' ' + exp_str64 + ' ' + mant_str64
            else:
                sign_bit, exp_str, mant_str = floatingPoint32(float(decimal + '.' + fraccionDecimal))
                ieee_32 = str(sign_bit) + ' ' + exp_str + ' ' + mant_str
                sign_bit64, exp_str64, mant_str64 = floatToBinary64(float(decimal + '.' + fraccionDecimal))
                ieee_64 = str(sign_bit64) + ' ' + exp_str64 + ' ' + mant_str64
            return binario + '.' + fraccionBinario, octal + '.' + fraccionOctal, decimal + '.' + fraccionDecimal, hexadecimal + '.' + fraccionHexadecimal, ieee_32, ieee_64
        
        if base == 2 or base == 8 or base == 10 or base == 16:
            return proceso(num)
        else:
            pass

def entero(num, base):
    if base == 2:
        binario = num
        decimal = str(binario_a_decimal(num))
        octal = str(decimal_a_octal(int(decimal)))
        hexadecimal = str(decimal_a_hexadecimal(int(decimal)))
    elif base == 8:
        decimal = str(octal_a_decimal(str(num)))
        binario = str(decimal_a_binario(int(decimal)))
        octal = num
        hexadecimal = str(decimal_a_hexadecimal(int(decimal)))
    elif base == 10:
        binario = str(decimal_a_binario(int(num)))
        octal = str(decimal_a_octal(int(num)))
        decimal = num
        hexadecimal = str(decimal_a_hexadecimal(int(num)))
    elif base == 16:
        num = num.upper()
        decimal = str(hexadecimal_a_decimal(num))
        binario = str(decimal_a_binario(int(decimal)))
        octal = str(decimal_a_octal(int(decimal)))
        hexadecimal = num

    return binario, octal, decimal, hexadecimal

def fraccion(num, base):
    if base == 10:
        fraccionDecimal = num
    else:
        fraccionDecimal = fraccion_a_fracciondecimal(num, base)

    fraccionBinario, fraccionOctal, fraccionHexadecimal = fracciondecimal_a_fraccion(fraccionDecimal)

    return fraccionBinario, fraccionOctal, fraccionDecimal, fraccionHexadecimal

def fraccion_a_fracciondecimal(num, base):
    i = -1
    fraccion = 0
    for x in num:
        valorReal = obtener_valor_real(x)
        fraccion += int(valorReal) * (int(base) ** int(i))
        i -= 1

    fraccion = str(fraccion)
    return fraccion[fraccion.find('.')+1::]

def fracciondecimal_a_fraccion(num):
    num = num[::-1] + '.0'
    num = num[::-1]
    bases = [2, 8, 16]
    salida = list()
    aux = num
    resultado = ''

    for x in bases:
        for i in range(0, 8):
            if float(num) == 0:
                break

            num = float(num) * x
            num = str(num)
            resultado += obtener_caracter_hexadecimal(int(num[:num.find('.')]))
            num = num[num.find('.')+1::]
            num = num[::-1] + '.0'
            num = float(num[::-1])

        salida.append(resultado)
        resultado = ''
        num = aux
    
    return salida[0], salida[1], salida[2]

def binaryOfFraction32(fraction):
 
    # Declaring an empty string
    # to store binary bits.
    binary = str()
 
    # Iterating through
    # fraction until it
    # becomes Zero.
    while (fraction):
         
        # Multiplying fraction by 2.
        fraction *= 2
 
        # Storing Integer Part of
        # Fraction in int_part.
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0
     
        # Adding int_part to binary
        # after every iteration.
        binary += str(int_part)
 
    # Returning the binary string.
    return binary
 
# Function to get sign  bit,
# exp bits and mantissa bits,
# from given real no.
def floatingPoint32(real_no):
 
    # Setting Sign bit
    # default to zero.
    sign_bit = 0
 
    # Sign bit will set to
    # 1 for negative no.
    if(real_no < 0):
        sign_bit = 1
 
    # converting given no. to
    # absolute value as we have
    # already set the sign bit.
    real_no = abs(real_no)
 
    # Converting Integer Part
    # of Real no to Binary
    int_str = bin(int(real_no))[2 : ]
 
    # Function call to convert
    # Fraction part of real no
    # to Binary.
    fraction_str = binaryOfFraction32(real_no - int(real_no))
 
    # Getting the index where
    # Bit was high for the first
    # Time in binary repres
    # of Integer part of real no.
    ind = int_str.index('1')
 
    # The Exponent is the no.
    # By which we have right
    # Shifted the decimal and
    # it is given below.
    # Also converting it to bias
    # exp by adding 127.
    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]
 
    # getting mantissa string
    # By adding int_str and fraction_str.
    # the zeroes in MSB of int_str
    # have no significance so they
    # are ignored by slicing.
    mant_str = int_str[ind + 1 : ] + fraction_str
 
    # Adding Zeroes in LSB of
    # mantissa string so as to make
    # it's length of 23 bits.
    mant_str = mant_str + ('0' * (23 - len(mant_str)))
 
    # Returning the sign, Exp
    # and Mantissa Bit strings.
    return sign_bit, exp_str, mant_str

def convertToInt32(mantissa_str):
 
    # variable to make a count
    # of negative power of 2.
    power_count = -1
 
    # variable to store
    # float value of mantissa.
    mantissa_int = 0
 
    # Iterations through binary
    # Number. Standard form of
    # Mantissa is 1.M so we have
    # 0.M therefore we are taking
    # negative powers on 2 for
    # conversion.
    for i in mantissa_str:
 
        # Adding converted value of
        # Binary bits in every
        # iteration to float mantissa.
        mantissa_int += (int(i) * pow(2, power_count))
 
        # count will decrease by 1
        # as we move toward right.
        power_count -= 1
         
    # returning mantissa in 1.M form.
    return (mantissa_int + 1)

def floatToBinary64(value):
    import struct
    getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
    num = str(value)
    if num.find('-') == -1:
        signo = '0'
    else:
        signo = '1'
        num = num[1::]
        
    num = float(value)

    val = struct.unpack('Q', struct.pack('d', value))[0]
    num = str(getBin(val))
    exponente = num[:11]
    significado = num[11::]
    return signo, exponente, significado