import matplotlib.patches as shp
import matplotlib.pyplot as plt

plt.rcParams['toolbar'] = 'None'

pth = shp.Path

fig, ax = plt.subplots()

class Polygon:
  def __init__(self, vertices):
    self.vertices = vertices
    if (type(vertices) != list):
      raise TypeError("Vertices should be a list")
    else:
      codes = [pth.MOVETO]
      i = 0
      while i < len(vertices) - 2: # C-style for statement, variable for the vertices list
        codes.append(pth.LINETO)
        i += 1
      codes.append(pth.CLOSEPOLY)
      path = shp.Path(vertices, codes)
      p = shp.PathPatch(path, facecolor='black')
      ax.add_artist(p)
