import pytest
import sys
import os

sys.path.append(os.path.join(
  os.getcwd(),
  'src'
))

import txt

def test_text():
  s = Text('Hello', 0.1, 0.3, color='forestgreen', size=14)

  assert s.content == 'Hello'
  assert s.x == 0.1
  assert s.y == 0.3
  assert s.color == 'forestgreen'
  assert s.size == 14
