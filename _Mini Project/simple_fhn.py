
# Fitzhugh-Nagumo equations:
#           dv/dt = v - (v^3 / 3) - w + i
#           dw/dt = (v + alpha - beta*w) / tau
# v = membrane voltage
# w = relaxation or recovery variable
# I = input current
# a, b, tau parameters of the model
# 𝑎 = 0.7, 𝑏 = 0.8 and 𝜏 = 12.5.
class FHN_Neuron(object):
    def __init__(self, a=0.7, b=0.8, tau=12.5, v_init=0.7, w_init-0.5):
        self.a = a
        self.b = b
        self.tau = tau

        self.v_init = v_init
        self.w_init = w_init

    def dx_dt(self, x, I):
        dvdt = x[0] - (x[0]**3/3) - x[1] + I
        dwdt = (x[0] + self.a - self.b*x[1]) / self.tau
        return np.array(dvdt,dwdt)
