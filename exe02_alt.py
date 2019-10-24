fig, ax = plt.subplots(
    figsize=(14, 14),
    subplot_kw={"projection": esri.crs}
)

img = plt.imread("data/esri-image-floripa.png")
img_extent = [-5439870.428999424, -5361598.912035404, -3248267.9540068433, -3150428.5578018166]
ax.imshow(img, transform=esri.crs, extent=img_extent, origin="upper");
ax.set_extent(extent)

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