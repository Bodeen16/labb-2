import numpy as np
import matplotlib.pyplot as plt 

"""
#uppgift 1.1a; 

t0 = 0
y0 = 1

f = lambda t, y: 1 + t - y 
g = lambda t: np.exp(-t) + t

h = 0.1 
N = 12

t = np.zeros(N+1)
y = np.zeros(N+1)

t[0] = t0
y[0] = y0

for j in range(N):
    t[j+1] = t[j] + h
    y[j+1] = y[j] + h*f(t[j], y[j])

plt.plot(t, y, label="f")
plt.plot(t, g(t), label="g")
plt.legend()
plt.grid()
plt.show()
"""


"""
#Uppgift 1.1b; 

t0 = 0
y0 = 1
T = 1.2

f = lambda t, y: 1 + t - y 
g = lambda t: np.exp(-t) + t

h = 0.1 
N = 12

t = np.zeros(N+1)
y = np.zeros(N+1)

t[0] = t0
y[0] = y0

for j in range(N):
    t[j+1] = t[j] + h
    y[j+1] = y[j] + h*f(t[j], y[j])

yh = y[-1]

eh = np.abs(yh - g(T))
print("eh =", eh)

#Vi får utskriften: 
#eh = 0.018764675431202527 vilket kan avrundas till 0.0188.
"""

#Uppgift 1.2a; 

