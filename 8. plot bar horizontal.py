import matplotlib.pyplot as plt
import numpy as np
index = np.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]
plt.title('Diagram Batang')
plt.barh(index,values,xerr=std,error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
plt.yticks(index+0.4,['A','B','C','D','E'])
plt.legend(loc=5)
plt.show()
