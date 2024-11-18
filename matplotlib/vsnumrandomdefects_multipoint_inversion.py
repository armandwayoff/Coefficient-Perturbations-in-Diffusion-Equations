import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

mpl.use("pgf")

# Data

x1 = [3, 4, 6, 8, 10, 11, 12, 15]
x2 = [6, 7, 7, 8, 8, 10, 11, 13]
x3 = [5, 5, 5, 6, 7, 7, 9, 12]
x4 = [4, 6, 7, 7, 7, 12, 16, 17]
x5 = [2, 4, 7, 8, 14, 18, 21, 23]
x6 = [3, 4, 6, 8, 9, 9, 11, 12]

# Seed=1235, global RHS, amax=10, size 27 sponge, FEM size 100
y1 = np.array([0.00140391,  0.00149261, 0.00850191, 0.0217079, 0.00918157, 0.00964265, 0.00996124, 0.0125178])
# Seed=1236, global RHS, amax=10, size 27 sponge, FEM size 100
y2 = np.array([0.00724021, 0.00727869, 0.00727869, 0.00839758, 0.00839758, 0.00893436, 0.00860586, 0.0112658])
# Seed=1237, global RHS, amax=10, size 27 sponge, FEM size 100
y3 = np.array([0.00606552, 0.00606552, 0.00606552, 0.00610451, 0.00635399, 0.00635399, 0.00930583, 0.010919])
# Seed=1238, global RHS, amax=10, size 27 sponge, FEM size 100
y4 = np.array([0.00225424, 0.00328086, 0.00440725, 0.00440725, 0.00440725, 0.00922446, 0.0114842, 0.0109696])
# Seed=1239, global RHS, amax=10, size 27 sponge, FEM size 100
y5 = np.array([0.00199619, 0.00818061, 0.00783069, 0.00775506, 0.0149207, 0.0166007, 0.0177689, 0.020336])
# Seed=1240, global RHS, amax=10, size 27 sponge, FEM size 100
y6 = np.array([0.000499655, 0.00248776, 0.00857469, 0.0127429, 0.0130132, 0.0130132, 0.0215516, 0.0186289])


pattern_size = 27
num_pot_def = ((pattern_size - 1) / 2) ** 2

# Plot settings

f = plt.figure()
# f.set_figwidth(5)
f.set_figheight(4)  

_, ax = plt.subplots()

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 3, 5

# Plot

plt1 ,= plt.semilogy(x1[start1:], y1[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(x2[start1:], y2[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(x3[start1:], y3[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(x4[start1:], y4[start1:], '-o', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb])
plt5 ,= plt.semilogy(x5[start1:], y5[start1:], '-o', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0])
plt6 ,= plt.semilogy(x6[start1:], y6[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb])


# plt7 ,= plt.semilogy(x[start1:], y7[start1:], '-s', linewidth=linew, color=[cvalr, cvalg, cvalb], markerfacecolor=[mfcvalr, mfcvalg, mfcvalb])


extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, plt6, extra, plt4, extra, plt1, extra, plt3, extra, plt2, extra, plt5]

label_col_1 = [r"Pattern \textbackslash\ Seed", r"Sponge"]
label_j_1 = [r"$1235$"]
label_j_2 = [r"$1236$"]
label_j_3 = [r"$1237$"]
label_j_4 = [r"$1238$"]
label_j_5 = [r"$1239$"]
label_j_6 = [r"$1240$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'Number of random defects in \% for $p \in \{0.91, 0.92, \dots, 0.98\}$')
plt.ylabel(r'Relative error $\|\nabla(\overline{u}_h - \widetilde{u}_h)\|_{L^2(\Omega)} / \|\nabla \overline{u}_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)

# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
legend_labels = numpy.concatenate([label_col_1, label_j_1, label_empty * 1, label_j_2, label_empty * 1, label_j_3, label_empty * 1, label_j_4, label_empty * 1, label_j_5, label_empty * 1, label_j_6, label_empty * 1])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 7, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# Ticks
ticks = sorted(set(x1[start1:] + x2[start1:] + x3[start1:] + x4[start1:] + x5[start1:] + x6[start1:]))
labels = []
for i in range(len(ticks)):
    labels.append(round(ticks[i] * 100 / num_pot_def, 1))

ax.set_xticklabels(labels)
plt.xticks(ticks, rotation=45)

# Show or save plot
plt.tight_layout()
plt.show()

plt.savefig("vsnumrandomdefects_multipoint_inversion.pgf") # save as PGF file which can be used in your document via `\input`
