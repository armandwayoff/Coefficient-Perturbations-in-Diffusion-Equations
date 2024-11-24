# https://fenicsproject.discourse.group/t/matplotlib-instead-of-pyvista-in-dolfinx/9733
# https://fenicsproject.discourse.group/t/dolfinx-fem-function-function-add-with-dolfinx-fem-function-function/9328
# conda activate fenicsx-env

import numpy as np
from mpi4py import MPI
import ufl
from ufl import dot, dx, grad, inner

from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
from dolfinx.fem import (
    Expression,
    Function,
    functionspace,
    assemble_scalar,
    dirichletbc,
    form,
    locate_dofs_topological,
)
from dolfinx.io import VTXWriter

from petsc4py.PETSc import ScalarType
from basix.ufl import element

import matplotlib.pyplot as plt
import matplotlib as mpl

from scipy.integrate import quad
from scipy.stats import hmean

# plt.rcParams['text.usetex'] = True

Nper = 128  # Nper / H \in 2\N
pattern_width = 1 / (Nper - 1)
# k = 10
# p = k / (Nper / 2)
p = 0.1
amin = 1    
amax = 5
h = 1000 # fine mesh
H = 8  # coarse mesh 
c = Nper // H

# np.random.seed(5)

# random_perturbations = np.random.choice(np.arange(1, Nper, 2), size=k, replace=False)
random_values = np.zeros(Nper, dtype=int)
random_values[1::2] = np.random.binomial(1, p, size=(Nper + 1) // 2)
k = np.sum(random_values)  # number of defects

random_perturbations = np.where(random_values == 1)[0]
print(k)

breakpoints = np.linspace(0, 1, Nper)

# values_per ##########################
values_per = np.full(Nper, amin)
values_per[1::2] = amax
#######################################

# values_pert #########################
values_pert = values_per.copy()
values_pert[random_perturbations] = amin
#######################################

# values_hat ##########################
hmean_coarsecell = 2 / (1 / amin + 1 / amax)
values_hat = np.empty(Nper)
rect = values_pert / values_per * pattern_width
for i in range(0, Nper, c):
    values_hat[i:i + c] = np.sum(rect[i:i + c]) / (c * pattern_width)
values_hat *= hmean_coarsecell
#######################################

# values_star #########################
hmean_coarsedomain = hmean_coarsecell
# adef = 1 / ((1 / 2 + k * 1 / Nper) * 1 / amin + (1 / 2 - k * 1 / Nper) * 1 / amax)
adef = 1 / ((1 / 2 + k * pattern_width) * 1 / amin + (1 / 2 - k * pattern_width) * 1 / amax)
a1 = hmean_coarsedomain - hmean_coarsedomain**2 / adef
values_star = np.full(Nper, hmean_coarsecell + p * a1)
#######################################

# values_bar ##########################
a0 = values_per.copy()
ai = [a0]
for j in range(k):
    aj = values_per.copy()
    aj[random_perturbations[j]] = amin
    ai.append(aj)

values_bar = np.empty(Nper)
for i in range(0, Nper, c):
    sum_T = 0
    for j in range(1, k + 1):
        sum_T += hmean(ai[j][i:i + c]) 
    sum_T += (1 - k) * hmean_coarsecell
    values_bar[i:i + c] = sum_T   
#######################################

class diffusionProblem:
    def __init__(self, Nmesh, label, coeff):
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
        if coeff == 'A_no_scale_sep':
            self.acoeff = A_no_scale_sep(self.x[0])
        elif coeff == 'A_periodic':
            self.acoeff = A_periodic(self.V)
        elif coeff == 'A_perturbed':
            self.acoeff = A_perturbed(self.V)
        elif coeff == 'A_hat':
            self.acoeff = A_hat(self.V)
        elif coeff == 'A_star':
            self.acoeff = A_star(self.V)
        elif coeff == 'A_bar':
            self.acoeff = A_bar(self.V)
        elif coeff == 'piecewise_hmean':
            self.acoeff = piecewise_hmean(A_no_scale_sep, self.msh)

        self.a = inner(self.acoeff * grad(self.u), grad(self.v)) * dx
        self.L = inner(self.f, self.v) * dx

        self.problem = LinearProblem(self.a, self.L, bcs=[self.bc], petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
        self.uh = self.problem.solve()

        self.xi = self.V.tabulate_dof_coordinates()
        self.xi_order = np.argsort(self.xi[:,0])

    def plot_solution(self, ax=plt):
        ax.plot(self.xi[self.xi_order, 0], self.uh.x.array[self.xi_order], label=self.label, linewidth=1)

    def plot_coeff(self):
        plt.plot(self.xi[self.xi_order, 0], self.acoeff.x.array[self.xi_order], label="Coeff " + self.label)

def A_no_scale_sep(x):
    return 1/(2 - ufl.sin(2 * np.pi * ufl.tan(15 * np.pi * x / 32)))

def h_mean(func, a, b):
    return (b - a)/quad(lambda x: 1/func(x), a, b)[0]

def piecewise_hmean(A, msh):
    xH = np.linspace(0, 1, H + 1)
    yH = np.array([h_mean(A, xH[i], xH[i + 1]) for i in range(len(xH) - 1)])

    dg_element = element("DG", "interval", 0)
    Vdg = fem.functionspace(msh, dg_element)
    
    return interpolate_pwc(Vdg, xH, yH)

def interpolate_pwc(V, brkpnts, values):
    g = fem.Function(V)

    def piecewise_constant(x):
        indices = np.digitize(x[0], brkpnts) - 1  
        return values[indices]

    g.interpolate(piecewise_constant)
    return g

def A_periodic(V):
    return interpolate_pwc(V, breakpoints, values_per)

def A_perturbed(V):
    return interpolate_pwc(V, breakpoints, values_pert)
    
def A_hat(V):
    return interpolate_pwc(V, breakpoints, values_hat)

def A_star(V):
    return interpolate_pwc(V, breakpoints, values_star)

def A_bar(V):
    return interpolate_pwc(V, breakpoints, values_bar)

# https://jsdokken.com/dolfinx-tutorial/chapter4/convergence.html
# https://fenicsproject.discourse.group/t/unexpectedly-high-l2-error-when-comparing-coarse-and-fine-resolution-approximation/12673
# https://github.com/FEniCS/dolfinx/commit/ab79530e1ae60a646002609b510e8392cc09e213#diff-b0cafb782dd5cfad884c470627b18987ecb3fc113a5bb414f98e360992253a91R913
padding = 1e-14
def error(type, uh, u_ex="zero", degree_raise=3):
    # Create higher order function space
    degree = uh.function_space.ufl_element().degree
    # family = uh.function_space.ufl_element().family
    # family = uh.function_space.ufl_element().cell().family()
    family = uh.function_space.element.basix_element.family

    mesh = uh.function_space.mesh
    if u_ex == "zero":
        if type == 'L2':
            error = form(inner(uh, uh) * dx)
        elif type == 'H10':
            error = form(dot(grad(uh), grad(uh)) * dx)
        error_local = assemble_scalar(error)
        error_global = mesh.comm.allreduce(error_local, op=MPI.SUM)
        return np.sqrt(error_global)
    else:
        W = functionspace(mesh, (family, degree + degree_raise))
        # Interpolate approximate solution
        u_W = Function(W)
        u_W.interpolate(uh)

        # Interpolate exact solution, special handling if exact solution
        # is a ufl expression or a python lambda function
        u_ex_W = Function(W)

        if isinstance(u_ex, Function):
            if u_ex.function_space.mesh != mesh:
                from dolfinx.fem import create_interpolation_data

                fine_mesh_cell_map = mesh.topology.index_map(mesh.topology.dim)
                num_cells_on_proc = fine_mesh_cell_map.size_local + fine_mesh_cell_map.num_ghosts
                cells = np.arange(num_cells_on_proc, dtype=np.int32)
                interpolation_data = create_interpolation_data(W, u_ex.function_space, cells, padding)
                u_ex_W.interpolate_nonmatching(u_ex, cells, interpolation_data=interpolation_data)
            else:
                u_ex_W.interpolate(u_ex)
        elif isinstance(u_ex, ufl.core.expr.Expr):
            u_expr = Expression(u_ex, W.element.interpolation_points())
            u_ex_W.interpolate(u_expr)
        else:
            u_ex_W.interpolate(u_ex)

        u_ex_W.name = "u_ex_W"
        u_W.name = "u_W"
        with VTXWriter(mesh.comm, f"test_u_{family}_{degree}.bp", [u_ex_W, u_W], engine="BP4") as vtx:
            vtx.write(0.0)

        # Compute the error in the higher order function space
        e_W = Function(W)
        e_W.x.array[:] = u_W.x.array - u_ex_W.x.array

        # Integrate the error
        if type == 'L2':
            error = form(inner(e_W, e_W) * dx)
        elif type == 'H10':
            error = form(dot(grad(e_W), grad(e_W)) * dx)
        error_local = assemble_scalar(error)
        error_global = mesh.comm.allreduce(error_local, op=MPI.SUM)
        return np.sqrt(error_global)

"""
P1 = diffusionProblem(h, "FEM fine", 'A_no_scale_sep')
P2 = diffusionProblem(H, "FEM coarse", 'A_no_scale_sep')
P3 = diffusionProblem(H, "FEM coarse with $\overline{A}_H$", 'piecewise_hmean')
"""

P4 = diffusionProblem(h, "$a_\\varepsilon(\,\cdot,\omega)$ fine", 'A_perturbed')
P5 = diffusionProblem(H, "$a_\\varepsilon(\,\cdot,\omega)$ coarse", 'A_perturbed')
P6 = diffusionProblem(H, "$\widehat{a}(\omega) = \\frac{\overline{a}_\mathrm{per}}{|T|} \int_T \\frac{a(x,\omega)}{a_\mathrm{per}(x)} \, \mathrm{d}x$", 'A_hat')
P7 = diffusionProblem(H, "$a^\\ast(\omega) = \overline{a}_\mathrm{per} + p a_1$", 'A_star')
P8 = diffusionProblem(H, "$\overline{a}(\omega) = \sum_{i=0}^N \mu_i \overline{a}_i$", 'A_bar')

print("fine", error('L2', P4.uh))
print("coarse", error('L2', P4.uh, P5.uh))
print("A_hat",  error('L2', P4.uh, P6.uh))
print("A_star", error('L2', P4.uh, P7.uh))
print("A_bar",  error('L2', P4.uh, P8.uh))

"""
P1.plot_solution()
P2.plot_solution()
P3.plot_solution()
plt.legend()
plt.show()
"""

# mpl.use("pgf")

plt.figure(figsize=(6,1.5))
P4.plot_coeff()
plt.xticks([0, 1], ['$0$', '$1$'])
plt.yticks([amin, amax], ['$a_\mathrm{min}$', '$a_\mathrm{max}$'])
plt.tight_layout()
plt.show()

# plt.savefig("1Dperturbedcoeff.pgf") 

plt.figure(figsize=(7,2.5))
plt.subplot(1, 2, 1)
P4.plot_solution()
P5.plot_solution()
P6.plot_solution()
P7.plot_solution()
P8.plot_solution()
plt.xticks([0, 1], ['$0$', '$1$'])
plt.yticks([0, 0.08], ['$0$', '$0.08$'])

axzoom = plt.subplot(1, 2, 2)
P4.plot_solution(axzoom)
P5.plot_solution(axzoom)
P6.plot_solution(axzoom)
P7.plot_solution(axzoom)
P8.plot_solution(axzoom)
x1,x2,y1,y2 = 0.3,0.7, 0.06,0.084
axzoom.set_xlim([x1, x2])
axzoom.set_ylim([y1, y2])
axzoom.set_xticks([x1, x2], ['$0.3$', '$0.7$'])
axzoom.set_yticks([])

plt.legend(# bbox_to_anchor=(1, 0.5), loc="center left", 
    ncol = 5,
    bbox_to_anchor=(0, 1, 1, 0), loc="lower center")
plt.tight_layout()
plt.show()

# plt.savefig("1Dperturbedsolutions.pgf") 
# plt.savefig("methodscomparison.pgf") 
