import matplotlib.pyplot as plt

class Text:
  def __init__(self, content, x, y, color='black', size=12):
    plt.text(x, y, content, color=color, fontsize=size)
