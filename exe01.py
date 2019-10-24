from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


projection = ccrs.PlateCarree()
fig, ax = plt.subplots(
    subplot_kw={"projection": projection},
    figsize=(9, 9)
)

ax.set_extent(extent)
ax.add_geometries(floripa_outline, projection, facecolor='0.7', edgecolor='k')

gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

sul = floripa.loc[floripa["lat"] < lat]
norte = floripa.loc[floripa["lat"] >= lat]

data = sul.groupby("balneario_nome").mean()
ax.plot(
    data["lon"], data["lat"], linestyle="none",
    marker="o", label="Sul"
)

data = norte.groupby("balneario_nome").mean()
ax.plot(
    data["lon"], data["lat"], linestyle="none",
    marker="o", label="Norte"
)

ax.legend();