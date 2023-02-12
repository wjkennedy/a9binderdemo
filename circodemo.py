from pycirclize import Circos
import random
import numpy as np
random.seed(0)
np.random.seed(0)

# Define the size of each sector based on the number of projects in each group
sectors = {
    "Super A": 30,
    "Sub A": 20,
    "Group": 25,
    "Project": 10,
    "Issue": 5
}

# Initialize the circos plot
circos = Circos(sectors, space=5)

colors = ["tomato", "skyblue", "limegreen", "gold", "purple"]
cmaps = ["bwr", "viridis", "Spectral", "Reds", "Blues"]

# Add text and data to each sector
for idx, sector in enumerate(circos.sectors):
    sector.text(sector.name, size=12)

    # Plot a random heatmap for each sector
    heatmap_track = sector.add_track((70, 85))
    matrix_data = np.random.randint(0, 100, (5, int(sector.size)))
    heatmap_track.axis(ec="grey")
    heatmap_track.heatmap(matrix_data, cmap=cmaps[idx])

    # Plot a random bar chart for each sector
    bar_track = sector.add_track((85, 100))
    x = np.arange(0, int(sector.size)) + 0.5
    height = np.random.randint(1, 10, int(sector.size))
    bar_track.bar(x, height, facecolor=colors[idx], ec="grey", lw=0.5, hatch="//")

fig = circos.plotfig()
