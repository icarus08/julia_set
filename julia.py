import numpy as np
from matplotlib import pyplot as plt

size = 20
# X = np.linspace(-2,2,20).reshape(size,2)
c = complex(0.0,0.65)
C = np.array([0.1, -0.3])
Z = np.array([0.4, -0.8])
M = np.zeros((size,1))
N = np.zeros((size,1))
for x in range(1,size):
    Z = Z*Z + C
    if Z[0] > 2 or Z[1] > 2:
        break
    else:
        M[x]=Z[0]
        N[x]=Z[1]
        print(Z)
# print(M)
# print(N)
plt.scatter(M,N)
plt.show()