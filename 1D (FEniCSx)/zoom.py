from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
"""
axins = zoomed_inset_axes(ax, 2, loc="lower center", 
                          axes_kwargs={"facecolor" : "none"})
"""
"""
ax_bbox = ax.get_position()
zoomed_width = 0.6
zoomed_height = 0.5
main_plot_center = (ax_bbox.x0 + ax_bbox.x1 - zoomed_width + 0.04) / 2

# Manually create an Axes object for the zoomed area and center it horizontally with the main plot
axins = fig.add_axes([main_plot_center, 0.05, zoomed_width, zoomed_height]) # [left, bottom, width, height]

P4.plot_solution(axins)
P5.plot_solution(axins)
P6.plot_solution(axins)
P7.plot_solution(axins)
P8.plot_solution(axins)

x1,x2,y1,y2 = 0.25,0.75, 0.06,0.084
axins.set_xlim(x1,x2)
axins.set_ylim(y1,y2)
axins.set_xticks([])
axins.set_yticks([])

pp,p1,p2 = mark_inset(ax,axins,loc1=1,loc2=2)
pp.set_fill(True)
pp.set_facecolor("none")
pp.set_edgecolor("k")
"""