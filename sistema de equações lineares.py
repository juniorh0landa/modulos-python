import numpy as np
import timeit

#Método de resolução Gauss-Seidel
def gauss_seidel(A,b,tol = 1e-5):
    n=np.shape(A)[0]  
    x0 = np.zeros_like(b)
    x = np.copy(x0)  
    it = 0   
    while (it < 10000):  
        it = it+1
        for i in np.arange(n):  
            x[i] = b[i]  
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                x[i] -= A[i,j]*x[j]  
            x[i] /= A[i,i] 
        #tolerancia  
        if (np.linalg.norm(x-x0,np.inf) < tol):  
            return x
        #prepara nova iteração 
        x0 = np.copy(x)
  
#Gerando a matriz:
M = 20
A = np.around(np.random.rand(M,M),2)*10 + np.diagflat(np.random.randint(3*M + 1, 2*(3*M + 1), M))
B = np.around(np.random.rand(M,1),2)*10
for i in range(M):
    for j in range(M):
        A[i,j]=((-1)**np.random.choice(10))*A[i,j]
    B[i,0]=((-1)**np.random.choice(10))*B[i,0]

#Gauss-seidel:
inM = timeit.default_timer()
resp1 = gauss_seidel(A,B)
fiM = timeit.default_timer()

#Numpy:
inN = timeit.default_timer()
resp2 = np.linalg.solve(A,B)
fiN = timeit.default_timer()

#Resultados:
print("\nSISTEMA DE EQUAÇÕES LINEARES\nGauss-Seidel: (Duração {:f})\n".format(fiM - inM),np.transpose(resp1), "\n\nNumpy: (Duração: {:f})\n".format(fiN - inN), np.transpose(resp2))
print("\nDiferença entre métodos: \n",abs(np.transpose(resp1) - np.transpose(resp2)))