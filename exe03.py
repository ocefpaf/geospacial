import cartopy.crs as ccrs
import matplotlib.pyplot as plt


projection = ccrs.PlateCarree()
fig, ax = plt.subplots(
    subplot_kw={"projection": projection},
    figsize=(9, 9)
)

dx = dy = 0.1
extent = [west-dx, south+dx, east-dy, north+dy]
ax.set_extent(extent)
ax.coastlines("10m")
gs.plot(ax=ax);