import pytest
from .shp import Rect, Circle, Polygon

def test_rect():
  s = Rect(0.4, 0.3, 0.1, 0.24, color='green', fill=False, borderradius=0.1)

  assert s.x == 0.4
  assert s.y == 0.3
  assert s.width == 0.1
  assert s.height == 0.24
  assert s.color == 'green'
  assert s.fill == False
  assert s.borderradius == 0.1

def test_circle():
  s = Circle(0.1, 0.3, 0.2, color='red', fill=True)

  assert s.x == 0.1
  assert s.y == 0.3
  assert s.radius == 0.2
  assert s.color == 'red'
  assert s.fill == True

def test_poly():
  s = Polygon(
    [
      (1, 1),
      (2, 1),
      (2, 2),
      (1, 2),
      (1, 1)
    ]
  )

  assert s.vertices == [(1, 1), (2, 1), (2, 2), (1, 2), (1, 1)]
