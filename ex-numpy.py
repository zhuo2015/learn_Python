import numpy as np
import random

x11 = np.random.randint(1,100,10)
print(x11)
np.savetxt("numpy_exce_1.txt",x11)
x12 = np.loadtxt("numpy_exce_1.txt")
print(x12)

print(np.min(x12))
print(np.max(x12))
print(np.mean(x12))
print('np.sort: \n', np.sort(x12))
print('x12= ', x12)
print('%' * 20)
print(x12.min())
print(x12.max())
print(x12.mean())
print('x12.sort: ', x12.sort())
print('x12 = ',x12)


    
