import numpy as np
import matplotlib.pyplot as plt


a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
x= [-10, 10]
t=np.choose(a, x)
print(t)
y=np.power(x,3)
print("baze",np.square(y))


theta=np.angle([1.0, 1.0j, 1+1j])               # in radians
z=np.angle(1+1j, deg=True)                  # in degrees
u1=np.sin(z)
u2=np.cos(z)
meshPoints =np.linspace(-1,1,num=500)
print(meshPoints)
pi=3.14

print("53th value of meshPoints is {}".format(meshPoints[52]))
plt.plot(meshPoints, np.sin(2 *pi * meshPoints))
plt.show()

plt.savefig("sin.png")
