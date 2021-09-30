import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

import seaborn as sns
import matplotlib.pyplot as plt

# Global default parameters
A=0.7
B=0.8
TAU=12.5

class Neuron(object):
    def __init__(self, end=800 ):

        self.type = False

        self.start = 0 # Defines when model starts in time ms
        self.end = end # Defines how long model is run for
        self.t = np.linspace(self.start, self.end, num=3000) # Time span
        self.I_on  = self.start+(self.end*0.1) # Time when current applied
        self.I_off = self.end-(self.end*0.1)  # Time when current switched off

        # Seaborn graph aesthetics
        sns.set_style('darkgrid')
        sns.set_context('paper')

    def self_identifies(self): # Test method for troubleshooting
        if not self.type:
            return "I'm a neuron!"
        else:
            return "I'm a %s neuron!" % self.type

    def solve(self, I):
        """
        Integrate the ordinary differential equations of the system.

        Args:
            I (int): External current applied.

        Returns:
            y (arr)  : Membrane potential at the given times. Either 2 or 3 dimensional depending on neuron type.
            title (str): Title of experiment containing key information.
        """
        y = odeint(self.dx_dt, self.x0, self.t, args=(I,))
        title = "Applied current: %s mA/cm2, %s" % (I,self.title)
        return y, title

    def solve_ss(self, I=0):
        """
        Finds the steady state roots of the system of ODEs when I = 0.

        Args:
            I (int): 0 is default.

        Returns:
            results (arr): Keyed array containing the root for each equation.
        """
        fsolv = True
        eq = fsolve(self.dx_dt, self.x0, args=(self.t,I,fsolv))
        results = []
        for i, x in enumerate(self.legend):
            results.append({x: eq[i]})
        return "Roots: ", results

    def plot(self, y, ax=None, save=[False,None]):
        """
        Plots the results after solving with odeint.

        Args:
            y (arr)   : Array containing y values in y[0], and the title of plot in y[1].
            save (arr): save[0] (boolean) True for save or False for not save, save[1] (str), filename.

        Returns:
            results (plot): Plot or ax
        """
        singleplt = False

        if ax is None:
            singleplt = True

        plt.xlabel('Time (ms)')
        plt.ylabel(self.label)
        plt.title(y[1])

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

    def __init__(self, a=A, b=B, tau=TAU, x0=[-1.20, -0.62]):
        """
        Inits FHN_Neuron class with following variables.

        Args:
            a   (int): Parameter a from model. Default is globally set.
            b   (int): Parameter b from model. Default is globally set.
            tau (int): Parameter tau from model. Default is globally set.
            x0  (arr): Initial conditions for FHN model.
        """
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
        """
        Derivative calculation for FHN values passed to it via odeint or fsolve.

        Args:
            x (arr): x = [v,w].
            t (arr): time span.
            I (int): Applied current.
            fsolve (bool): Using fsolve or not.

        Returns:
            results (arr): 2D array containing dvdt and dwdt.
        """
        if ((not fsolv) and (t < self.I_on or t > self.I_off)):
            I = 0
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return [dvdt,dwdt]

    def plot_nullclines(self, I, ax, vmin=-1, vmax=1):
        """
        Plots nullclines for FHN model

        Args:
            I (int)   : Applied current.
            vmin (int): Minimum of y axis.
            vmax (int): Maximum of y axis.

        Returns:
            None : (TODO. Bad practice, prob.)
        """
        V = np.linspace(vmin,vmax,100)
         # Plot a nullcline for dV/dt = 0
        ax.plot(V, ((V - V**3) + I), label='dV/dt=0')

        # Plot a nullcline for dw/dt = 0
        ax.plot(V, ((V+self.a)/self.b), label='dw/dt=0')
        ax.set(xlabel='V', ylabel='w');
        # ax.title('Nullclines: %s' % self.title)
        ax.legend()
        return None

class Rinzel_Neuron(FHN_Neuron):
    def __init__(self, a=A, b=B, tau=TAU, e=0.0001, c=-0.775, x0=[-1.03,-0.41,0.25], end=20000):
        """
        Inits Rinzel_Neuron class with following variables.

        Args:
            a   (int): Parameter a from model. Default is globally set.
            b   (int): Parameter b from model. Default is globally set.
            tau (int): Parameter tau from model. Default is globally set.
            e   (int): Parameter e from model.
            c   (int): Parameter c from model.
            x0  (arr): Initial conditions for Rinzel model.
        """
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
        # print(self.a, self.b, self.tau, self.e, self.c)
        self.type = "Rinzel"

        # self.title = "e = %s, c = %s" % (self.e,self.c)
        self.title = "a = %s, b = %s, tau = %s, e = %s, c = %s" % (self.a,self.b,self.tau,self.e,self.c)


    def dx_dt(self, x, t, I, fsolv=False):
        """
        Derivative calculation for Rinzel values passed to it via odeint or fsolve.

        Args:
            x (arr): x[0] is v and x[1] is w. x = [v,w,z].
            t (arr): time span.
            I (int): Applied current.
            fsolve (bool): Using fsolve or not.

        Returns:
            results (arr): 3D array containing dvdt, dwdt, and dzdt.
        """

        if ((not fsolv) and (t < self.I_on or t > self.I_off)):
            I = 0
        dvdt = x[0] - (x[0]**3/3) - x[1] + x[2] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        dzdt = self.e * (-x[0] + self.c - x[2])

        return [dvdt,dwdt,dzdt]

    # def plot_nullclines(self, I, ax, vmin=-1, vmax=1):
    #     return None

    def plot(self, y, ax=None, save=[False,None]):
        """
        Plot specifically for Rinzel model due to splitting z into subplot.

        Args:
            y (arr)   : Array containing y values in y[0], and the title of plot in y[1].
            save (arr): save[0] (boolean) True for save or False for not save, save[1] (str), filename.

        Returns:
            results (plot): ax
        """
        singleplt = False
        if ax is None:
            singleplt = True
            fig,ax = plt.subplots(2, sharex=True, figsize=(20, 10))
        plt.xlabel('Time (ms)')
        plt.suptitle(y[1])


        ax[0].plot(self.t,y[0][:,0:2]);
        ax[0].set_ylabel(self.label[0])
        ax[0].legend(self.legend[0:2])

        ax[1].plot(self.t,y[0][:,2]);
        ax[1].set_ylabel(self.label[1])
        ax[1].legend(self.legend[2])
        # plt.show()
        if save[0] == True:
            fig.savefig('Figures/'+save[1]+'.eps', format='eps')
            print('Figure saved as '+save[1])
        return ax
