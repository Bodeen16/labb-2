import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


"""
#Uppgift a; 
N = 4
L = 1
k = 2
Ta = 2
Tb = 2
h = L / N

def q(x):
    return 50 * (x**3) * np.log(x +1)

x = np.linspace(0, L, N+1) [1:N]

faktor = k / (h**2)

A = faktor * np.array([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])

b = -q(x)

b[0] = b[0] - faktor * Ta
b[-1] = b[-1] - faktor * Tb

print("Systemmatrisen A:")
print(A)

print("Högerledet b:")
print(b)

#Vi får meddetta utskriften: 
#Systemmatrisen A:
#[[-64.  32.   0.]
 #[ 32. -64.  32.]
 #[  0.  32. -64.]]
#Högerledet b:
#[-64.1743309   -2.53415693 -75.80439553]
"""


"""
#Uppgift b; 

N = 6 #Valfritt / Generellt
L = 1
k = 2
Ta = 2 
Tb = 2 
h = L/N

def q(x):
    return 50*(x**3)*np.log(x +1)

x = np.linspace(0, L, N+1)[1:N]
faktor = k / (h**2)

hd = -2 * np.ones(N-1)
sd = np.ones(N-2)

A = faktor * (np.diag(hd, 0) + np.diag(sd, 1) + np.diag(sd, -1))

b = -q(x)

b[0] = b[0] - faktor * Ta
b[-1] = b[-1] - faktor * Tb

print("Generell Systemmatris A:")
print(A)

print("Generellt Högerled b:")
print(b)

#Vi får därmed olika matriser beroende på vilket värde vi anger N. 
# I detta fall då N = 6 får vi utskriften: 
#Generell Systemmatris A:
#[[-144.   72.    0.    0.    0.]
 #[  72. -144.   72.    0.    0.]
 #[   0.   72. -144.   72.    0.]
 #[   0.    0.   72. -144.   72.]
 #[   0.    0.    0.   72. -144.]]
#Generellt Högerled b:
#[-144.03568303   -0.53274458   -2.53415693   -7.56778702 -161.53865172]
"""

"""
#Uppgift c;
L = 1
N = 4
k = 2
Ta = 2 
Tb = 2 

def q(x):
    return 50*(x**3)*np.log(x +1)

def diskretisering_temperatur(N, q, k, Ta, Tb, L):
    h = L / N
    faktor = k / (h**2)

    x = np.linspace(0, L, N+1)[1:N]
    n_inre = N -1

    hd = -2 * np.ones(n_inre)
    sd = np.ones(n_inre - 1)

    diagonaler = [hd, sd, sd]
    offsets = [0, 1, -1]
    A = faktor * sp.sparse.diags(diagonaler, offsets, shape=(n_inre, n_inre), format="csr")

    b = -q(x)

    b[0] = b[0] - faktor * Ta
    b[-1] = b[-1] - faktor * Tb

    return A, b

A, b = diskretisering_temperatur(N, q, k, Ta, Tb, L)
print("Systemmatrisen A:")
print(A.toarray())

print("Högerledet b:")
print(b)

#När vi exempelvis väljer N = 4 får vi utskriften:
#Systemmatrisen A:
#[[-64.  32.   0.]
# [ 32. -64.  32.]
# [  0.  32. -64.]]
#Högerledet b:
#[-64.1743309   -2.53415693 -75.80439553]
"""

"""
# Uppgift d; 

N = 100
L = 1
k = 2
Ta = 2 
Tb = 2 

def q(x):
    return 50*(x**3)*np.log(x +1)

def diskretisering_temperatur(N, q, k, Ta, Tb, L):
    h = L / N
    faktor = k / (h**2)

    x = np.linspace(0, L, N+1)[1:N]
    n_inre = N -1

    hd = -2 * np.ones(n_inre)
    sd = np.ones(n_inre - 1)

    diagonaler = [hd, sd, sd]
    offsets = [0, 1, -1]
    A = faktor * sp.sparse.diags(diagonaler, offsets, shape=(n_inre, n_inre), format="csr")

    b = -q(x)

    b[0] = b[0] - faktor * Ta
    b[-1] = b[-1] - faktor * Tb

    return A, b

A, b = diskretisering_temperatur(N, q, k, Ta, Tb, L)

T = sp.sparse.linalg.spsolve(A, b)

x = np.linspace(0, L, N +1)
T_all = np.concatenate(([Ta], T, [Tb]))

plt.plot(x, T_all, ".-")
plt.xlabel("x")
plt.ylabel("T(x)")
plt.grid(True)
plt.show()

#Utifrån det plottade grafen ser vi att temperaturen vid x = 0.2 är ca 2.1261.
"""