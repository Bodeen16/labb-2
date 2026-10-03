import numpy as np
import matplotlib.pyplot as plt 
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

"""
#Uppgift c; 
def f(t, y, R, L, C):

    q = y[0]
    i = y[1]

    dq_dt = i

    di_dt = -(1/(L*C)) * q - (R/L) * i

    return [dq_dt, di_dt]

t0 = 0
T = 20

#i;
Q0_i = 1 
L_i = 2 
C_i = 0.5 
R_i = 1 
y0_i = [Q0_i, 0]

sol_i = sp.integrate.solve_ivp(f, [t0, T], y0_i, args=(R_i, L_i, C_i))

#ii; 
Q0_ii = 1 
L_ii = 2
C_ii = 0.5
R_ii = 0
y0_ii = [Q0_ii, 0]

sol_ii = sp.integrate.solve_ivp(f, [t0, T], y0_ii, args=(R_ii, L_ii, C_ii))

plt.figure(1)
plt.plot(sol_i.t, sol_i.y[0], label="q(t)")
plt.plot(sol_i.t, sol_i.y[1], label="i(t)")
plt.grid(True)
plt.title("i; Dämpad svängning")
plt.legend()

plt.figure(2)
plt.plot(sol_ii.t, sol_ii.y[0], label="q(t)")
plt.plot(sol_ii.t, sol_ii.y[1], label="i(t)")
plt.grid(True)
plt.title("ii; Odämpad svängning")
plt.legend()

plt.show()
"""

"""
#Uppgift d; 

t0 = 0
T = 20

N_ts = [20, 40, 80, 160]

Q0_i = 1 
L_i = 2 
C_i = 0.5 
R_i = 1 

for N in N_ts: 
    h = (T-t0)/N

    t = np.zeros(N + 1)
    q = np.zeros(N + 1)
    i = np.zeros(N + 1)
    t[0] = t0
    q[0] = Q0_i
    i[0] = 0

    for j in range(N):
        t[j+1] = t[j] + h

        dq_dt = i[j]
        di_dt = -(1/(L_i*C_i)) * q[j] - (R_i/L_i) * i[j]

        q[j+1] = q[j] + h * dq_dt
        i[j+1] = i[j] + h * di_dt

    plt.figure()
    plt.plot(t, q, label="q(t)")
    plt.plot(t, i, label="i(t)")
    plt.legend()
    plt.grid(True)
    plt.title(f"N = {N}")

plt.show()

#Utifrån de fyra graferna ser vi att lösningen växer för N = 20 vilket inebär att den är instabil där. För N = 40 växer den men minskar inte heller, och för N = 80 och N = 160 minskar lösningen.
#Därmed kan man konstatera att N = 40, 80 och 160 ger en numeriskt stabil lösningen då lösningarna inte växer. 
"""
    




