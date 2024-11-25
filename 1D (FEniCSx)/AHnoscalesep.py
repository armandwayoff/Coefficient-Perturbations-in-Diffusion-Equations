# https://fenicsproject.discourse.group/t/matplotlib-instead-of-pyvista-in-dolfinx/9733
# conda activate fenicsx-env

import numpy as np
from mpi4py import MPI
import ufl
from ufl import dx, grad, inner
from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
from petsc4py.PETSc import ScalarType
from basix.ufl import element
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.integrate import quad


class diffusionProblem:
    def __init__(self, Nmesh, label, acoeff):
        self.P = 1
        self.label=label
        self.msh = mesh.create_interval(comm=MPI.COMM_WORLD, nx=Nmesh, points=(0.0, 1.0))
        self.lagrange_element = element("Lagrange", "interval", self.P)
        self.V = fem.functionspace(self.msh, self.lagrange_element)
        self.facets = mesh.locate_entities_boundary(self.msh, dim=0, marker=lambda x: np.isclose(x[0], 0.0) | np.isclose(x[0], 1.0))
        self.dofs = fem.locate_dofs_topological(V=self.V, entity_dim=0, entities=self.facets)
        self.bc = fem.dirichletbc(value=ScalarType(0), dofs=self.dofs, V=self.V)

        self.u = ufl.TrialFunction(self.V)
        self.v = ufl.TestFunction(self.V)
        self.x = ufl.SpatialCoordinate(self.msh)

        self.f = 1
        self.acoeff = acoeff(self.x[0])

        self.a = inner(self.acoeff * grad(self.u), grad(self.v)) * dx
        self.L = inner(self.f, self.v) * dx

        self.problem = LinearProblem(self.a, self.L, bcs=[self.bc], petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
        self.uh = self.problem.solve()

        self.xi = self.V.tabulate_dof_coordinates()
        self.xi_order = np.argsort(self.xi[:,0])

    def plot_show(self):
        plt.plot(self.xi[self.xi_order, 0], self.uh.x.array[self.xi_order], label=self.label)



def A(x):
    return 1/(2 - ufl.sin(2 * np.pi * ufl.tan(15 * np.pi * x / 32)))

def hmean(a, b):
    return (b - a)/quad(lambda x: 1/A(x), a, b)[0]

# mpl.use("pgf")

x = np.linspace(0, 1, 500)
y = np.array([A(xi) for xi in x])

H = 8
xH = np.linspace(0, 1, H+1)
yH = np.array([hmean(xH[i], xH[i+1]) for i in range(len(xH)-1)])

P2 = diffusionProblem(8, "FEM coarse", A)
P1 = diffusionProblem(1000, "FEM fine", A)

plt.plot(x, y)
for i in range(len(xH) - 1):
    plt.hlines(y=yH[i], xmin=xH[i], xmax=xH[i+1], linewidth=2, color='r')

plt.show()
# plt.savefig("1DAandHmean.pgf") # save as PGF file which can be used in your document via `\input`

P1.plot_show()
P2.plot_show()
plt.legend()
plt.show()

