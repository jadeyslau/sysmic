import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

import seaborn as sns
import matplotlib.pyplot as plt

A=0.7
B=0.8
TAU=12.5

class Neuron(object):
    def __init__(self, end=800 ):

        self.type = False

        self.start = 0
        self.end = end
        self.t = np.linspace(self.start, self.end, num=3000)
        self.I_on  = self.start+(self.end*0.1)
        self.I_off = self.end-(self.end*0.1)

        # Seaborn graph aesthetics
        sns.set_style('darkgrid')
        sns.set_context('paper')


    def self_identifies(self):
        if not self.type:
            return "I'm a neuron!"
        else:
            return "I'm a %s neuron!" % self.type

    def solve(self, I):
        y = odeint(self.dx_dt, self.x0, self.t, args=(I,))
        title = "Applied current: %s mA/cm2, %s" % (I,self.title)
        return y, I, title

    def solve_ss(self, I=0):
        fsolv = True
        eq = fsolve(self.dx_dt, self.x0, args=(self.t,I,fsolv))
        results = []
        for i, x in enumerate(self.legend):
            results.append({x: eq[i]})
        return "Roots: ", results

    def plot(self, y, ax=None, save=[False,None]):
        singleplt = False

        if ax is None:
            singleplt = True

        plt.xlabel('Time (ms)')
        plt.ylabel(self.label)
        plt.title(y[2])

        if singleplt:
            plt.plot(self.t,y[0][:,0:2])
            plt.legend(self.legend)

            if save[0] == True:
                plt.savefig('Figures/'+save[1]+'.eps', format='eps')
                print('Figure saved as '+save[1])
            return plt.show()
        else:
            ax.plot(self.t,y[0][:,0:2])


            plt.legend(self.legend)
            return ax


class FHN_Neuron(Neuron):
    # Fitzhugh-Nagumo equations:
    #           dv/dt = v - (v^3 / 3) - w + i
    #           dw/dt = (v + alpha - beta*w) / tau
    # v = membrane voltage
    # w = relaxation or recovery variable
    # I = input current
    # a, b, tau parameters of the model
    # 𝑎 = 0.7, 𝑏 = 0.8 and 𝜏 = 12.5.

    def __init__(self, a=A, b=B, tau=TAU, x0=[-1.2, -0.6]):
        super().__init__()
        self.a = a
        self.b = b
        self.tau = tau
        self.x0 = x0
        self.legend = ['v','w']
        self.label  = 'v, w'

        self.type = "FitzHugh-Nagumo"

        self.title = ("a = %s, b = %s, tau = %s" % (self.a,self.b,self.tau))


    def dx_dt(self, x, t, I, fsolv=False):
        if ((not fsolv) and (t < self.I_on or t > self.I_off)):
            I = 0
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return [dvdt,dwdt]

class Rinzel_Neuron(FHN_Neuron):
    def __init__(self, a=A, b=B, tau=TAU, e=0.0001, c=-0.775, x0=[-1.02,-0.4,0.25], end=20000):
        super().__init__('t')
        # self.start = 0
        self.end = end
        self.t = np.linspace(self.start, self.end, num=3000)
        self.I_on  = self.start+(self.end*0.1)
        self.I_off = self.end-(self.end*0.1)

        self.a = a
        self.b = b
        self.tau = tau

        self.e  = e
        self.c  = c
        self.x0 = x0
        self.legend = ['v', 'w', 'z']
        self.label  = ['v, w','z']
        print(self.a, self.b, self.tau, self.e, self.c)
        self.type = "Rinzel"

        self.title = "e = %s, c = %s" % (self.e,self.c)


    def dx_dt(self, x, t, I, fsolv=False):
        # x = [v,w,z]
        if ((not fsolv) and (t < self.I_on or t > self.I_off)):
            I = 0
        dvdt = x[0] - (x[0]**3/3) - x[1] + x[2] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        dzdt = self.e * (-x[0] + self.c - x[2])

        return [dvdt,dwdt,dzdt]

    def plot(self, y, ax=None, save=[False,None]):
        singleplt = False
        if ax is None:
            singleplt = True
            fig,ax = plt.subplots(2, sharex=True, figsize=(40, 10))
        plt.xlabel('Time (ms)')
        plt.suptitle(y[2])


        ax[0].plot(self.t,y[0][:,0:2]);
        ax[0].set_ylabel(self.label[0])
        ax[0].legend(self.legend[0:2])

        ax[1].plot(self.t,y[0][:,2]);
        ax[1].set_ylabel(self.label[1])
        ax[1].legend(self.legend[2])

        return ax
