import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
###1###
x=np.array([0,1,2,3,4,5,6,7,8,9,10])
f=((np.e)**((-x)/10))*np.sin((np.pi)*x)
print(f)
g=x*((np.e)**(-x/3))
print(g)

plt.figure()

plt.subplot(211)
plt.plot(f, 'b--')
plt.xlabel('x axies')
plt.ylabel('y axies')
plt.subplot(212)
plt.plot(g,'r--')
plt.xlabel('x axies')
plt.ylabel('y axies')
plt.savefig("EX14.3.soale avval.pdf")

###2###
r0=1
tetha=np.linspace(0,2*np.pi,100)
r=r0+np.cos(tetha)
x=r*np.sin(tetha)
y=r*np.cos(tetha)

plt.figure()
plt.plot(x,y, 'b--')
plt.savefig("EX14.3.soale dovvom.pdf")
plt.show()
