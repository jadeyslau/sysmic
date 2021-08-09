import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Neuron():
    def __init__(self, I_ext=0):
        self.I_ext = I_ext

    def self_identifies(self):
        return "I'm a neuron!"

class FHN_Neuron(Neuron):

    # Fitzhugh-Nagumo equations:
    #           dv/dt = v - (v^3 / 3) - w + i
    #           dw/dt = (v + alpha - beta*w) / tau
    # v = membrane voltage
    # w = relaxation or recovery variable
    # I = input current
    # a, b, tau parameters of the model
    # 𝑎 = 0.7, 𝑏 = 0.8 and 𝜏 = 12.5.

    def __init__(self, I_ext=0, a=0.7, b=0.8, tau=12.5, x0=[0.7,-0.5]):
        Neuron.__init__(self, I_ext=I_ext)
        self.a     = a
        self.b     = b
        self.tau   = tau
        self.x0    = x0
        self.I_ext = I_ext

    def dx_dt(self, x, t, I):
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return [dvdt,dwdt]

    def solve(self, x0, I, t):
        y = odeint(self.dx_dt,x0,t,args=(I,))
        print(y.shape)
        return y

    def plot(self, I, t):
        y = self.solve(self.x0, I, t)

        # plot results
        plt.plot(t,y)
        plt.xlabel('time')
        plt.ylabel('y(t)')
        plt.title("Applied current: %s mA/cm2" % I)
        plt.show()
        return None

    def self_identifies(self):
        return "I'm a FitzHugh Nagamo neuron!"
# function that returns dy/dt
# def model(x, t):
#     I = 0.5
#     a=0.7
#     b=0.8
#     tau=12.5
#     dvdt = x[0] - (x[0]**3/3) - x[1] + I
#     dwdt = (x[0] + a - b*x[1]) / tau
#     return np.array(dvdt,dwdt)

# def dx_dt(x, t):
#     I   = 0
#     a   = 0.7
#     b   = 0.8
#     tau = 12.5
#
#     dvdt = x[0] - (x[0]**3/3) - x[1] + I
#     dwdt = (x[0] + a - b*x[1]) / tau
#     return [dvdt,dwdt]
#
# # initial condition
# x0 = [0.5,-0.7]
# I = 0
# # time points
# t = np.linspace(0, 200, num=1500)
#
# # solve ODE
# y = odeint(dx_dt,x0,t)
#
# # plot results
# plt.plot(t,y)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()
