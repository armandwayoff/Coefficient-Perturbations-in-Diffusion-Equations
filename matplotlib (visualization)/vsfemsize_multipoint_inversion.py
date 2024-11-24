import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

mpl.use("pgf")

# Data

x = np.array([70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=10, size 27 checkerboard
y1 = np.array([0.00266208, 0.00226569, 0.00218429, 0.00178663, 0.00193874, 0.00316076,
              0.00326324, 0.00202335, 0.00167854, 0.00192078,  0.00177527, 0.00502418, 0.00219934, 
              0.00207302, 0.00184488, 0.00193628, 0.00702799, 0.00228338, 0.0022337])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=100, size 27 checkerboard
y2 = np.array([0.00467185, 0.00953295, 0.00714918, 0.00402709, 0.00447797, 0.00384258, 0.00395727, 0.007398, 0.0053469, 0.00493044, 0.00823577, 0.00488618, 0.00486281, 0.00610165, 0.0051229, 0.00651042, 0.0067311, 0.00453142, 0.00417261])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=50, size 27 checkerboard
y3 = np.array([0.00530753, 0.00939653, 0.00316189, 0.00327004, 0.00383546, 0.00337239, 0.00646584, 0.00487614, 0.00484394, 0.00453759, 0.00367021, 0.00385386, 0.00366955, 0.00851626, 0.00863592, 0.00844454, 0.0037733, 0.00373445, 0.00413423])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=5, size 27 checkerboard
y4 = np.array([0.000621123, 0.000817403, 0.00168234, 0.00198998, 0.00108908, 0.000969559, 0.0007806, 0.00074298, 0.000662342, 0.000743363, 0.000720384, 0.000736083, 0.000739095, 0.000730557, 0.000704058, 0.000741083, 0.000780176, 0.00080198, 0.000809756])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=1000, size 27 checkerboard
y5 = np.array([0.00553779, 0.00425131, 0.00688602, 0.0146016, 0.00625989, 0.00630352, 0.0114521, 0.00695844, 0.00736088, 0.00612611, 0.00683705, 0.00617013, 0.0069768, 0.00645682, 0.00747324, 0.00718411, 0.00864323, 0.00766025, 0.00737241])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=2, size 27 checkerboard
y6 = np.array([0.000108503, 0.000109577, 0.000116613, 0.000112088, 0.000115106, 0.000116714, 0.000117011, 0.000123043, 0.000113487, 0.000122425, 0.000122428, 0.000125828, 0.000123977, 0.000126089, 0.000119048, 0.000129804, 0.000136009, 0.000138857, 0.000148512])
# Seed=1234, 3 defects, global RHS, p=0.98, amax=3, size 27 checkerboard
y7 = np.array([0.00027253, 0.000289123, 0.000321763, 0.000298813, 0.000309712, 0.000362966, 0.00039156, 0.000558393, 0.000404492, 0.000779602, 0.000508759, 0.00174414, 0.000432761, 0.00043382, 0.000353836, 0.000340178, 0.000329336, 0.00031686, 0.000314078])

# Seed=1235, 3 defects, global RHS, p=0.98, amax=10, size 27 sponge
y1sponge = np.array([0.00161439, 0.00155363, 0.00143265, 0.00140391, 0.00145167, 0.00129845, 0.00132746, 0.00134625, 0.00149046, 0.00132994, 0.00130215, 0.00120654, 0.00125403, 0.00122019, 0.00133903, 0.00121487, 0.00125192, 0.00126536, 0.00118245])
# Seed=1235, 3 defects, global RHS, p=0.98, amax=100, size 27 sponge
y2sponge = np.array([0.00361004, 0.00403236, 0.00346604, 0.00351567, 0.00317413, 0.00286725, 0.00328225, 0.00285924, 0.00348176, 0.00256453, 0.00248527, 0.00230092, 0.00246441, 0.00233083, 0.0026306, 0.00214176, 0.00250071, 0.00235348, 0.00218807])
# Seed=1235, 3 defects, global RHS, p=0.98, amax=50, size 27 sponge
y3sponge = np.array([0.00312415, 0.00334772, 0.00282185, 0.00290879, 0.00272129, 0.00226717, 0.00248744, 0.00246939, 0.00296711, 0.00230862, 0.00223191, 0.00206192, 0.00219452, 0.00206465, 0.0023302, 0.0019599, 0.0022008, 0.0020943, 0.0019505])
# Seed=1235, 3 defects, global RHS, p=0.98, amax=5, size 27 sponge
y4sponge = np.array([0.000870813, 0.00082876, 0.000787731, 0.000769405, 0.000802652, 0.000766863, 0.000762645, 0.000772458, 0.000815086, 0.000768755, 0.000763607, 0.000716861, 0.000733522, 0.000727962, 0.000782753, 0.000735731, 0.00073155, 0.000756359, 0.000716188])
# Seed=1235, 3 defects, global RHS, p=0.98, amax=1000, size 27 sponge
y5sponge = np.array([0.00507899, 0.00535236, 0.00640604, 0.00562219, 0.00676909, 0.00605021, 0.00575097, 0.0048564, 0.00580238, 0.00441062, 0.00342369, 0.0039536, 0.00350812, 0.00586271, 0.00378751, 0.00306226, 0.00464501, 0.00358573, 0.00321545])
# Seed=1235, 3 defects, global RHS, p=0.98, amax=2, size 27 sponge
y6sponge = np.array([0.000163286, 0.000161164, 0.000158395, 0.000155201, 0.000158619, 0.000162872, 0.000160467, 0.000164283, 0.000164661, 0.000161362, 0.000163417, 0.000158341, 0.000159419, 0.000161401, 0.000169794, 0.000164733, 0.000159887, 0.000165771, 0.000161365])


# Plot settings

f = plt.figure()
# f.set_figwidth(5)
f.set_figheight(4)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 3, 5

# Plot
"""
plt1 ,= plt.semilogy(x[start1:], y1[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(x[start1:], y2[start1:], '-s', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(x[start1:], y3[start1:], '-s', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(x[start1:], y4[start1:], '-s', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb])
plt5 ,= plt.semilogy(x[start1:], y5[start1:], '-s', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0])
plt6 ,= plt.semilogy(x[start1:], y6[start1:], '-s', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb])
"""
plt1 ,= plt.semilogy(x[start1:], y1sponge[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(x[start1:], y2sponge[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
plt3 ,= plt.semilogy(x[start1:], y3sponge[start1:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])
plt4 ,= plt.semilogy(x[start1:], y4sponge[start1:], '-o', linewidth=linew, color=[0.0, cvalg, cvalb], markerfacecolor=[0.0, mfcvalg, mfcvalb])
plt5 ,= plt.semilogy(x[start1:], y5sponge[start1:], '-o', linewidth=linew, color=[cvalr, cvalg, 0.0], markerfacecolor=[mfcvalr, mfcvalg, 0.0])
plt6 ,= plt.semilogy(x[start1:], y6sponge[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, cvalb], markerfacecolor=[mfcvalr, 0.0, mfcvalb])

# plt7 ,= plt.semilogy(x[start1:], y7[start1:], '-s', linewidth=linew, color=[cvalr, cvalg, cvalb], markerfacecolor=[mfcvalr, mfcvalg, mfcvalb])


extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, plt6, extra, plt4, extra, plt1, extra, plt3, extra, plt2, extra, plt5]

label_col_1 = [r"Pattern \textbackslash\ Contrast", r"Sponge"]
label_j_1 = [r"$c = 10$"]
label_j_2 = [r"$c = 100$"]
label_j_3 = [r"$c = 50$"]
label_j_4 = [r"$c = 5$"]
label_j_5 = [r"$c = 1000$"]
label_j_6 = [r"$c = 2$"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'\textsc{fem} mesh size')
plt.ylabel(r'Relative error $\|\nabla(\overline{u}_h - \widetilde{u}_h)\|_{L^2(\Omega)} / \|\nabla \overline{u}_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
plt.grid(axis='both', which='minor', ls='dotted', alpha=1)

# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
legend_labels = numpy.concatenate([label_col_1, label_j_6, label_empty * 1, label_j_4, label_empty * 1, label_j_1, label_empty * 1, label_j_3, label_empty * 1, label_j_2, label_empty * 1, label_j_5, label_empty * 1])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 7, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# Ticks
plt.xticks(x[start1:])

# Show or save plot
plt.tight_layout()
plt.show()

plt.savefig("vsfemsize_multipoint_inversion_sponge.pgf") # save as PGF file which can be used in your document via `\input`
