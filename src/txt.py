import matplotlib.pyplot as plt

class Text:
  def __init__(self, content, x, y, color='black', size=12):
    self.x = x
    self.y = y
    self.content = content
    self.color = color
    self.size = size
    plt.text(x, y, content, color=color, fontsize=size)
