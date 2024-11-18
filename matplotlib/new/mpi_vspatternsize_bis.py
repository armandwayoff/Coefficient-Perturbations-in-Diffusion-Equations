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

keys = np.array([25, 27, 31, 37, 41, 53, 63, 73, 81])

sponge_global_def_100_1_1234_num = np.array([0.0, 0.0, 6.36491e-05, 0.000133348, 8.91757e-05, 5.40628e-05, 0.000160053, 0.000371916, 0.000207073])
sponge_global_def_100_1_1234_denom = np.array([0.15001, 0.13851, 0.13766, 0.131673, 0.132669, 0.118759, 0.110947, 0.109099, 0.106639])
sponge_global_def_100_1_1234 = sponge_global_def_100_1_1234_num / sponge_global_def_100_1_1234_denom

sponge_global_def_100_2_1234_num = np.array([0.000258832, 3.84994e-05, 0.000164445, 0.000633357, 0.000258792, 0.000283545, 0.000298334, 0.000397037, 0.000458917])
sponge_global_def_100_2_1234_denom = np.array([0.150751, 0.138751, 0.138218, 0.13235, 0.133324, 0.119239, 0.11173, 0.109826, 0.107341])
sponge_global_def_100_2_1234 = sponge_global_def_100_2_1234_num / sponge_global_def_100_2_1234_denom

sponge_global_def_100_3_1234_num = np.array([0.000297219, 0.000191458, 0.000184237, 0.00100311, 0.000880688, 0.000919634, 0.000395304, 0.000463453, 0.000657821])
sponge_global_def_100_3_1234_denom = np.array([0.150991, 0.139191, 0.138531, 0.132823, 0.133911, 0.120026, 0.112375, 0.110352, 0.107814])
sponge_global_def_100_3_1234 = sponge_global_def_100_3_1234_num / sponge_global_def_100_3_1234_denom

sponge_global_def_100_4_1234_num = np.array([0.000324548, 0.000235888, 0.000707991, 0.00106677, 0.000879344, 0.00179044, 0.00078596, 0.000650657, 0.000998947])
sponge_global_def_100_4_1234_denom = np.array([0.151198, 0.139593, 0.138714, 0.133318, 0.134437, 0.120824, 0.113105, 0.110938, 0.108333])
sponge_global_def_100_4_1234 = sponge_global_def_100_4_1234_num / sponge_global_def_100_4_1234_denom

sponge_global_def_100_5_1234_num = np.array([0.000982259, 0.00154905, 0.00126093, 0.00166719, 0.00140699, 0.00131752, 0.00117369, 0.00121221, 0.00144143])
sponge_global_def_100_5_1234_denom = np.array([0.151686, 0.140466, 0.139831, 0.134345, 0.13502, 0.121314, 0.113653, 0.111604, 0.108986])
sponge_global_def_100_5_1234 = sponge_global_def_100_5_1234_num / sponge_global_def_100_5_1234_denom

################################################

sponge_25_global_def_100_1234_denom = np.array([0.15001])

sponge_global_def_100_1234_num = np.vstack((sponge_global_def_100_1_1234_num, sponge_global_def_100_2_1234_num,
                                            sponge_global_def_100_3_1234_num, sponge_global_def_100_4_1234_num,
                                            sponge_global_def_100_5_1234_num))
sponge_global_def_100_1234_denom = np.vstack((sponge_global_def_100_1_1234_denom, sponge_global_def_100_2_1234_denom,
                                              sponge_global_def_100_3_1234_denom, sponge_global_def_100_4_1234_denom,
                                              sponge_global_def_100_5_1234_denom))

sponge_25_global_def_100_1234_num = np.array([0., 0.00025883, 0.00029722, 0.00032455, 0.00098226])
sponge_25_global_def_100_1234_denom = np.array([0.15001, 0.150751, 0.150991, 0.151198, 0.151686])

sponge_25_global_def_100_1234_num = sponge_global_def_100_1234_num[:, 8]
sponge_25_global_def_100_1234_denom = sponge_global_def_100_1234_denom[:, 8]

print(sponge_25_global_def_100_1234_num)
print(sponge_25_global_def_100_1234_denom)

# Plot settings
f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 1

# Plot

plt1 ,= plt.semilogy(keys[start1:], sponge_global_def_100_1_1234_num[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(keys[start1:], sponge_global_def_100_2_1234_num[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(keys[start1:], sponge_global_def_100_3_1234_num[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(keys[start1:], sponge_global_def_100_4_1234_num[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb])
plt5 ,= plt.semilogy(keys[start1:], sponge_global_def_100_5_1234_num[start1:], '-o', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb])


extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, 
                 extra, plt1, 
                 extra, plt2,
                 extra, plt3,
                 extra, plt4, 
                 extra, plt5
                 ]

label_col_1 = [r"Seed \textbackslash\ Proportion of perturbations", r"1234"]
label_j_1 = [r"$1\,\%$"]
label_j_2 = [r"$2\,\%$"]
label_j_3 = [r"$3\,\%$"]
label_j_4 = [r"$4\,\%$"]
label_j_5 = [r"$5\,\%$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'Pattern size')
plt.ylabel(r'Relative error $\|\nabla(u_h - \overline{u}_h)\|_{L^2(\Omega)} / \|\nabla u_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)
plt.gca().yaxis.set_minor_locator(LogLocator(numticks=15,subs=np.arange(2,10)))


# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
legend_labels = numpy.concatenate([label_col_1, 
                                   label_j_1, label_empty * 1, 
                                   label_j_2, label_empty * 1, 
                                   label_j_3, label_empty * 1, 
                                   label_j_4, label_empty * 1, 
                                   label_j_5, label_empty * 1])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 6, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

plt.xticks(keys[start1:])

# Show or save plot
# plt.savefig("relative_energy_errors_vs_femsize.png", dpi=300)  # Save as PNG
plt.tight_layout()
plt.show()

plt.savefig("mpi_vspatternsize.pgf") # save as PGF file which can be used in your document via `\input`
