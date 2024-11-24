import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

mpl.use("pgf")

# Data
x = np.array([10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250])
y = np.array([0.00022784, 0.000472128, 0.000250893, 0.000379315, 0.000324754, 0.000255675, 0.000317715, 0.000287517, 0.000310661, 0.000294495, 0.000267172, 0.000296384, 0.000285198])
ybis = np.array([0.0230146, 0.281377, 0.231378, 0.227339, 0.26503, 0.284774, 0.27355, 0.29213, 0.302388, 0.29986, 0.304648, 0.305247, 0.310365])
y2 = np.array([0.00558151, 0.00503027, 0.0044505, 0.00393357, 0.00415212, 0.00396442, 0.00409113, 0.00404088, 0.00407525, 0.00404995, 0.00391827, 0.00400231, 0.00393495])
y2bis = np.array([0.27122, 0.434772, 0.433128, 0.477986, 0.501848, 0.475854, 0.494389, 0.503589, 0.492427, 0.49749, 0.504056, 0.495293, 0.503821])
y3 = np.array([0, 2.34867e-05, 3.37216e-05, 7.26793e-05, 8.53506e-05, 8.25075e-05, 0.000101249, 0.000101065, 0.000111878, 0.000106069, 9.84612e-05, 0.000106946, 0.000105389])
y3bis = np.array([0, 0.00531666, 0.0157585, 0.0196188, 0.0303994, 0.0336577, 0.0298715, 0.0408917, 0.0395577, 0.0380809, 0.0447343, 0.0416592, 0.04242])

cb9non = np.array([0.00249549, 0.00271956, 0.00297835, 0.00308233, 0.00368105, 0.00360019, 0.00355019, 0.00344447, 0.00340327, 0.00345949, 0.00341169, 0.00338502, 0.00332512])
cb9 = np.array([0.415329, 0.750469, 0.87785, 1.00979, 1.0737, 1.1639, 1.2292, 1.25697, 1.23877, 1.28927, 1.31512, 1.34124, 1.36653])
cb27non = np.array([7.04205e-05, 0.000277071, 0.00034998, 0.000287651, 0.000302144, 0.00042841, 0.000348128, 0.000330848, 0.000399858, 0.0003663, 0.000342329, 0.000392149, 0.000371183])
cb27 = np.array([0.0120566, 0.139115, 0.201116, 0.220587, 0.249547, 0.277107, 0.277892, 0.292211, 0.326669, 0.32111, 0.334481, 0.348388, 0.357193])
cb81non = np.array([0, 7.82584e-06, 8.66934e-06, 1.20337e-05, 3.0787e-05, 2.49516e-05, 3.23982e-05, 3.89175e-05, 4.367e-05, 3.64198e-05, 3.1963e-05, 3.08995e-05, 3.75521e-05])
cb81 = np.array([0, 0.00403049, 0.00686261, 0.0129805, 0.0463577, 0.0426124, 0.0632339, 0.0670862, 0.0732636, 0.0785074, 0.0735189, 0.0751279, 0.086052])

# Plot settings

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 2, 3, 5

# Plot
plt1 ,= plt.semilogy(x[start1:], y2bis[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(x[start2:], ybis[start2:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(x[start3:], y3bis[start3:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(x[start1:], cb9[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt5 ,= plt.semilogy(x[start2:], cb27[start2:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt6 ,= plt.semilogy(x[start3:], cb81[start3:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, extra, plt1, plt4, extra, plt2, plt5, extra, plt3, plt6]

label_col_1 = [r"Pattern \textbackslash\ Size", r"Sponge", r"Checkerboard"]
label_j_1 = [r"$s = 9$"]
label_j_2 = [r"$s = 27$"]
label_j_3 = [r"$s = 81$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'\textsc{fem} mesh size')
plt.ylabel(r'Relative error $\|\nabla(u_h - \overline{u}_h)\|_{L^2(\Omega)} / \|\nabla u_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)

# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
legend_labels = numpy.concatenate([label_col_1, label_j_1, label_empty * 2, label_j_2, label_empty * 2, label_j_3, label_empty * 2])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 4, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# Ticks
plt.xticks(x[start1:])

# Show or save plot
plt.tight_layout()
plt.show()

# plt.savefig("relative_energy_errors_vs_femsize.pgf") # save as PGF file which can be used in your document via `\input`
