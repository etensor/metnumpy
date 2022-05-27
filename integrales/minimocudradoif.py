import streamlit as st
import matplotlib.pyplot as plt
from pylab import mpl
import math
from mpl_toolkits.mplot3d import Axes3D

def minimo_cuadrado_if():
    menu_met = st.radio('Base :',('Lineal','Polinomial','Multivariante'))
    if menu_met == 'Lineal':
        x = st.text_input('Ingrese los valores de X', value='1.21, 3.00, 5.16, 8.31, 10.21')
        y = st.text_input('Ingrese los valores de Y', value='1.69, 5.89, 4.11, 5.49, 8.65')

        x = x.replace(" ", "")
        y = y.replace(" ", "")

        x = x.split(',')
        y = y.split(',')

        if len(x) == len(y):
            for i in range(0, len(x)):
                x[i] = float(x[i])
            for i in range(0, len(y)):
                y[i] = float(y[i])
                
            parameter = liner_fitting(x,y)
            draw_data = calculate(x,parameter[0],parameter[1])
            draw(x,draw_data,y)
        else:
     
            st.write("Los valores en X y en Y deben ser del mismo tamaño")

    if menu_met == 'Polinomial':
        x = st.text_input('Ingrese los valores de X', value='0, 1, 2, 3, 4, 5')
        y = st.text_input('Ingrese los valores de Y', value='2.1, 7.7, 13.6, 27.2, 40.9, 61')

        x = x.replace(" ", "")
        y = y.replace(" ", "")

        x = x.split(',')
        y = y.split(',')

        if len(x) == len(y):
            for i in range(0, len(x)):
                x[i] = float(x[i])
            for i in range(0, len(y)):
                y[i] = float(y[i])
                
            data=polynomial_fitting(x,y)
            parameters=calculate_parameter(data)
            for w in parameters:
                st.text(w)
            newData=calculateF(x,parameters)
            drawF(x,newData,y)
        else:
     
            st.write("Los valores en X y en Y deben ser del mismo tamaño")
        
    if menu_met == 'Multivariante':
        x1 = st.text_input('Ingrese los valores de X', value='2, 4, 5, 8, 9')
        x2 = st.text_input('Ingrese los valores de X', value='3, 5, 7, 9, 12')
        y = st.text_input('Ingrese los valores de Y', value='48, 50, 51, 55, 56')

        x1 = x1.replace(" ", "")
        x2 = x2.replace(" ", "")
        y = y.replace(" ", "")

        x1 = x1.split(',')
        x2 = x2.split(',')
        y = y.split(',')

        if len(x1) == len(x2)== len(y):
            for i in range(0, len(x1)):
                x1[i] = float(x1[i])
            for i in range(0, len(x2)):
                x2[i] = float(x2[i])
            for i in range(0, len(y)):
                y[i] = float(y[i])
            data = multivariatel_liner_fitting(x1, x2, y)
            data2 = calculate_parameter(data)
            newY = calculateM(x1, x2, data2)
            drawM([x1, x2], y, newY)  



def calculate_parameter(data):
         #i se usa para controlar elementos de columna, línea es un elemento de línea, j se usa para controlar el número de bucles y los datos se usan para almacenar variables locales. Guardar el valor modificado
    i = 0;
    j = 0;
    line_size = len(data)
 
       #Convierta el determinante al determinante triangular superior
    while j < line_size-1:
        line = data[j]
        temp = line[j]
        templete=[]
        for x in line:
            x=x/temp
            templete.append(x)
        data[j]=templete
                 #flag sign el número de líneas que deben eliminarse
        flag = j+1
        while flag < line_size:
            templete1 = []
            temp1=data[flag][j]
            i = 0
            for x1 in data[flag]:
                if x1!=0:
                   x1 = x1-(temp1*templete[i])
                   templete1.append(x1)
                else:
                   templete1.append(0)
                i += 1
            data[flag] = templete1
            flag +=1
        j += 1
 
 
         #Buscando el valor del parámetro correspondiente
 
    parameters=[]
    i=line_size-1
         #j Identificación menos el número de elementos
         #flag_rolIdentifique qué columna excepto
    flag_j=0
    rol_size=len(data[0])
    flag_rol=rol_size-2
         #Obtener la cantidad de soluciones
    while i>=0:
        operate_line = data[i]
        if i==line_size-1:
            parameter=operate_line[rol_size-1]/operate_line[flag_rol]
            parameters.append(parameter)
        else:
            flag_j=(rol_size-flag_rol-2)
            temp2=operate_line[rol_size-1]
                         #result_flag es la bandera para acceder a la solución que se ha resuelto
            result_flag=0
            while flag_j>0:
                temp2-=operate_line[flag_rol+flag_j]*parameters[result_flag]
                result_flag+=1
                flag_j-=1
            parameter=temp2/operate_line[flag_rol]
            parameters.append(parameter)
        flag_rol-=1
        i-=1
    return parameters


def multivariatel_liner_fitting(data_x1,data_x2,data_y):
    size = len(data_x1)
    sum_x1 = 0
    sum_x2 = 0
    sum_square_x1 = 0
    sum_square_x2 = 0
    sum_x1x2 = 0
    sum_y = 0
    sum_x1y = 0
    sum_x2y = 0
    i = 0
    while i < size:
        sum_x1 += data_x1[i]
        sum_x2 += data_x2[i]
        sum_y += data_y[i]
        sum_x1y += data_x1[i]*data_y[i]
        sum_x2y += data_x2[i]*data_y[i]
        sum_x1x2 += data_x1[i]*data_x2[i]
        sum_square_x1 += data_x1[i]*data_x1[i]
        sum_square_x2 += data_x2[i]*data_x2[i]
        i += 1
    return [[size, sum_x1, sum_x2, sum_y]
        ,[sum_x1, sum_square_x1, sum_x1x2, sum_x1y]
        ,[sum_x2, sum_x1x2, sum_square_x2,sum_x2y]]


def polynomial_fitting(data_x,data_y):
            size=len(data_x)
            i=0
            sum_x = 0
            sum_sqare_x =0
            sum_third_power_x = 0
            sum_four_power_x = 0
            average_x = 0
            average_y = 0
            sum_y = 0
            sum_xy = 0
            sum_sqare_xy = 0
            while i<size:
                sum_x += data_x[i]
                sum_y += data_y[i]
                sum_sqare_x += math.pow(data_x[i],2)
                sum_third_power_x +=math.pow(data_x[i],3)
                sum_four_power_x +=math.pow(data_x[i],4)
                sum_xy +=data_x[i]*data_y[i]
                sum_sqare_xy +=math.pow(data_x[i],2)*data_y[i]
                i += 1;
            average_x=sum_x/size
            average_y=sum_y/size
            return [[size, sum_x, sum_sqare_x, sum_y]
                , [sum_x, sum_sqare_x, sum_third_power_x, sum_xy]
                , [sum_sqare_x,sum_third_power_x,sum_four_power_x,sum_sqare_xy]]

def liner_fitting(data_x,data_y):
      size = len(data_x);
      i=0
      sum_xy=0
      sum_y=0
      sum_x=0
      sum_sqare_x=0
      average_x=0;
      average_y=0;
      while i<size:
          sum_xy+=data_x[i]*data_y[i];
          sum_y+=data_y[i]
          sum_x+=data_x[i]
          sum_sqare_x+=data_x[i]*data_x[i]
          i+=1
      average_x=sum_x/size
      average_y=sum_y/size
      return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
      return_b=average_y-average_x*return_k
      return [return_k,return_b]
 
def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay

def calculateF(data_x,parameters):
    datay=[]
    for x in data_x:
        datay.append(parameters[2]+parameters[1]*x+parameters[0]*x*x)
    return datay

def calculateM(data_x1,data_x2,parameters):
    datay=[]
    i = 0
    while i < len(data_x1):
        result = parameters[2]+parameters[1]*data_x1[i]+parameters[0]*data_x2[i]
        i += 1
        datay.append(result)
    return datay

def draw(data_x,data_y_new,data_y_old):
    plt.plot (data_x, data_y_new, label = "curva de ajuste")
    plt.scatter (data_x, data_y_old, label = "datos discretos")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title ("Datos de ajuste lineal de una variable")
    plt.legend(loc="upper left")
    st.pyplot(plt,figsize=(2, 2))


def drawF(data_x,data_y_new,data_y_old):
    plt.plot (data_x, data_y_new, label = "curva de ajuste")
    plt.scatter (data_x, data_y_old, label = "datos discretos")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title ("Datos de ajuste polinomial de una variable")
    plt.legend(loc="upper left")
    st.pyplot(plt,figsize=(2, 2))

def drawM(data_x,old_y,new_y):
        #Crear objeto de función de dibujo
    fig = plt.figure()
        #Cree un objeto Axes3D para incluir las coordenadas 3D de la imagen
    ax = Axes3D(fig)
    ax.scatter(data_x[0], data_x[1], old_y, color='red')
    ax.plot(data_x[0], data_x[1], new_y, color='black')
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title ("Datos de ajuste lineal multivariante")
    st.pyplot(plt,figsize=(2, 2))