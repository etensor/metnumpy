import numpy as np
import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations +
                   (implicit_multiplication_application,))



def def_mtr():
    #dims = int(st.text_input('Dimensiones matriz n x n '),value='3')
    dims = int(input('dimensiones matriz n x n '))

    nums = [x for x in range(9)]
    mtr = np.array(nums).reshape((3,3))
    mtr2 = np.array(nums[::-1]).reshape((3,3))
    print(mtr, mtr2, sep='\n\n')
    mul = mtr*mtr2
    mul_2 = np.matmul(mtr,mtr2,)
    suma = mtr+mtr2
    print(f'mul: {mul}\n,{mul_2},\n{suma}')



def_mtr()