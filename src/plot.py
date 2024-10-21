import matplotlib.pyplot as plt

plt.rcParams['toolbar'] = 'None'

class Line:
  def __init__(self, x1, y1, x2, y2, color='black'):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.color = color
    x = [x1, x2]
    y = [y1, y2]
    plt.gca().set_aspect(1)
    plt.plot(x, y, color=color)
