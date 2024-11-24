import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

mpl.use("pgf")

# Data

x = np.array([1, 3, 5, 7, 9, 11, 13])
ysponge81 = np.array([8.88536e+07, 1.43075e+08, 1.50897e+08, 1.50781e+08, 1.49965e+08, 1.4936e+08, 1.48981e+08])
ysponge27 = np.array([0.316576, 0.401247, 0.44604, 0.480961, 0.511415, 0.538523, 0.560387])
ysponge19 = np.array([0.455477, 0.55728, 0.619774, 0.66171, 0.693402])
ysponge11 = np.array([0.792301, 0.996414, 1.09567])

ycb27 = np.array([42.0444, 41.3739, 41.4596, 41.5174, 41.5561, 41.5854, 41.6156])
ycb19 = np.array([0.786222, 0.803607, 0.821298, 0.835003, 0.859145])
ycb11 = np.array([2.90335, 2.87926, 2.91387])

# Plot settings

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 0

# Plot
plt1 ,= plt.semilogy(x[start1:3], ysponge11[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(x[start2:5], ysponge19[start2:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(x[start3:], ysponge27[start3:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(x[start1:3], ycb11[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt5 ,= plt.semilogy(x[start2:5], ycb19[start2:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt6 ,= plt.semilogy(x[start3:], ycb27[start3:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, extra, plt1, plt4, extra, plt2, plt5, extra, plt3, plt6]

label_col_1 = [r"Pattern \textbackslash\ Size", r"Sponge", r"Checkerboard"]
label_j_1 = [r"$s = 11$"]
label_j_2 = [r"$s = 19$"]
label_j_3 = [r"$s = 27$"]
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

plt.savefig("relative_energy_errors_vs_numdefects.pgf") # save as PGF file which can be used in your document via `\input`
