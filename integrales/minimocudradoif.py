import streamlit as st
import matplotlib.pyplot as plt
from pylab import mpl

def minimo_cuadrado_if():
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
 
def draw(data_x,data_y_new,data_y_old):
    plt.plot (data_x, data_y_new, label = "curva de ajuste")
    plt.scatter (data_x, data_y_old, label = "datos discretos")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title ("Datos de ajuste lineal de una variable")
    plt.legend(loc="upper left")
    st.pyplot(plt,figsize=(2, 2))