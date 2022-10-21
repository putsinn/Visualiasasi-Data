import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('file.txt')

plt.plot(data[:,0], data[:,1])
plt.title ('Data "file.text"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

