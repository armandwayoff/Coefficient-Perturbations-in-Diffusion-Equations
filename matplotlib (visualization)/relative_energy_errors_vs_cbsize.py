import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# mpl.use("pgf")

x = np.array([9, 15, 21, 25, 31, 37, 41, 53, 63, 73, 81])

y2 = np.array([0.96955, 0.569886, 0.403971, 0.336314, 0.257441, 0.219014, 0.195993, 0.145214, 0.11383, 0.102295, 0.0907943])  # sponge pattern f exactly in the defect block
y3 = np.array([4.76016e+08, 0.602729, 2.46625, 0.830233, 0.258869, 0.225821, 0.320712, 0.110813, 0.109032, 0.412448, 8.88536e+07]) # sponge pattern f=1
y4 = np.array([0.481949, 0.28411, 0.20221, 0.16354, 0.123732, 0.101429, 0.093669, 0.0651953, 0.0510991, 0.0476644, 0.0488627]) # sponge pattern f far away from the defect block
y5 = np.array([0.322697, 0.190411, 0.132675, 0.11221, 0.0885265, 0.0734998, 0.0669462, 0.0482137, 0.0382324, 0.0350658, 0.0298518]) # checkerboard pattern f far away from the defect block
y6 = np.array([0.99866, 0.591164, 0.408771, 0.346439, 0.264211, 0.220872, 0.19985, 0.149747, 0.109593, 0.0980356, 0.0899418]) # checkerboard pattern f exactly in the defect block
y7 = np.array([3.0017, 1.18449, 1.6402, 0.595692, 0.375667, 1.81017, 0.365562, 0.192765, 0.179254, 0.141179, 0.118998]) # checkerboard pattern f=1

# Plot settings

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 1

# Plot
# plt1 ,= plt.semilogy(x[start1:], y2[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt1 ,= plt.semilogy(x[start1:], y2[start1:], color=[0.0, 0.0, cvalb], marker='.', linestyle='solid', markersize=18, markerfacecolor='none')
plt2 ,= plt.semilogy(x[start2:], y4[start2:], color=[cvalr, 0.0, 0.0], marker='.', linestyle='solid', markersize=18, markerfacecolor='none')
plt3 ,= plt.semilogy(x[start3:-1], y3[start3:-1], color=[0.0, cvalg, 0.0], marker='.', linestyle='solid', markersize=24, markerfacecolor='none')
plt4 ,= plt.semilogy(x[start1:], y6[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
# plt4 ,= plt.semilogy(x[start1:], y6[start1:], color='b', marker='.', linestyle='solid', markersize=12, markerfacecolor='white')
plt5 ,= plt.semilogy(x[start2:], y5[start2:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt6 ,= plt.semilogy(x[start3:], y7[start3:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

# legend_handle = [extra, extra, extra, extra, plt2, plt5, extra, plt1, plt4]
legend_handle = [extra, extra, extra, extra, plt2, plt5, extra, plt1, plt4 , extra , plt3, plt6]

label_col_1 = [r"Pattern \textbackslash\ RHS", r"Sponge", r"Checkerboard"]
label_j_1 = [r"$f$ far away"]
label_j_2 = [r"$f$ exact. in"]
label_j_3 = [r"$f \equiv 1$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'Pattern size')
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
# plt.savefig("relative_energy_errors_vs_femsize.png", dpi=300)  # Save as PNG
plt.tight_layout()
plt.show()

# plt.savefig("relative_energy_errors_vs_cbsize.pgf") # save as PGF file which can be used in your document via `\input`
