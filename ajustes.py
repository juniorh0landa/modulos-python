import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import timeit

#função de até 4° grau
def function(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

#definindo pontos aleatorios
x_data = np.array(np.linspace(-20,25,10))
y_ans = function(x_data,0,-3,1,2,0)
y_noise = 10*np.random.normal(size=x_data.size)
y_data = y_ans + y_noise
plt.plot(x_data,y_data,'ro')

#Resolução manual
inM = timeit.default_timer()
A = []
for i in x_data:
    aux = []
    for j in range(4,-1,-1):
        aux.append(i**j)
    A.append(aux)

A=np.array(A)
g=y_data

A_t = np.transpose(A)
m = np.dot(A_t,A)
m_inv = np.linalg.inv(m)
n = np.dot(m_inv,A_t)
B = np.dot(n,g)
fiM = timeit.default_timer()

#resolução scipy
inS = timeit.default_timer()
popt, pcov = curve_fit(function,x_data,y_data)
fiS = timeit.default_timer()

#plotando as funções
fx = np.poly1d(B)
plt.plot(x_data,fx(x_data),'b-')
sx = np.poly1d(popt)
plt.plot(x_data,sx(x_data),'g-.')
print("\nManual: (Duração: {:.10f})\n".format(fiM-inM),fx)
print("\n\nScipy: (Duração: {:.10f})\n".format(fiS-inS),np.poly1d(popt))