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

"""
#Uppgift 1.2a; 

h = 0.2 
f = lambda t, y: 1 + t - y 
t0 = 0
y0 = 1
T = 1.2
yht = []

while h >= 0.0125: 
    N = int(((T/h)))

    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0
    y[0] = y0

    for j in range(N):
        t[j+1] = t[j] + h
        y[j+1] = y[j] + h*f(t[j], y[j])

    yht.append(y[-1])
    print("h =",h, "yh =",y[-1])
    h = h/2

# Vi får utskriften: 
#h = 0.2 yh = 1.32768
#h = 0.1 yh = 1.4138105960899996
#h = 0.05 yh = 1.457356867725024
#h = 0.025 yh = 1.4792404381364943
#h = 0.0125 yh = 1.490208703749873
"""

"""
#Uppgift 1.2b;

h = 0.2 
f = lambda t, y: 1 + t - y 
g = lambda t: np.exp(-t) + t
t0 = 0
y0 = 1
T = 1.2
yht = []

while h >= 0.0125: 
    N = int(round(T/h))

    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0
    y[0] = y0

    for j in range(N):
        t[j+1] = t[j] + h
        y[j+1] = y[j] + h*f(t[j], y[j])

    yht.append(y[-1])
    eh = np.abs(yht[-1] - g(T))
    print("h =", h, "eh =", eh)
  
    h = h/2

#Vi får utskriften: 
#h = 0.2 eh = 0.03905021191220226
#h = 0.1 eh = 0.018764675431202527
#h = 0.05 eh = 0.009205187573429363
#h = 0.025 eh = 0.004559784729120109
#h = 0.0125 eh = 0.0022693669592026566
#Dessa värden stämmer överens med de verifierade värdena
"""

"""
#Uppgift 1.2c; 
h = 0.2 
f = lambda t, y: 1 + t - y 
g = lambda t: np.exp(-t) + t
t0 = 0
y0 = 1
T = 1.2
yht = []
eht = []

while h >= 0.0125: 
    N = int(round(T/h))

    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0
    y[0] = y0

    for j in range(N):
        t[j+1] = t[j] + h
        y[j+1] = y[j] + h*f(t[j], y[j])

    yht.append(y[-1])
    eh = np.abs(yht[-1] - g(T))
    eht.append(eh)

    if len(yht) >= 2: 
        ehf = eht[-2]/eht[-1]
        p = np.log(ehf) * 1/(np.log(2))
        print("p =", p)

    h = h/2

#Vi får utskriften: 
#p = 1.0573110409669717
#p = 1.0275003117582744
#p = 1.0134814042897493
#p = 1.0066758019830548
#Dessa värden stämmer överens med de verifierade värdena

"""

