#https://stackoverflow.com/questions/28476117/easy-openstreetmap-tile-displaying-for-python
import matplotlib.pyplot as plt
import geotiler
file_name = "plot_points.png"
points = eval(input("List of points: "))

x = []
y = []
locations = []

for lat, lon in points:
    locations.append((lon, lat))
    x.append(lon)
    y.append(lat)

limUpperX = max(x)
limLowerX = min(x)
limUpperY = max(y)
limLowerY = min(y)
paddingX = (limUpperX - limLowerX) * 0.25
paddingY = (limUpperY - limLowerY) * 0.25

map_data = geotiler.Map(
    extent=(limLowerX - paddingX, limLowerY - paddingY, limUpperX + paddingX, limUpperY + paddingY), zoom=16)
img = geotiler.render_map(map_data)
fig = plt.figure(figsize=(100, 100))
ax = plt.subplot(111)
ax.imshow(img)
xx, yy = zip(*(map_data.rev_geocode(point) for point in locations))
ax.scatter(xx, yy, s=50, c='r')
plt.axis('off')
plt.savefig(file_name, bbox_inches='tight', pad_inches=0)
