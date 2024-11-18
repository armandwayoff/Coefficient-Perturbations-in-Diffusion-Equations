# conda activate fenicsx-env

import numpy as np
import ufl
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.integrate import quad

def A(x):
    return 1/(2 - ufl.sin(2 * np.pi * ufl.tan(15 * np.pi * x / 32)))

def hmean(a, b):
    return (b - a)/quad(lambda x: 1/A(x), a, b)[0]

x = np.linspace(0, 1, 500)
y = np.array([A(xi) for xi in x])

H = 8
xH = np.linspace(0, 1, H+1)
yH = np.array([hmean(xH[i], xH[i+1]) for i in range(len(xH)-1)])

plt.plot(x, y)
for i in range(len(xH) - 1):
    plt.hlines(y=yH[i], xmin=xH[i], xmax=xH[i+1], linewidth=2, color='r')

# mpl.use("pgf")

plt.show()

# plt.savefig("1dFEniCS.pgf") 

