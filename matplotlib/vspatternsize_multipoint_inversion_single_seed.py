import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# mpl.use("pgf")

# Data

x = np.array([25, 31, 37, 41, 53, 63, 73, 81])

x1def = np.array([1, 2, 3, 4, 6, 9, 12, 16]) # 1%
x2def = np.array([2, 4, 6, 8, 13, 19, 25, 32]) # 2%
x25def = np.array([3, 5, 8, 10, 16, 24, 32, 40]) # 2.5%
x3def = np.array([4, 6, 9, 12, 20, 28, 38, 48]) # 3%
x4def = np.array([5, 9, 12, 16, 27, 38, 51, 64]) # 4%
x5def = np.array([7, 11, 16, 20, 33, 48, 64, 80]) # 5%

# 2222
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 1%, p = 0.98
y1_2222 = np.array([0, 5.40231e-05, 0.00020389, 0.000182511, 0.000381055, 0.000709154, 0.000778738, 0.000794373])
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2%, p = 0.98
y2_2222 = np.array([0.000104406, 0.00076025, 0.00551497, 0.00322045, 0.00802483, 0.0230656, 0.00311169, 0.00180014])
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2.5%, p = 0.98
y25_2222 = np.array([0.000242539, 0.00110612, 0.00566664, 0.00366489, 0.00760141, 0.0227228, 0.00467583, 0.00275895])
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 3%, p = 0.98
y3_2222 = np.array([0.000935573, 0.00110341, 0.00570999, 0.00335233, 0.00502097, 0.00450876, 0.00522459, 0.00675815])
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 4%, p = 0.98
y4_2222 = np.array([0.000767656, 0.00325436, 0.0059586, 0.00424335, 0.0283283, 0.00687502, 0.0207619, 0.0102965])
# Seed=2222, global RHS, amax=10, sponge, FEM size 100, percentofdef = 5%, p = 0.98
y5_2222 = np.array([0.00565887, 0.00424505, 0.00652361, 0.00545879, 0.0292998, 0.0113122, 0.0214344, 0.0129582])

# 4321
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 1%, p = 0.98
y1_4321 = np.array([0, 0.000197424, 0.00034451, 0.00108874, 0.000645786, 0.000661601, 0.000567573, 0.00193133])
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2%, p = 0.98
y2_4321 = np.array([0.000173894, 0.000568832, 0.000749883, 0.00549182, 0.00609544, 0.00148516, 0.00509259, 0.00440387])
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2.5%, p = 0.98
y25_4321 = np.array([0.000418698, 0.00072409, 0.0017814, 0.00593286, 0.00861927, 0.00626971, 0.00512274, 0.00555823])
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 3%, p = 0.98
y3_4321 = np.array([0.00240285, 0.00236717, 0.00275401, 0.00591872, 0.00835329, 0.0221299, 0.00750302, 0.00763072])
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 4%, p = 0.98
y4_4321 = np.array([0.00286882, 0.00263374, 0.00317286, 0.00684704, 0.00998996, 0.0231585, 0.0102082, 0.0110429])
# Seed=4321, global RHS, amax=10, sponge, FEM size 100, percentofdef = 5%, p = 0.98
y5_4321 = np.array([0.00282962, 0.00350932, 0.00347885, 0.00716067, 0.013409, 0.0249985, 0.015049, 0.0196517])

# 1234
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 1%, p = 0.98
y1_1234 = np.array([0, 0.000529971, 0.00122154, 0.000871148, 0.00104897, 0.00144171, 0.00286357, 0.00376097])
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2%, p = 0.98
y2_1234 = np.array([0.00142049, 0.0012353, 0.00502154, 0.00243955, 0.0037801, 0.00249704, 0.003181, 0.00632484])
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 2.5%, p = 0.98
y25_1234 = np.array([0.00177032, 0.00111927, 0.00843521, 0.00579971, 0.00622876, 0.00320117, 0.00357597, 0.00582915])
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 3%, p = 0.98
y3_1234 = np.array([0.00190054, 0.00136738, 0.00827685, 0.00568496, 0.00653741, 0.00338007, 0.00402151, 0.00685602])
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 4%, p = 0.98
y4_1234 = np.array([0.00304345, 0.00828281, 0.00861724, 0.00664104, 0.0127867, 0.00666733, 0.00801402, 0.0111394])
# Seed=1234, global RHS, amax=10, sponge, FEM size 100, percentofdef = 5%, p = 0.98
y5_1234 = np.array([0.00725104, 0.0118071, 0.0115022, 0.00917554, 0.0111593, 0.00882932, 0.0102563, 0.0149661])


# Plot settings

f = plt.figure()
# f.set_figwidth(5)
f.set_figheight(4)  

# _, ax = plt.subplots()

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 1, 5

markersize1, markersize2, markersize3 = 30, 20, 7 # 5
# Plot

"""
plt1_2222 ,= plt.semilogy(x[start2:], y1_2222[start2:], linewidth=linew, color=[cvalr, 0.0, 0.0], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')
plt2_2222 ,= plt.semilogy(x[start1:], y2_2222[start1:], linewidth=linew, color=[0.0, 0.0, cvalb], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')
plt25_2222 ,= plt.semilogy(x[start1:], y25_2222[start1:], linewidth=linew, color=[cvalr, 0.0, cvalb], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')
plt3_2222 ,= plt.semilogy(x[start1:], y3_2222[start1:], linewidth=linew, color=[0.0, cvalg, 0.0], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')
plt4_2222 ,= plt.semilogy(x[start1:], y4_2222[start1:], linewidth=linew, color=[0.0, cvalg, cvalb], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')
plt5_2222 ,= plt.semilogy(x[start1:], y5_2222[start1:], linewidth=linew, color=[cvalr, cvalg, 0.0], marker='.', linestyle='solid', markersize=markersize1, markerfacecolor='none')

plt1_4321 ,= plt.semilogy(x[start2:], y1_4321[start2:], linewidth=linew, color=[cvalr, 0.0, 0.0], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
plt2_4321 ,= plt.semilogy(x[start1:], y2_4321[start1:], linewidth=linew, color=[0.0, 0.0, cvalb], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
plt25_4321 ,= plt.semilogy(x[start1:], y25_4321[start1:], linewidth=linew, color=[cvalr, 0.0, cvalb], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
plt3_4321 ,= plt.semilogy(x[start1:], y3_4321[start1:], linewidth=linew, color=[0.0, cvalg, 0.0], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
plt4_4321 ,= plt.semilogy(x[start1:], y4_4321[start1:], linewidth=linew, color=[0.0, cvalg, cvalb], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
plt5_4321 ,= plt.semilogy(x[start1:], y5_4321[start1:], linewidth=linew, color=[cvalr, cvalg, 0.0], marker='.', linestyle='solid', markersize=markersize2, markerfacecolor='none')
"""

"""
plt1_2222 ,= plt.semilogy(x[start2:], y1_2222[start2:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0], markersize=markersize3)
plt2_2222 ,= plt.semilogy(x[start1:], y2_2222[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb], markersize=markersize3)
plt25_2222 ,= plt.semilogy(x[start1:], y25_2222[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb], markersize=markersize3)
plt3_2222 ,= plt.semilogy(x[start1:], y3_2222[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0], markersize=markersize3)
plt4_2222 ,= plt.semilogy(x[start1:], y4_2222[start1:], '-s', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb], markersize=markersize3)
plt5_2222 ,= plt.semilogy(x[start1:], y5_2222[start1:], '-s', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0], markersize=markersize3)

plt1_4321 ,= plt.semilogy(x[start2:], y1_4321[start2:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0], markersize=markersize3)
plt2_4321 ,= plt.semilogy(x[start1:], y2_4321[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb], markersize=markersize3)
plt25_4321 ,= plt.semilogy(x[start1:], y25_4321[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb], markersize=markersize3)
plt3_4321 ,= plt.semilogy(x[start1:], y3_4321[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0], markersize=markersize3)
plt4_4321 ,= plt.semilogy(x[start1:], y4_4321[start1:], '-o', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb], markersize=markersize3)
plt5_4321 ,= plt.semilogy(x[start1:], y5_4321[start1:], '-o', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0], markersize=markersize3)
"""

plt1_1234 ,= plt.semilogy(x[start2:], y1_1234[start2:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0], markersize=markersize3)
plt2_1234 ,= plt.semilogy(x[start1:], y2_1234[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb], markersize=markersize3)
plt25_1234 ,= plt.semilogy(x[start1:], y25_1234[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb], markersize=markersize3)
plt3_1234 ,= plt.semilogy(x[start1:], y3_1234[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0], markersize=markersize3)
plt4_1234 ,= plt.semilogy(x[start1:], y4_1234[start1:], '-o', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb], markersize=markersize3)
plt5_1234 ,= plt.semilogy(x[start1:], y5_1234[start1:], '-o', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0], markersize=markersize3)


extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

# 1234
# legend_handle = [extra, extra, extra, plt1, extra, plt2, extra, plt3, extra, plt4, extra, plt5, extra, plt6]
# 4321
legend_handle = [extra, extra, # extra, extra, 
                 extra, plt1_1234, 
                 extra, plt2_1234,
                 extra, plt25_1234, 
                 extra, plt3_1234,
                 extra, plt4_1234, 
                 extra, plt5_1234
                 ]

label_col_1 = [r"Seed \textbackslash\ Proportion of perturbations", r"4321"] #, r"4321", r"1234"]
label_j_1 = [r"$1\,\%$"]
label_j_2 = [r"$2\,\%$"]
label_j_25 = [r"$2.5\,\%$"]
label_j_3 = [r"$3\,\%$"]
label_j_4 = [r"$4\,\%$"]
label_j_5 = [r"$5\,\%$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'Pattern size')
plt.ylabel(r'Relative error $\|\nabla(\overline{u}_h - \widetilde{u}_h)\|_{L^2(\Omega)} / \|\nabla \overline{u}_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)

# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
# 1234
# legend_labels = numpy.concatenate([label_col_1, label_j_2, label_empty * 1, label_j_3, label_empty * 1, label_j_1, label_empty * 1, label_j_4, label_empty * 1, label_j_5, label_empty * 1, label_j_6, label_empty * 1])
# 4321
legend_labels = numpy.concatenate([label_col_1, 
                                   label_j_1, label_empty * 1, 
                                   label_j_2, label_empty * 1, 
                                   label_j_25, label_empty * 1, 
                                   label_j_3, label_empty * 1, 
                                   label_j_4, label_empty * 1, 
                                   label_j_5, label_empty * 1])


#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 7, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# Ticks
ticks = x
# ax.set_xticklabels(xdef)
plt.xticks(ticks, rotation=0)

# Show or save plot
plt.tight_layout()
plt.show()

plt.savefig("vspatternsize_multipoint_inversion_4321.pgf") # save as PGF file which can be used in your document via `\input`
