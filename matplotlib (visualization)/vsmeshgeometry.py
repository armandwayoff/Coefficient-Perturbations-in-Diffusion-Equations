import matplotlib as mpl
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.ticker import LogLocator

# mpl.use("pgf")


# Data
x = np.array([236, 239, 242, 243, 244, 246, 250])
y = np.array([0.495974, 0.876021, 0.498762, 4.76016e+08, 0.501225, 0.505584, 0.503821])
y2 = np.array([0.305502, 0.315596, 0.309824, 0.316576, 0.307187, 0.31545, 0.310365])
y3 = np.array([0.0429325, 0.0748221, 0.0434108, 8.88536e+07, 0.0432376, 0.0462146, 0.04242])


# List of keys
keys = range(20, 250)

# List of values
values9 = [0.322852, 0.434041, 0.400771, 0.420442, 0.425349, 0.628037, 0.385078, 
          4.75672e+11, 0.402682, 0.643969, 0.434772, 0.704053, 0.393791, 
          0.596219, 0.442948, 0.657738, 0.473747, 0.645321, 0.406843, 
          0.571844, 0.449143, 0.586385, 0.468664, 0.756921, 0.434403, 
          6.03672e+10, 0.444943, 0.717045, 0.467392, 0.760179, 0.433128, 
          0.698486, 0.466062, 0.737607, 0.490296, 0.858324, 0.440242, 
          0.689794, 0.469565, 0.72938, 0.484848, 0.871604, 0.456638, 
          1.197e+10, 0.464552, 0.746339, 0.481349, 0.79605, 0.453399, 
          0.751623, 0.477986, 0.768419, 0.497774, 1.01931, 0.457759, 
          0.774366, 0.480273, 0.819241, 0.492653, 0.953704, 0.469146, 
          5.85321e+09, 0.475536, 0.75997, 0.488781, 0.821353, 0.465571, 
          0.779084, 0.485163, 0.780446, 0.501848, 1.11999, 0.468536, 
          0.8249, 0.486804, 0.864062, 0.497139, 1.00758, 0.477155, 
          2.02496e+10, 0.482518, 0.76733, 0.493366, 0.840782, 0.473643, 
          0.794812, 0.489953, 0.785496, 0.504273, 1.1778, 0.475854, 
          0.852494, 0.491208, 0.883159, 0.500037, 1.04243, 0.482723, 
          3.79915e+09, 0.487345, 0.771788, 0.496495, 0.856543, 0.479379, 
          0.804951, 0.493379, 0.78775, 0.505805, 1.2103, 0.48115, 
          0.867004, 0.494389, 0.889712, 0.502071, 1.06547, 0.486815, 
          3.05159e+09, 0.490885, 0.774723, 0.498785, 0.869793, 0.483668, 
          0.812175, 0.495955, 0.788787, 0.50686, 1.22865, 0.485151, 
          0.874412, 0.496802, 0.89048, 0.503589, 1.08127, 0.489949, 
          1.73009e+09, 0.493596, 0.776773, 0.500544, 0.881212, 0.487004, 
          0.817725, 0.497966, 0.789255, 0.507663, 1.23911, 0.488266, 
          0.877974, 0.498695, 0.888668, 0.504771, 1.09256, 0.492427, 
          5.2596e+08, 0.495743, 0.778272, 0.501947, 0.891229, 0.489679, 
          0.822229, 0.499583, 0.789448, 0.508315, 1.24507, 0.490757, 
          0.879426, 0.50022, 0.885776, 0.505721, 1.10094, 0.494442, 
          1.38954e+09, 0.49749, 0.77941, 0.503095, 0.900139, 0.491878, 
          0.826027, 0.500916, 0.789505, 0.508861, 1.2484, 0.492797, 
          0.879707, 0.501475, 0.882511, 0.506504, 1.10739, 0.496118, 
          1.24146e+09, 0.498941, 0.780308, 0.504056, 0.90815, 0.493722, 
          0.829322, 0.502036, 0.789497, 0.509325, 1.25014, 0.494509, 
          0.879333, 0.502526, 0.879208, 0.507162, 1.11252, 0.497539, 
          2.95962e+08, 0.50017, 0.78104, 0.504876, 0.91542, 0.495293, 
          0.832239, 0.502992, 0.789459, 0.509721, 1.25093, 0.495974, 
          0.8786, 0.503424, 0.876021, 0.507726, 1.11671, 0.498762, 
          4.76016e+08, 0.501225, 0.781651, 0.505584, 0.922066, 0.49665, 
          0.83486]

values9sponge_crisscross = [0.357792, 0.590676, 0.437568, 0.483597, 0.460262, 0.452999, 0.412795, 0.482201, 0.423362, 0.419095, 0.44923, 0.462767, 0.416615, 0.495904, 0.464036, 0.447118, 0.492229, 0.460212, 0.425044, 0.483012, 0.468015, 0.449217, 0.481041, 0.479492, 0.45027, 0.498184, 0.459087, 0.449591, 0.477483, 0.479793, 0.447864, 0.500552, 0.477094, 0.466895, 0.497416, 0.474814, 0.451419, 0.490291, 0.481037, 0.465445, 0.490547, 0.489601, 0.466779, 0.505215, 0.474283, 0.466518, 0.488218, 0.489365, 0.463556, 0.504941, 0.485287, 0.478594, 0.501056, 0.484327, 0.465623, 0.496414, 0.488375, 0.475947, 0.496243, 0.495533, 0.476478, 0.509184, 0.482732, 0.476926, 0.493831, 0.495248, 0.473134, 0.507765, 0.490727, 0.48593, 0.503722, 0.490605, 0.474377, 0.500697, 0.492979, 0.483041, 0.499891, 0.499393, 0.482934, 0.511576, 0.48818, 0.484003, 0.497355, 0.499254, 0.47961, 0.509728, 0.494537, 0.490977, 0.505672, 0.495007, 0.480326, 0.503742, 0.496077, 0.488164, 0.502336, 0.502154, 0.487554, 0.512947, 0.492027, 0.489141, 0.499833, 0.502178, 0.484306, 0.511188, 0.497344, 0.494706, 0.507142, 0.498265, 0.484697, 0.50599, 0.498316, 0.492047, 0.504062, 0.504254, 0.49101, 0.513706, 0.494903, 0.493022, 0.5017, 0.504413, 0.487888, 0.512322, 0.499496, 0.497602, 0.508288, 0.500785, 0.488094, 0.507717, 0.50005, 0.495095, 0.50536, 0.505918, 0.493674, 0.514189, 0.497138, 0.496023, 0.50317, 0.506172, 0.490724, 0.513229, 0.501199, 0.499929, 0.509201, 0.502801, 0.490835, 0.50909, 0.50147, 0.497554, 0.506393, 0.507278, 0.49578, 0.514587, 0.498927, 0.498383, 0.504364, 0.507583, 0.493035, 0.513964, 0.502583, 0.501847, 0.509937, 0.504457, 0.493103, 0.510212, 0.502672, 0.499583, 0.507252, 0.508416, 0.497488, 0.514965, 0.500393, 0.500278, 0.505355, 0.508729, 0.494959, 0.514568, 0.503732, 0.503456, 0.510527, 0.505844, 0.495013, 0.511149, 0.503709, 0.501292, 0.507987, 0.509385, 0.498911, 0.515334, 0.50162, 0.501842, 0.506193, 0.509674, 0.496589, 0.515069, 0.504702, 0.504826, 0.511, 0.507025, 0.496644, 0.511946, 0.504616, 0.502753, 0.508624, 0.510224, 0.500127, 0.51569, 0.502667, 0.503172, 0.506913, 0.510469, 0.497989, 0.515491, 0.505533, 0.506004, 0.51138, 0.508043, 0.498052, 0.512633, 0.505415, 0.504021, 0.509184, 0.510959, 0.501187, 0.516026, 0.503576, 0.504331, 0.507542, 0.511152, 0.499206, 0.515855]



# Plot settings

f, ax = plt.subplots()

# f.set_figwidth(5)
f.set_figheight(3)

linew = 1.5
cvalr, cvalg, cvalb = 1, 0.8, 1
mfcvalr, mfcvalg, mfcvalb = 0.7, 0.5, 0.7

start1, start2, start3 = 0, 0, 90

# Plot
# plt1 ,= plt.semilogy(x[start1:], y[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
# plt2 ,= plt.semilogy(x[start2:], y2[start2:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
# plt3 ,= plt.semilogy(x[start3:], y3[start3:], '-o', linewidth=linew, color=[0.0, cvalg, 0.0], markerfacecolor=[0.0, mfcvalg, 0.0])

plt1 ,= plt.semilogy(keys[start1:], values9[start1:], '-o', linewidth=linew, color=[cvalr, 0.0, 0.0], markerfacecolor=[mfcvalr, 0.0, 0.0])
plt2 ,= plt.semilogy(keys[start1:], values9sponge_crisscross[start1:], '-o', linewidth=linew, color=[0.0, 0.0, cvalb], markerfacecolor=[0.0, 0.0, mfcvalb])
# plt2 ,= plt.semilogy(keys[start1:], values9sponge_crisscross[start1:], marker='.', linestyle='solid', markersize=2, markerfacecolor=[0.0, 0.0, cvalb])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

legend_handle = [extra, extra, extra, plt1 , extra, plt2]

label_col_1 = [r"Pattern \textbackslash\ Mesh geometry", r"Sponge"]
label_j_1 = [r"Default"]
label_j_2 = [r"Criss cross"]
label_empty = [""]

# Labels and grid
plt.xlabel(r'\textsc{fem} mesh size')
plt.ylabel(r'$\|\nabla(u_h - \overline{u}_h)\|_{L^2(\Omega)} / \|\nabla u_h\|_{L^2(\Omega)}$')
# plt.grid(True, which='both')
plt.grid(axis='both', which='major', ls='-')
# plt.grid(axis='both', which='minor', ls='dotted', alpha=1)
# plt.gca().yaxis.set_minor_locator(LogLocator(numticks=15,subs=np.arange(2,10)))


# Legend
# plt.legend([r'$9$', r'$27$', r'Sponge: $81$', r'$9$', r'$27$', r'Checkerboard: $81$'], loc='upper center', ncol=3)

#organize labels for table construction
legend_labels = numpy.concatenate([label_col_1, label_j_1, label_empty * 1, label_j_2, label_empty * 1])

#Create legend
plt.legend(legend_handle, legend_labels, 
          # loc = 'upper center', 
          bbox_to_anchor=(0, 1, 1, 0), loc="lower center",
          # bbox_to_anchor=(0.5, 1.2), loc='upper center',
          ncol = 3, shadow = False, handletextpad = -2,
          columnspacing=1, labelspacing=0.8)

# Ticks
ticks9 = [27, 45, 63, 81, 99, 117, 135, 153, 171, 189, 207, 225, 243]

xticks = sorted(set(ticks9))
yticks = [10**0, 10**8, 10**12]

plt.xticks(xticks, rotation=0)
plt.yticks(yticks, rotation=0)


# Iterate over tick labels and color them one by one
for i, tick in enumerate(ax.get_xticklabels()):
    if xticks[i] in ticks9:
        tick.set_color([cvalr, 0.0, 0.0])   

# Show or save plot
plt.tight_layout()
plt.show()

# plt.savefig("vsmeshgeometry.pgf") # save as PGF file which can be used in your document via `\input`