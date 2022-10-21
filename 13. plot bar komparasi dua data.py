import matplotlib.pyplot as plt
import numpy as np
x0 = np.arange(8)
y1 = np.array([4,3,2,1,2,4,6,6])
y2 = np.array([5,4,2,1,3,4,5,6])
plt.ylim(-7,7)
plt.bar(x0,y1,0.9,facecolor='r')
plt.bar(x0,-y2,0.9,facecolor='g')
plt.xticks(())
plt.grid(True)
for x, y in zip(x0,y1):
    plt.text(x + 0.4, y+0.05, '%d' % y, ha='center', va= 'bottom')
for x, y in zip(x0, y2):
    plt.text(x + 0.4, -y - 0.05, '%d' % y, ha='center', va= 'top')
plt.show()
