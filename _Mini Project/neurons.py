import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

import seaborn as sns
import matplotlib.pyplot as plt

class Neuron(object):
    def __init__(self, I_ext=0):
        self.I_ext = I_ext
        self.type = False
        # print('Neuron __init__() called')

    def self_identifies(self):
        if not self.type:
            return "I'm a neuron!"
        else:
            return "I'm a %s neuron!" % self.type

    def plot(self, y, t, ax=None, save=[False,None]):
        singleplt = False
        # print(ax)
        if ax is None:
            singleplt = True
            # ax = plt.gca()
        # ax.plot(t,y[0])

        sns.set_style('darkgrid')

        # plt.legend(self.legend)
        plt.xlabel('Time (ms)')
        plt.ylabel('v, w')
        plt.title(y[2])
        # if y[2]:
        #     plt.title(y[2])
        # else:
        #     plt.title("Applied current: %s mA/cm2" % y[1])
        # plt.show()

        if singleplt:
            plt.plot(t,y[0])
            plt.legend(self.legend)
            if save[0] == True:
                plt.savefig('Figures/'+save[1]+'.eps', format='eps')
                print('Figure saved as '+save[1])
            return plt.show()
        else:
            ax.plot(t,y[0])
            plt.legend(self.legend)
            return ax
        # return fig

class FHN_Neuron(Neuron):
    # Fitzhugh-Nagumo equations:
    #           dv/dt = v - (v^3 / 3) - w + i
    #           dw/dt = (v + alpha - beta*w) / tau
    # v = membrane voltage
    # w = relaxation or recovery variable
    # I = input current
    # a, b, tau parameters of the model
    # 𝑎 = 0.7, 𝑏 = 0.8 and 𝜏 = 12.5.
    #x0=[0.7,-0.5]
    def __init__(self, I_ext=1, a=0.7, b=0.8, tau=12.5, x0=[0.7,-0.5]):
        super().__init__()
        self.a = a
        self.b = b
        self.tau = tau
        self.x0 = x0
        self.legend = ['v','w']

        self.type = "FitzHugh-Nagumo"
        # print(self.a, self.b, self.tau)

        # self.I_ext = I_ext
        # print('FHN Neuron __init__() called')

    def dx_dt(self, x, t, I):
        if t < 50 or t > 200:
            I = 0

        # print(t, I)
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return [dvdt,dwdt]

    def solve(self, I, t):
        y = odeint(self.dx_dt, self.x0, t, args=(I,))
        title = ("I = %s, a = %s, b = %s, tau = %s" % (I,self.a,self.b,self.tau))
        # print(y)
        return y, I, title

    def solve_ss(self, t, I=0):
        eq = fsolve(self.dx_dt, self.x0, args=(t,I))
        return "Roots: v = %s, w = %s" % (eq[0], eq[1])

class Rinzel_Neuron(FHN_Neuron):
    def __init__(self, I_ext=1, e=0.0001, c=-0.775, x0=[0.5,-0.7,-0.5]):
        super().__init__()
        self.I_ext = I_ext
        self.e  = e
        self.c  = c
        self.x0 = x0
        self.legend = ['v', 'w', 'z']

        self.type = "Rinzel"

        # print('Rinzel Neuron __init__() called')

    def dx_dt(self, x, t, I):
        # x = [v,w,z]
        dvdt = x[0] - (x[0]**3/3) - x[1] + x[2] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        dzdt = self.e* (-x[0] + self.c - x[2])
        return [dvdt,dwdt,dzdt]

    def solve(self, I, t):
        # print(I, t, z)
        y = odeint(self.dx_dt, self.x0, t, args=(I,))
        title = "Applied current: %s mA/cm2, e = %s, c = %s" % (I,self.e,self.c)
        return y, I, title

    def solve_ss(self, t, I=0):
        eq = fsolve(self.dx_dt, self.x0, args=(t,I))
        return "Roots: v = %s, w = %s, z = %s" % (eq[0], eq[1], eq[2])
