import numpy as np
import matplotlib.pyplot as plt

###1###
a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
x= [-10, 10]

t=np.choose(a, x)
print(t)
###2###
y=np.power(x,3)
print("baze",np.square(y))
###3####
theta=np.angle([1.0, 1.0j, 1+1j])  # in radians
z=np.angle(1+1j, deg=True)# in degrees
###4###
u1=np.sin(z)
u2=np.cos(z)
###5###
meshPoints =np.linspace(-1,1,num=500)
print(meshPoints)
###6###
print("53th value of meshPoints is {}".format(meshPoints[52]))
###7###
plt.plot(meshPoints, np.sin(2 *np.pi * meshPoints))
plt.show()
plt.savefig("sin.png")

