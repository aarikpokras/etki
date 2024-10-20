import matplotlib.pyplot as plt
import matplotlib.patches as shp

plt.rcParams['toolbar'] = 'None'

fig, ax = plt.subplots()

# Self variables allow the user to reference them, e.g. shapevariable.property

class Circle:
  def __init__(self, x, y, radius, color='black', fill=True):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.fill = fill
    c = shp.Circle((self.x, self.y), self.radius, color=self.color, fill=self.fill)
    ax.add_artist(c)
    plt.gca().set_aspect(1)

class Rect:
  def __init__(self, x, y, width, height, color='black', fill=True, borderradius=0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.fill = fill
    self.borderradius = borderradius
    if (borderradius == 0): # Trick the user into thinking the rounded Rect is the same shape (silly user)
      r = shp.Rectangle((x, y), width, height, color=color, fill=fill)
      ax.add_artist(r)
      plt.gca().set_aspect(1)
    else:
      boxS = shp.BoxStyle.Round(
      pad=0.1,
      rounding_size=borderradius
      )
      r = shp.FancyBboxPatch((x, y), width, height, boxS, color=color, fill=fill)
      ax.add_artist(r)
      plt.gca().set_aspect(1)
