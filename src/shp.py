import matplotlib.pyplot as plt
import matplotlib.patches as shp

plt.rcParams['toolbar'] = 'None'

fig, ax = plt.subplots()

# Self variables allow the user to reference them, e.g. shapevariable.property

class Shape:
  def adda(self, shapevar):
    ax.add_artist(shapevar)
    plt.gca().set_aspect(1)

  def setSelf(self, x, y, color, fill, radius=None, width=None, height=None, borderradius=None):
    self.x = x
    self.y = y
    self.color = color
    self.fill = fill
    self.radius = radius
    self.width = width
    self.height = height
    self.borderradius = borderradius

class Circle(Shape):
  def __init__(self, x, y, radius, color='black', fill=True):
    self.setSelf(x, y, color, fill, radius)
    c = shp.Circle((self.x, self.y), self.radius, color=self.color, fill=self.fill)
    self.adda(c)

  def __str__(self):
    return f'Circle({self.x}, {self.y}, {self.radius}, color={self.color}, fill={self.fill})'


class Rect(Shape):
  def __init__(self, x, y, width, height, color='black', fill=True, borderradius=0):
    self.setSelf(x, y, color, fill, width=width, height=height, borderradius=borderradius)
    if (borderradius == 0):  # Trick the user into thinking the rounded Rect is the same shape (silly user)
      r = shp.Rectangle((x, y), width, height, color=color, fill=fill)
      self.adda(r)
    else:
      boxS = shp.BoxStyle.Round(
        pad=0.1,
        rounding_size=borderradius
      )
      r = shp.FancyBboxPatch((x, y), width, height, boxS, color=color, fill=fill)
      self.adda(r)

  def __str__(self):
    return f"""Rect({self.x}, {self.y}, {self.width}, {self.height},
    color={self.color}, fill={self.fill}, borderradius={self.borderradius})"""


pth = shp.Path

class Polygon(Shape):
  def __init__(self, vertices, fillcolor='black', bordercolor='black'):
    self.vertices = vertices
    self.fillcolor = fillcolor
    self.bordercolor = bordercolor
    if (type(vertices) is not list):
      raise TypeError("Vertices should be a list")
    else:
      codes = [pth.MOVETO]
      i = 0
      while i < len(vertices) - 2:  # C-style for statement, variable for vertices
        codes.append(pth.LINETO)
        i += 1
      codes.append(pth.CLOSEPOLY)
      path = shp.Path(vertices, codes)
      p = shp.PathPatch(path, facecolor=fillcolor, edgecolor=bordercolor)
      self.adda(p)

  def __str__(self):
    return f'Polygon({self.vertices})'


class Oval(Shape):
  def __init__(self, x, y, width, height, color='black', fill=True, rotateAngle=0):
    self.setSelf(x, y, width, height)
    self.rotateAngle = rotateAngle
    o = shp.Ellipse((x, y), width, height, angle=rotateAngle, color=color, fill=fill)
    self.adda(o)
