import cartopy.io.img_tiles as cimgt


url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
esri = cimgt.GoogleTiles(url=url)

fig, ax = plt.subplots(
    figsize=(14, 14),
    subplot_kw={"projection": esri.crs}
)

ax.set_extent(extent)
ax.add_image(esri, 11)
# ax.images[0].write_png("data/esri-image-floripa.png")

data = sul.groupby("balneario_nome").mean()
ax.plot(
    data["lon"], data["lat"], linestyle="none",
    marker="o", label="Sul", transform=ccrs.PlateCarree(),
)

data = norte.groupby("balneario_nome").mean()
ax.plot(
    data["lon"], data["lat"], linestyle="none",
    marker="o", label="Norte", transform=ccrs.PlateCarree()
);