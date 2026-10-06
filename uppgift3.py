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

"""
#Uppgift e; 

N = 50 
L = 1
k = 2
Ta = 2 
Tb = 2 

N_ts = [N, 2*N, 4*N, 8*N, 16*N, 32*N, 64*N, 128*N]
T_vd = []
p_vd = []

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

for N in N_ts: 
    A, b = diskretisering_temperatur(N, q, k, Ta, Tb, L)
    T = sp.sparse.linalg.spsolve(A, b)
    T_all = np.concatenate(([Ta], T, [Tb])) 

    T_vd.append(float(T_all[int(0.7 * N)]))

print("T-värden vid x = 0.7:", T_vd)


for i in range(len(T_vd) -2):
    fel1 = abs(T_vd[i] - T_vd[i+1])
    fel2 = abs(T_vd[i+1] - T_vd[i+2])
    p = np.log(fel1 /fel2)/np.log(2)
    p_vd.append(float(p))



print("Noggrannhetsordning p:", p_vd)

#Vi får utskriften: 
#T-värden vid x = 0.7: [2.3617929540928917, 2.3619824369781885, 2.3620298106197546, 2.362041654212619, 2.3620446151215, 2.3620453553476666, 2.362045540407259, 2.3620455866580436]
#Noggrannhetsordning p: [1.9999110655605556, 1.9999777724128491, 1.999994803431534, 2.000002053676341, 1.999976215530155, 2.0004401766081985]
#Vi ser alltså att det konvergerar mot 2.3620456 samt att noggrannhetsordningen är ca 2 vilket stämmer överens med teorin. 
"""

"""
#Uppgift f;
N = 400
L = 1
k = 2
id_x = int(0.7 *N)
x = np.linspace(0, L, N+1)

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


A, b = diskretisering_temperatur(N, q, k, 2.0, 2.0, L)
T = sp.sparse.linalg.spsolve(A, b)
T_all_0 = np.concatenate(([2.0], T, [2.0]))
v0 = float(T_all_0[id_x])

A, b = diskretisering_temperatur(N, q, k, 2.2, 2.0, L)
T = sp.sparse.linalg.spsolve(A, b)
T_all_1 = np.concatenate(([2.2], T, [2.0]))
v1 = float(T_all_1[id_x])

A, b = diskretisering_temperatur(N, q, k, 2.0, 2.3, L)
T = sp.sparse.linalg.spsolve(A, b)
T_all_2 = np.concatenate(([2.0], T, [2.3]))
v2 = float(T_all_2[id_x])

os_Ta = abs(v1 - v0)
os_Tb = abs(v2 - v0)
T_os = os_Ta + os_Tb
print("Total osäkerhet i punkten T(0.7):", T_os)
plt.plot(x, T_all_0, label="Ta = 2.0, Tb = 2.0")
plt.plot(x, T_all_1, label="Ta = 2.2, Tb = 2.0")
plt.plot(x, T_all_2, label="Ta = 2.0, Tb = 2.3")
plt.grid(True)
plt.legend()
plt.show()

#Vi får utskriften: 
#Total osäkerhet i punkten T(0.7): 0.2699999999999947
"""