import numpy as np
import matplotlib as plt
from matplotlib import pyplot

# grid
N    = 20000                   # total length of sides for square grid in m
SIZE_TILE = 1.5                # size per grid tile in meters

class Grid:
    def __init__(self, N, SIZE_TILE):
        np.array(N / SIZE_TILE, N / SIZE_TILE)


    def grid(N, SIZE_TILE):
        # make values from -5 to 5, for this example
        zvals = np.random.rand(100,100)*10-5

        # make a color map of fixed colors
        cmap = plt.colors.ListedColormap(['blue','black','red'])
        bounds=[-6,-2,2,6]
        norm = plt.colors.BoundaryNorm(bounds, cmap.N)

        # tell imshow about color map so that only set colors are used
        img = pyplot.imshow(zvals,interpolation='nearest',
                            cmap = cmap,norm=norm)

        # make a color bar
        pyplot.colorbar(img,cmap=cmap,
                        norm=norm,boundaries=bounds,ticks=[-5,0,5])

        pyplot.show()

class Graph:
    def __init__(nodes, edges):
        