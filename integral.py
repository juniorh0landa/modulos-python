import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import timeit

#definição da função de sexto grau
def fun_sex(x):
    return x**6 + x**5 + x**4 + x**3 + x**2 + x**1 + x**0

#método da integração pelo método do trapézio
def int_trap(x,y,intervalos):
    area = np.zeros(intervalos - 1)
    for i in range(len(area)):
        ym = (y[i] + y[i+1])/2
        area[i] = ym*(x[i+1] - x[i])
    return sum(area)

xgraph = []
ygraphM = []
ygraphS = []

integral, erro = integrate.quad(fun_sex,0,25)
print('\nINTEGRAL ANALÍTICA (Scipy): {:f}; Erro: {:.10f}'.format(integral,erro))

print("\nINTEGRAÇÃO NUMÉRICA (TRAPÉZIO)\n\n\tManual\t\tScipy\nN:\tDuração:\tDuração:\tIntegral:\t\t|Erro|:")
for i in range(10,4011,400):
    inM = timeit.default_timer()
    x = np.linspace(0,25,i)
    y = fun_sex(x)
    intM = int_trap(x,y,i)
    fiM = timeit.default_timer()
    inS = timeit.default_timer()
    intS = integrate.trapz(y,x)
    fiS = timeit.default_timer()
    xgraph.append(i)
    ygraphM.append(fiM - inM)
    ygraphS.append(fiS - inS)
    print("{:d}\t{:.10f}\t{:.10f}\t{:f}\t{:f}".format(i,fiM - inM,fiS - inS,intM,abs(integral-intM)))

plt.plot(xgraph,ygraphM,'b-')
plt.plot(xgraph,ygraphS,'r-.')