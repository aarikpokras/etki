import pytest
import sys
import os

sys.path.append(os.path.join(
  os.getcwd(),
  'src'
))

import plot

def test_line():
  s = plot.Line(0, 0.1, 0.2, 0.25, color='purple')

  assert s.x1 == 0
  assert s.y1 == 0.1
  assert s.x2 == 0.2
  assert s.y2 == 0.25
  assert s.color == 'purple'
