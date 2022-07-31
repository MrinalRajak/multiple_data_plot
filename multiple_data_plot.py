

#multiple data plot using matplotlib

import numpy as np
import matplotlib.pyplot as plt
v=np.loadtxt("data2.txt")
v1=np.loadtxt("data1.txt")
x,y=v[:,0],v[:,1]
x1,y1=v1[:,0],v1[:,1]
fig,(ax0,ax1)=plt.subplots(ncols=2)
ax0.plot(x,y,lw=2,ls='-.',c='r')
ax0.set_xlim(0,11)
ax0.set_ylim(0,110)
ax0.legend("velocity")
ax0.set_xlabel('Time(sec)',fontsize=20)
ax0.set_ylabel('Distance(m)',fontsize=20)
ax0.set_title(r'$\delta-\tau$',fontsize=25)
ax0.set_xticks([1,4,7,9,10])
ax0.set_yticks([4,8,13,22,35])
ax1.legend(loc='best',shadow='Time',fancybox='Time')
ax1.plot(x1,y1,lw=2,ls='-.',c='blue')
ax1.set_xlim(0,11)
ax1.set_ylim(4,210)
ax1.legend('velocity')
ax1.set_xlabel('Time(sec)',fontsize=20)
ax1.set_ylabel('Distance(m)',fontsize=20)
ax1.set_title(r'$\alpha-\gamma$',fontsize=25)
ax1.set_xticks([0,2,7,9,10])
ax1.set_yticks([32,45,50,65,95])
fig.subplots_adjust(wspace=0.5)
plt.show()
