import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.ticker import LogLocator
# from mpltools import annotation
from scipy.stats import linregress
from slope_marker import slope_marker

# mpl.use("pgf")

keys = np.array([2., 5., 10., 50., 100., 200., 300., 400., 500., 600., 700., 800., 900., 1000.])


sponge_9_global_def_243_num = np.array([0.00377351, 0.00693401, 0.00827998, 0.00954406, 0.00971822, 0.00980693, 0.00983675, 0.00985171, 0.0098607, 0.0098667, 0.00987099, 0.00987421, 0.00987671, 0.00987872])
sponge_9_global_def_243_denom = np.array([0.17319, 0.165194, 0.163304, 0.162511, 0.162481, 0.162473, 0.162472, 0.162471, 0.162471, 0.162471, 0.162471, 0.162471, 0.162471, 0.16247])
sponge_9_global_def_243 = sponge_9_global_def_243_num / sponge_9_global_def_243_denom

sponge_27_global_def_243_num = np.array([0.000135226, 0.00022849, 0.000266246, 0.000302145, 0.000307176, 0.000309748, 0.000310614, 0.000311049, 0.000311311, 0.000311485, 0.00031161, 0.000311704, 0.000311777, 0.000311835])
sponge_27_global_def_243_denom = np.array([0.166018, 0.153521, 0.1505, 0.149221, 0.149173, 0.14916, 0.149158, 0.149157, 0.149156, 0.149156, 0.149156, 0.149156, 0.149156, 0.149156])
sponge_27_global_def_243 = sponge_27_global_def_243_num / sponge_27_global_def_243_denom

sponge_81_global_def_243_num = np.array([4.66169e-05, 8.68648e-05, 0.000104389, 0.000121098, 0.00012342, 0.000124604, 0.000125003, 0.000125203, 0.000125323, 0.000125403, 0.00012546, 0.000125503, 0.000125537, 0.000125564])
sponge_81_global_def_243_denom = np.array([0.162724, 0.14731, 0.143438, 0.141783, 0.14172, 0.141704, 0.141701, 0.1417, 0.141699, 0.141699, 0.141699, 0.141699, 0.141699, 0.141699])
sponge_81_global_def_243 = sponge_81_global_def_243_num / sponge_81_global_def_243_denom

cb_9_global_def_243_num = np.array([0.00128612, 0.00250707, 0.00344161, 0.00562678, 0.00623822, 0.00660983, 0.00674555, 0.00681583, 0.00685881, 0.0068878, 0.00690868, 0.00692443, 0.00693674, 0.00694662])
cb_9_global_def_243_denom = np.array([0.168926, 0.157284, 0.152789, 0.147612, 0.146841, 0.146532, 0.146457, 0.146428, 0.146414, 0.146406, 0.146401, 0.146398, 0.146396, 0.146394])
cb_9_global_def_243 = cb_9_global_def_243_num / cb_9_global_def_243_denom

cb_27_global_def_243_num = np.array([0.000142642, 0.000291013, 0.000412838, 0.000651735, 0.000705431, 0.000735934, 0.000746722, 0.00075224, 0.000755592, 0.000757843, 0.00075946, 0.000760677, 0.000761626, 0.000762388])
cb_27_global_def_243_denom = np.array([0.150492, 0.122886, 0.109909, 0.0965519, 0.0950799, 0.0945346, 0.0944076, 0.0943587, 0.0943348, 0.0943214, 0.0943132, 0.0943077, 0.0943039, 0.0943011])
cb_27_global_def_243 = cb_27_global_def_243_num / cb_27_global_def_243_denom

cb_81_global_def_243_num = np.array([1.54925e-05, 3.51754e-05, 4.98978e-05, 7.10704e-05, 7.47984e-05, 7.67904e-05, 7.74747e-05, 7.78208e-05, 7.80297e-05, 7.81695e-05, 7.82697e-05, 7.83449e-05, 7.84035e-05, 7.84505e-05])
cb_81_global_def_243_denom = np.array([0.138685, 0.0955871, 0.0750252, 0.0582399, 0.0567986, 0.0562464, 0.0561096, 0.056055, 0.0560277, 0.0560122, 0.0560024, 0.055996, 0.0559915, 0.0559882])
cb_81_global_def_243 = cb_81_global_def_243_num / cb_81_global_def_243_denom

# Plot settings
f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 1

# Plot

plt1 ,= plt.loglog(keys[start1:], sponge_9_global_def_243[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.loglog(keys[start1:], sponge_27_global_def_243[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.loglog(keys[start1:], sponge_81_global_def_243[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

plt4 ,= plt.loglog(keys[start1:], cb_9_global_def_243[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt5 ,= plt.loglog(keys[start1:], cb_27_global_def_243[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt6 ,= plt.loglog(keys[start1:], cb_81_global_def_243[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, extra, plt1, plt4, extra, plt2, plt5, extra, plt3, plt6]
# legend_handle = [extra, extra, extra, plt1, extra, plt2, extra, plt3]

label_col_1 = [r"Pattern \textbackslash\ Size", r"Sponge", r"Checkerboard"]
label_j_1 = [r"$s = 9$"]
label_j_2 = [r"$s = 27$"]
label_j_3 = [r"$s = 81$"]
label_empty = [""]


# Labels and grid
plt.xlabel(r'Contrast')
plt.ylabel(r'Relative error $\|\nabla(u_h - \overline{u}_h)\|_{L^2(\Omega)} / \|\nabla u_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)
plt.gca().yaxis.set_minor_locator(LogLocator(numticks=15,subs=np.arange(2,10)))


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

# plt.xticks(keys[start1:])

# Show or save plot
# plt.savefig("relative_energy_errors_vs_femsize.png", dpi=300)  # Save as PNG
plt.tight_layout()
plt.show()

plt.savefig("vscontrast_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vscontrast_sponge_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vscontrast_cb_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
 