import numpy as np
import scipy as sp

"""
#Uppgift a; 

def F(t, y, R, L, C):

    q = y[0]
    i = y[1]

    dq_dt = i

    di_dt = -(1/(L*C)) * q - (R/L) * i

    return [dq_dt, di_dt]

#Eftersom dq_dt = i borde d^2q/dt^2 motsvara i'. 
#Uttrycken för i' blir då -(1/(L*C)) * q - (R/L) * i vilket innebär att y' består av i och -(1/(L*C)) * q - (R/L) * i. 
"""


"""
#Uppgift b; 
#t = 0
#y = [1, 2]
#R = 0.5 
#L = 2
#C = 0.5

def f(t, y, R, L, C):

    q = y[0]
    i = y[1]

    dq_dt = i

    di_dt = -(1/(L*C)) * q - (R/L) * i

    return [dq_dt, di_dt]

#print(f(t, y, R, L, C))

#Vi får utskriften: 
#[2, -1.5] 
#Vilket stämmer överens med kontrollsiffrorna. 
"""



