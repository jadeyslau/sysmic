import matplotlib.pyplot as plt
import numpy as np

class Neuron(object):
    """Base neuron class with main components i.e. resistors, capacitors, and battery. Emulates current flow in a neuron."""

    def __init__(self, g_K=36.0, g_Na=120.0, gLeak=0.3, V_K=-12.0, V_Na=115.0, V_leak=10.613, tmin=0, tmax=50):
        # time constant

        # Capacitance: Membrane capacitance per unit area (uF/cm^2) I = C * (dV/dt)
        self.Cm = 1.0

        # Resistance: The state of ion channels. The more open the lower the resistance, the higher the conductance (amount of current flowing through these resistors Ohm's Law: I = V/R)
        # Average ion channel conductance per unit area (mS/cm^2)
        self.g_K = g_K
        self.g_Na = g_Na
        self.gLeak = g_leak

        # Battery: Concentration gradient of neuron is the external to internal ratio of ion concentration.
        # self.I_ext = I_ext
        # self.Q = C*R
        #
        # self.ts = np.linspace(0, 200, 300)
        # self.tau = R*C

        # Membrane potentials (mV)
        self.V_K = V_K
        self.V_Na = V_Na
        self.V_leak = V_leak

        # Time
        self.T = np.linspace(self.tmin, self.tmax, 10000)


    def voltage(self, I, R):


    def plot(self, y):
        print('plot')
        fig, ax = plt.subplots(1,1)

        ax.plot(self.ts, y)
        ax.set_xlabel("Time")

        fig.tight_layout()
        return fig

    def self_identifies(self):
        return "I'm a neuron!"


# class HHNeuron(Neuron):

# class FNNeuron(Neuron):
#     """FitzHugh-Naguno neuron.
#     The units in this model are different from the HH ones.
#     Sources:
#     https://github.com/ruhugu/brainythings/blob/master/brainythings/neurons.py
#     https://en.wikipedia.org/w/index.php?title=FitzHugh%E2%80%93Nagumo_model&oldid=828788626
#     http://www.scholarpedia.org/article/FitzHugh-Nagumo_model
#     """
#     def __init__():
