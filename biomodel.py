from scipy.integrate import odeint
import numpy as np
#import matplotlib.pyplot as plt

def elim(x, t):
    k1 = 1
    k2 = 1
    k3 = 1
    k4 = 1
    k5 = 1

    no3 = x[0]
    no2 = x[1]
    no = x[2]
    nh4 = x[3]

    dno3dt = -k3*no3
    dno2dt = -k1*no2 + k3*no3 - k4*no2
    dnodt = k1*no2 - k2*no*nh4 + k4*no2 -2*k5*no**2
    dnh4dt = -k2*nh4

    return [dno3dt, dno2dt, dnodt, dnh4dt]

x0 = [17, 0.1, 0, 1]
t = np.linspace(0, 15, 1000)
x = odeint(elim, x0, t)
f = open('plot.dat', 'w+')
for i in range(len(x)):
    f.write(str(t[i])+'\t'+str(x[i,0])+'\t'+str(x[i,1])+'\t'+str(x[i,3])+'\t'+str(x[i,2])+'\n')
f.close()
