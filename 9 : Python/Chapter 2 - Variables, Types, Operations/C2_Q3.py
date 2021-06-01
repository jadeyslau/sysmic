# We have an enzyme whose reaction velocity is v = 50 mol ⋅ L−1 ⋅ s−1 at the substrate concentration of [S] = Km = 2.5 mol ⋅ L−1 . Work out the maximum reaction velocity or Vmax for this enzyme using the Michaelis-Menten equation:

def calc_vmax(v, s, km):
    vmax = (v * (s+km)) / s
    print(vmax)

calc_vmax(50, 2.5, 2.5)
