import matplotlib.pyplot as plt
import matplotlib.patches as shp

plt.rcParams['toolbar'] = 'None'

fig, ax = plt.subplots()

# Self variables allow the user to reference them, e.g. shapevariable.property

class Shape:
  def adda(self, shapevar):
    ax.add_artist(shapevar)
    plt.gca().set_aspect(1)

  def setSelf(self, x, y, fillcolor, bordercolor, radius=None, width=None, height=None, borderradius=None,
              rotateAngle=0):
    self.x = x
    self.y = y
    self.bordercolor = bordercolor
    self.fillcolor = fillcolor
    self.radius = radius
    self.width = width
    self.height = height
    self.borderradius = borderradius
    self.rotateAngle = rotateAngle

class Circle(Shape):
  def __init__(self, x, y, radius, fillcolor='black', bordercolor='black'):
    self.setSelf(x, y, fillcolor=fillcolor, bordercolor=bordercolor, radius=radius)
    c = shp.Circle((self.x, self.y), self.radius, facecolor=self.fillcolor, edgecolor=self.bordercolor)
    self.adda(c)

  def __str__(self):
    return f'Circle({self.x}, {self.y}, {self.radius}, color={self.color}, fill={self.fill})'


class Rect(Shape):
  def __init__(self, x, y, width, height, fillcolor='black', bordercolor='black', borderradius=0, rotateAngle=0):
    self.setSelf(x, y, width=width, height=height, bordercolor=bordercolor, fillcolor=fillcolor,
                 borderradius=borderradius, rotateAngle=rotateAngle)
    if (borderradius == 0):
      r = shp.Rectangle((x, y), width, height, facecolor=fillcolor, edgecolor=bordercolor, angle=rotateAngle)
      self.adda(r)
    else:
      boxS = shp.BoxStyle.Round(
        pad=0.1,
        rounding_size=borderradius
      )
      r = shp.FancyBboxPatch((x, y), width, height, boxS, facecolor=fillcolor, edgecolor=bordercolor)
      self.adda(r)

  def __str__(self):
    return f"""Rect({self.x}, {self.y}, {self.width}, {self.height},
    fillcolor={self.fillcolor}, bordercolor={self.bordercolor}, borderradius={self.borderradius})"""


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
    return f'Polygon({self.vertices}, fillcolor={self.fillcolor}, bordercolor={self.bordercolor})'


class Oval(Shape):
  def __init__(self, x, y, width, height, fillcolor='black', bordercolor='black', rotateAngle=0):
    self.setSelf(x, y, width=width, height=height, fillcolor=fillcolor, bordercolor=bordercolor,
                 rotateAngle=rotateAngle)
    o = shp.Ellipse((x, y), width, height, angle=rotateAngle, edgecolor=bordercolor, facecolor=fillcolor)
    self.adda(o)

  def __str__(self):
    return f"""Oval({self.x}, {self.y}, {self.width}, {self.height}, fillcolor={self.fillcolor},
    bordercolor={self.bordercolor}, rotateAngle={self.rotateAngle})"""
