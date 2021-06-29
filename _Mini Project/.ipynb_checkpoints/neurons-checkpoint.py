


class Neuron(object):
    """Base neuron class with main components i.e. resistors, capacitors, and battery. Emulates current flow in a neuron."""

    def __init__(self, C=1, R=10, V=3):
        # time constant

        # Capacitance: Membrane capacity (units?) I = C * (dV/dt)
        self.C = C

        # Resistance: The state of ion channels. The more open the lower the resistance, the higher the conductance (amount of current flowing through these resistors Ohm's Law: I = V/R)
        self.R = R

        # Battery: Concentration gradient of neuron is the external to internal ratio of ion concentration.
        self.I_ext = I_ext

    def plot(self, y):
        print('plot')
        return fig


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
