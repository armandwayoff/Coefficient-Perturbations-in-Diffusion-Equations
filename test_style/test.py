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

keys = np.array([9, 15, 21, 25, 31, 37, 41, 53, 63, 73, 81])

sponge_in_def_243_num = np.array([0.00226597, 0.000856153, 0.000430579, 0.00030511, 0.000205015, 0.000150599, 0.000124016, 7.50179e-05, 5.05088e-05, 3.73819e-05, 2.62716e-05])
sponge_in_def_243_denom = np.array([0.00614399, 0.00239381, 0.00126047, 0.00089636, 0.000580773, 0.000423903, 0.000352801, 0.000210689, 0.000139227, 0.000108035, 0.000100362])
sponge_in_def_243 = sponge_in_def_243_num / sponge_in_def_243_denom

sponge_far_def_243_num = np.array([0.000313408, 1.42325e-05, 3.58695e-06, 1.38873e-06, 4.16215e-07, 2.03167e-07, 1.22261e-07, 3.30803e-08, 1.29994e-08, 7.27749e-09, 3.65603e-09])
sponge_far_def_243_denom = np.array([0.00535021, 0.0018899, 0.00094219, 0.000650745, 0.000437383, 0.000293745, 0.000239472, 0.000137233, 0.000101406, 7.6374e-05, 6.46522e-05])
sponge_far_def_243 = sponge_far_def_243_num / sponge_far_def_243_denom

sponge_global_def_243_num = np.array([0.00827998, 0.000900457, 0.00154971, 0.00107902, 0.000222516, 0.000505711, 0.000413639, 0.000244972, 6.01075e-05, 0.000132447, 0.000104389])
sponge_global_def_243_denom = np.array([0.163304, 0.15428, 0.148118, 0.147086, 0.143841, 0.140388, 0.140147, 0.135427, 0.133224, 0.133138, 0.143438])
sponge_global_def_243 = sponge_global_def_243_num / sponge_global_def_243_denom

keys_detailed = np.array([9, 11, 13, 15, 17, 19, 21, 25, 27, 29, 31, 33, 35, 37, 41, 53, 57, 59, 61, 63, 65, 73, 81])
sponge_global_def_243_detailed_num = np.array([0.00827998, 0.00166593, 0.00405629, 0.000900457, 0.00235566, 0.000536359, 0.00154971, 0.00107902, 0.000266246, 0.000795803, 0.000222516, 0.000651067, 0.000160415, 0.000505711, 0.000413639, 0.000244972, 0.000204928, 6.95175e-05, 0.000188017, 6.01075e-05, 0.000165749, 0.000132447, 0.000104389])
sponge_global_def_243_detailed_denom = np.array([0.163304, 0.159004, 0.155802, 0.15428, 0.152009, 0.150139, 0.148118, 0.147086, 0.1505, 0.145596, 0.143841, 0.144022, 0.144082, 0.140388, 0.140147, 0.135427, 0.135214, 0.135296, 0.137936, 0.133224, 0.133918, 0.133138, 0.143438])
sponge_global_def_243_detailed = sponge_global_def_243_detailed_num / sponge_global_def_243_detailed_denom

cb_in_def_243_num = np.array([0.0025497, 0.00094145, 0.000482804, 0.000341884, 0.000214701, 0.000143569, 0.000115654, 6.48177e-05, 4.51819e-05, 3.8343e-05, 3.22457e-05])
cb_in_def_243_denom = np.array([0.00373797, 0.00127149, 0.000613856, 0.000435373, 0.000267956, 0.000186046, 0.000143158, 8.51403e-05, 5.71297e-05, 4.72529e-05, 3.64725e-05])
cb_in_def_243 = cb_in_def_243_num / cb_in_def_243_denom

cb_far_def_243_num = np.array([0.000212581, 2.05401e-05, 4.33244e-06, 1.92613e-06, 7.40971e-07, 3.27046e-07, 2.00403e-07, 6.08804e-08, 2.78861e-08, 1.54059e-08, 8.09265e-09])
cb_far_def_243_denom = np.array([0.00461307, 0.00160585, 0.0008004, 0.000546869, 0.000366171, 0.000246918, 0.000198745, 0.000114587, 8.27494e-05, 6.20782e-05, 5.16251e-05])
cb_far_def_243 = cb_far_def_243_num / cb_far_def_243_denom

cb_global_def_243_num = np.array([0.00344161, 0.00123486, 0.000642118, 0.000448143, 0.000280653, 0.000182179, 0.000150402, 7.97282e-05, 5.86847e-05, 5.1145e-05, 4.98978e-05])
cb_global_def_243_denom = np.array([0.152789, 0.131279, 0.116927, 0.110083, 0.10181, 0.096199, 0.0928082, 0.0843039, 0.0778266, 0.0755346, 0.0750252])
cb_global_def_243 = cb_global_def_243_num / cb_global_def_243_denom

keys_detailed_1 = np.array([9, 13, 17, 21, 25, 29, 33, 37, 41, 53, 57, 61, 65, 73, 81])
indices_1 = np.isin(keys_detailed, keys_detailed_1)
sponge_global_def_243_detailed_1 = sponge_global_def_243_detailed[indices_1]

keys_detailed_2 = [11, 15, 19, 27, 31, 35, 59, 63]
indices_2 = np.isin(keys_detailed, keys_detailed_2)
sponge_global_def_243_detailed_2 = sponge_global_def_243_detailed[indices_2]

res = linregress(np.log(keys_detailed_2), np.log(sponge_global_def_243_detailed_2))
# print(res.slope)

# Plot settings
f = plt.figure()
f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 1

# Plot

'''
plt1 ,= plt.loglog(keys[start1:], sponge_in_def_243[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.loglog(keys[start1:], sponge_far_def_243[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
"""
slope_marker((3.5 * 1e1, 5 * 1e-04), (-2.027, 1), 
              r"$2.027$",
              r"$1$",
              invert=True,
              text_kwargs={'color': 'blue'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (0,0,1), 'lw': 1, 'zorder': 2}
            )
"""
plt3 ,= plt.loglog(keys[start1:], sponge_global_def_243[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

"""
plt3 ,= plt.loglog(keys_detailed[start1:], sponge_global_def_243_detailed[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
slope_marker((2.5 * 1e1, 1e-02), (-1.905, 1), 
              r"$1.905$",
              r"$1$",
              invert=False,
              text_kwargs={'color': 'green'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (0,0.7,0), 'lw': 1, 'zorder': 2}
            )
slope_marker((3.3 * 1e1, 1e-03), (-1.794, 1), 
              r"$1.794$",
              r"$1$",
              invert=True,
              text_kwargs={'color': 'green'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (0,0.7,0), 'lw': 1, 'zorder': 2}
            )
"""
plt4 ,= plt.loglog(keys[start1:], cb_in_def_243[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
slope_marker((2.5 * 1e1, 6 * 1e-03), (-2.041, 1), 
              r"$2.041$",
              r"$1$",
              invert=False,
              text_kwargs={'color': 'green'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (0,0.7,0), 'lw': 1, 'zorder': 2}
            )
plt5 ,= plt.loglog(keys[start1:], cb_far_def_243[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
slope_marker((1.3 * 1e1, 3 * 1e-02), (-2.54, 1), 
              r"$2.540$",
              r"$1$",
              invert=False,
              text_kwargs={'color': 'blue'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (0,0,1), 'lw': 1, 'zorder': 2}
            )
plt6 ,= plt.loglog(keys[start1:], cb_global_def_243[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
"""
slope_marker((3 * 1e1, 1.5 * 1e-04), (-1.685, 1), 
              r"$1.685$",
              r"$1$",
              invert=True,
              text_kwargs={'color': 'red'},
              poly_kwargs={'fc': (0,0,0,1), 'ec': (1,0,0), 'lw': 1, 'zorder': 2}
            )
"""
'''

plt1 ,= plt.loglog(keys[start1:], sponge_in_def_243_denom[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.loglog(keys[start1:], sponge_far_def_243_denom[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.loglog(keys[start1:], sponge_global_def_243_denom[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.loglog(keys[start1:], cb_in_def_243_denom[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt5 ,= plt.loglog(keys[start1:], cb_far_def_243_denom[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt6 ,= plt.loglog(keys[start1:], cb_global_def_243_denom[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

"""
plt1 ,= plt.loglog(keys[start1:], sponge_in_def_243_num[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.loglog(keys[start1:], sponge_far_def_243_num[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.loglog(keys[start1:], sponge_global_def_243_num[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.loglog(keys[start1:], cb_in_def_243_num[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt5 ,= plt.loglog(keys[start1:], cb_far_def_243_num[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt6 ,= plt.loglog(keys[start1:], cb_global_def_243_num[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
"""

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, extra, plt1, plt4, extra, plt2, plt5, extra, plt3, plt6]
# legend_handle = [extra, extra, extra, plt1, extra, plt2, extra, plt3]
# legend_handle = [extra, extra, extra, plt4, extra, plt5, extra, plt6]
# legend_handle = [extra, extra, extra, plt3]

label_col_1 = [r"Pattern \textbackslash\ Size", r"Sponge", r"Checkerboard"] 
label_j_1 = [r"$f$ exact. in"]
label_j_2 = [r"$f$ far away"]
label_j_3 = [r"$f \equiv 1$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'Pattern size')
# plt.ylabel(r'Relative error $\|\nabla(u_h - \overline{u}_h)\|_{L^2(\Omega)} / \|\nabla u_h\|_{L^2(\Omega)}$')
plt.ylabel(r'$ \|\nabla u_h\|_{L^2(\Omega)}$')

# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)
plt.gca().yaxis.set_minor_locator(LogLocator(numticks=15,subs=np.arange(2,10)))


# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
# legend_labels = numpy.concatenate([label_col_1, label_j_1, label_empty * 1])
legend_labels = numpy.concatenate([label_col_1, label_j_1, label_empty * 2, label_j_2, label_empty * 2, label_j_3, label_empty * 2])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 4, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# plt.xticks(keys_detailed[start1:], keys_detailed[start1:], rotation=45)

# Show or save plot
# plt.savefig("relative_energy_errors_vs_femsize.png", dpi=300)  # Save as PNG
plt.tight_layout()
plt.show()

# plt.savefig("vspatternsize_sponge_global_detailed.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vspatternsize_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vspatternsize_sponge_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vspatternsize_cb_numdenom_relative_energy_errors.pgf") # save as PGF file which can be used in your document via `\input`
# plt.savefig("vspatternsize_num.pgf") # save as PGF file which can be used in your document via `\input`
plt.savefig("vspatternsize_denom.pgf") # save as PGF file which can be used in your document via `\input`
