import numpy as np
import matplotlib.pyplot as plt
from random import random

#numeros aleatorios de theta entre 0 y pi/2
#numeros aleatorios de v entre 35 y 45

randomtheta = np.random.uniform(0, np.pi/2,1000000)
randomvel = np.random.uniform(35, 45, 1000000)

#funcion de alcance

def alcancep(vinicial, theta):
    g = 9.8
    dis = ((vinicial**2)*np.sin(2*theta))/g
    return dis
alcance = alcancep(randomvel, randomtheta)

#histograma de velocidad inicial

histvel = plt.hist(randomvel, bins =100)
plt.ylabel("freq")
plt.xlabel("vel inicial")
plt.savefig("histogramavelinicial.pdf")


#seleccionar distancias
d1 = np.where((alcance<66) & (alcance>56))
V1 = randomvel[d1]
x1 = len(V1)
theta1 = np.random.uniform(0, np.pi/2, x1)
alcance1 = alcancep(V1, theta1)

d2 = np.where((alcance1<120) & (alcance1>110))
V2 = V1[d2]
x2 = len(V2)
theta2 = np.random.uniform(0, np.pi/2, x2)
alcance2 = alcancep(V2, theta2)

d3 = np.where((alcance2<36) & (alcance2>26))
V3 = V2[d3]
x3 = len(V3)
theta3 = np.random.uniform(0, np.pi/2, x3)
alcance3 = alcancep(V3, theta3)

d4 = np.where((alcance3<172) & (alcance3>182))
V4 = V3[d4]
x4 = len(V4)
theta4 = np.random.uniform(0, np.pi/2, x4)
alcance4 = alcancep(V4, theta4)



plt.figure()
plt.hist(V1, bins = 50)
plt.ylabel("freq")
plt.xlabel("vel")
plt.title("Velocidad 1 ")
plt.savefig("velocidad1.pdf")

plt.figure()
plt.hist(V2, bins = 50)
plt.ylabel("freq")
plt.xlabel("vel")
plt.title("Velocidad 2")
plt.savefig("velocidad2.pdf")

plt.figure()
plt.hist(V3, bins = 50)
plt.ylabel("freq")
plt.xlabel("vel")
plt.title("Velocidad 3")
plt.savefig("velocidad3.pdf")

plt.figure()
plt.hist(V4, bins = 50)
plt.ylabel("freq")
plt.xlabel("vel")
plt.title("Velocidad 4")
plt.savefig("velocidad4.pdf")
plt.show()






