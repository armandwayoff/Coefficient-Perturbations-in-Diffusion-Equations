# https://fenicsproject.discourse.group/t/matplotlib-instead-of-pyvista-in-dolfinx/9733
# https://fenicsproject.discourse.group/t/dolfinx-fem-function-function-add-with-dolfinx-fem-function-function/9328
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
from scipy.stats import hmean

Nper = 300  # Nper / H \in 2\N
pattern_width = 1 / (Nper - 1)
k = 5
p = k / (Nper / 2)

amp = 1.5
omega = Nper

amp_pert, mean, sigma = 1*amp, 0.5, 1/omega

h = 1000 # fine mesh
H = 8  # coarse mesh 
c = Nper // H

means = np.random.choice(np.linspace(0, 1, h), size=k, replace=False)

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

        if acoeff == 'A':
            self.acoeff = A
            self.acoeff_solve = A(self.x[0], ufl)
        elif acoeff == 'A_perturbed':
            self.acoeff = A_perturbed
            self.acoeff_solve = A_perturbed(self.x[0], ufl)
        elif acoeff == 'A_star':
            self.acoeff =  A_star(self.msh, np)
            self.acoeff_solve = A_star(self.msh, ufl)
        elif acoeff == 'A_hat':
            self.acoeff =  A_hat(self.msh, np)
            self.acoeff_solve = A_hat(self.msh, ufl)
        elif acoeff == 'A_bar':
            self.acoeff =  A_bar(self.msh, np)
            self.acoeff_solve = A_bar(self.msh, ufl)
        elif acoeff == 'piecewise_hmean':
            self.acoeff = piecewise_hmean
            self.acoeff_solve = piecewise_hmean(A_perturbed, ufl, self.msh)

        self.a = inner(self.acoeff_solve * grad(self.u), grad(self.v)) * dx
        self.L = inner(self.f, self.v) * dx

        self.problem = LinearProblem(self.a, self.L, bcs=[self.bc], petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
        self.uh = self.problem.solve()

        self.xi = self.V.tabulate_dof_coordinates()
        self.xi_order = np.argsort(self.xi[:,0])

    def plot_coeff(self):
        length = len(self.xi[self.xi_order, 0])
        if np.array_equal(self.acoeff, piecewise_hmean):
            x = np.linspace(0, 1, length - 1)
            plt.plot(x, self.acoeff(A, np, self.msh), label=self.label)
        else:
            x = np.linspace(0, 1, length)
            plt.plot(x, self.acoeff(x, np), label=self.label)

    def plot_solution(self):
        plt.plot(self.xi[self.xi_order, 0], self.uh.x.array[self.xi_order], label=self.label)

def A(x, pack):
    return amp * pack.sin(omega * x) + 2 * amp
    # return 1/(2 - pack.sin(2 * np.pi * pack.tan(15 * np.pi * x / 32)))

def perturbation(amp, mean, sigma, x, pack):
    return amp * pack.exp(-(x - mean)**2 / (2 * sigma**2))

def perturbations(amp, means, sigma, x, pack):
    if pack == np:
        total_perturbation = np.zeros_like(x)
    else:
        total_perturbation = 0
    for mean in means:
        total_perturbation += perturbation(amp, mean, sigma, x, pack)
    return total_perturbation

def A_perturbed(x, pack):
    return A(x, pack) + perturbations(amp_pert, means, sigma, x, pack)

def h_mean(func, a, b, pack):
    return (b - a)/quad(lambda x: 1/func(x, pack), a, b)[0]

def mean_ratio(func1, func2, a, b, pack):
    return quad(lambda x: func1(x, pack) / func2(x, pack), a, b)[0] / (b - a)

def piecewise_hmean(A, pack, msh):
    num_intervals = msh.topology.index_map(msh.topology.dim).size_local
    xH = np.linspace(0, 1, num_intervals + 1)
    yH = np.array([h_mean(A, xH[i], xH[i + 1], pack) for i in range(len(xH) - 1)])

    if pack == np:
        return yH
    elif pack == ufl:        
        dg_element = element("DG", "interval", 0)
        Vdg = fem.functionspace(msh, dg_element)
        
        return interpolate_pwc(Vdg, xH, yH)

def piecewise_mean_ratio(A1, A2, pack, msh):
    num_intervals = msh.topology.index_map(msh.topology.dim).size_local
    xH = np.linspace(0, 1, num_intervals + 1)
    yH = np.array([mean_ratio(A1, A2, xH[i], xH[i + 1], pack) for i in range(len(xH) - 1)])

    if pack == np:
        return yH
    elif pack == ufl:        
        dg_element = element("DG", "interval", 0)
        Vdg = fem.functionspace(msh, dg_element)
        
        return interpolate_pwc(Vdg, xH, yH)
    
def A_star(msh, pack):
    aper = piecewise_hmean(A, pack, msh)
    adef = h_mean(A_perturbed, 0, 1, pack)
    a1 = aper - aper * aper / adef
    return aper + p * a1

def A_hat(msh, pack):
    aper = piecewise_hmean(A, pack, msh)
    b = piecewise_mean_ratio(A_perturbed, A, pack, msh)
    return aper * b

def A_bar(msh, pack):
    return "?"

def interpolate_pwc(V, brkpnts, values):
    g = fem.Function(V)

    def piecewise_constant(x):
        indices = np.digitize(x[0], brkpnts) - 1  
        return values[indices]

    g.interpolate(piecewise_constant)
    return g

P1 = diffusionProblem(h, "Perturbed coefficient", 'A_perturbed')
P2 = diffusionProblem(H, "FEM coarse", 'A_perturbed')
P3 = diffusionProblem(H, "FEM coarse with $\overline{A}_H$", 'piecewise_hmean')
P4 = diffusionProblem(H, "A_star", 'A_star')
P5 = diffusionProblem(H, "A_hat", 'A_hat')


P1.plot_coeff()
# P2.plot_coeff()
# P3.plot_coeff()
# P4.plot_coeff()
x = np.linspace(0, 1, h)
pert = np.array(perturbations(amp_pert, means, sigma, x, np))
plt.plot(x, pert, label='Pertubations')
plt.legend()
plt.show()

P1.plot_solution()
P2.plot_solution()
P3.plot_solution()
P4.plot_solution()
P5.plot_solution()
plt.legend()
plt.show()