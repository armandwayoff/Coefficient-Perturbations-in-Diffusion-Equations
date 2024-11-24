import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl

# mpl.use("pgf")

# Use PGF for LaTeX export

"""
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",  # or xelatex or lualatex
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})
"""


size = 11
amin, amax = 0, 10

A1 = np.random.random((size,size))

for i in range(size):
    for j in range(size):
        # if (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
        if (i > 0 and j > 0) and (i < size - 1 and j < size - 1) and (((i + 1) % 2 == 0 and (j + 1) % 2 == 0) or (i % 2 == 0 and j % 2 == 0)):
            A1[i,j] = amax
        else:
            A1[i,j] = amin

ncb = int((size - 1) / 2)
A1[ncb,ncb] = amin
A2 = A1.copy()
A2[ncb,ncb - 2] = amin
A2[ncb,ncb + 2] = amin
A3 = A2.copy()
A3[ncb,ncb - 4] = amin
A3[ncb,ncb + 4] = amin
AA = [A1, A2, A3]

# Set up figure and image grid
fig = plt.figure(figsize=(9.75, 3))

grid = ImageGrid(fig, 111,          # as in plt.subplot(111)
                 nrows_ncols=(1,3),
                 axes_pad=0.3,
                 share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="7%",
                 cbar_pad=0.3,
                 )

# Add data to image grid
for i, ax in enumerate(grid):
    im = ax.imshow(AA[i], cmap="Greys")
    
    # Remove the ticks on both axes
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Add a title to each subplot
grid[0].set_title("$1$ defect")
grid[1].set_title("$3$ defects")
grid[2].set_title("$5$ defects")


# Colorbar
cbar = ax.cax.colorbar(im, ticks=[amin, amax])
cbar.set_ticks([amin, amax])  # Set ticks at vmin and vmax
cbar.set_ticklabels(["$a_\mathrm{min}$", "$a_\mathrm{max}$"])  # Set custom labels


plt.tight_layout()    # Works, but may still require rect paramater to keep colorbar labels visible
plt.show()

# plt.savefig("multiple_defects_line_pattern.pgf") 