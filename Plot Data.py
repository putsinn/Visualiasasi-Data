import matplotlib.pyplot as plt
plt.axis([0,5,0,20]) #batas sumbu x dan sumbu y
plt.plot([1,2,3,4],[1,4,9,16],'ro-') #nilai data yang di plot
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.title('Plot Data persamaan Kuadrat',fontsize=20,fontname='Times New Roman')
plt.xlabel('x',fontsize=16,fontname='Times New Roman',color='blue')
plt.ylabel('y',fontsize=16,fontname='Times New Roman',color='blue')
plt.grid(True)
plt.legend(['First series'])
plt.savefig('grafik.png')
plt.show()
