import matplotlib.pyplot as plt
labels = ['Lain-lain','samsung','Apple','Huawei','Oppo','Vivo']
values = [42,21,14,9,8,7]
colors = ['red','green','pink','blue','yellow','orange']
explode = [0,1,0,0,0,0] #fokus pada samsung
plt.title('Diagram Pie Market Share Samsung')
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
plt.axis('equal')
plt.show()
