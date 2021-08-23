import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

import matplotlib.pyplot as plt

class Neuron(object):
    def __init__(self, I_ext=0):
        self.I_ext = I_ext
        self.type = None
        print('Neuron __init__() called')

    def self_identifies(self):
        return "I'm a %s neuron!" % self.type

    def plot(self, y, t, title=None):
        # y = self.solve(self.x0, I, t)
        # plot results
        plt.plot(t,y[0])
        plt.xlabel('Time (ms)')
        plt.ylabel('y(t)')
        plt.legend(self.legend)

        if y[2]:
            plt.title(y[2])
        else:
            plt.title("Applied current: %s mA/cm2" % y[1])
        plt.show()
        return None

class FHN_Neuron(Neuron):
    # Fitzhugh-Nagumo equations:
    #           dv/dt = v - (v^3 / 3) - w + i
    #           dw/dt = (v + alpha - beta*w) / tau
    # v = membrane voltage
    # w = relaxation or recovery variable
    # I = input current
    # a, b, tau parameters of the model
    # 𝑎 = 0.7, 𝑏 = 0.8 and 𝜏 = 12.5.
    def __init__(self, I_ext=1, a=0.7, b=0.8, tau=12.5, x0=[0.7,-0.5]):
        super().__init__()
        self.a = a
        self.b = b
        self.tau = tau
        self.x0 = x0
        self.legend = ['v','w']

        self.type = "FitzHugh-Nagumo"

        # self.I_ext = I_ext
        print('FHN Neuron __init__() called')

    def dx_dt(self, x, t, I):
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return [dvdt,dwdt]

    def solve(self, I, t):
        y = odeint(self.dx_dt, self.x0, t, args=(I,))
        title = ("Applied current: %s mA/cm2" % I)
        return y, I, title

    def solve_ss(self, t, I=0):
        eq = fsolve(self.dx_dt, self.x0, args=(t,I))
        return "Roots: ", eq


class Rinzel_Neuron(FHN_Neuron):
    def __init__(self, I_ext=1, e=0.0001, c=-0.775, x0=[0.7,-0.5,0]):
        super().__init__()
        self.I_ext = I_ext
        self.e  = e
        self.c  = c
        self.x0 = x0
        self.legend = ['v', 'w', 'z']

        self.type = "Rinzel"

        print('Rinzel Neuron __init__() called')

    def dx_dt(self, x, t, I, z):
        dvdt = x[0] - (x[0]**3/3) - x[1] + z + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        dzdt = self.e* (-x[0] + self.c - z)
        return [dvdt,dwdt,dzdt]

    def solve(self, I, t, z=0):
        # print(I, t, z)
        y = odeint(self.dx_dt, self.x0, t, args=(I,z,))
        title = "Applied current: %s mA/cm2, z = %s, e = %s, c = %s" % (I,z,self.e,self.c)
        return y, I, title

    def solve_ss(self, t, I=0):
        eq = fsolve(self.dx_dt, self.x0, args=(t,I))
        return "Roots: ", eq
