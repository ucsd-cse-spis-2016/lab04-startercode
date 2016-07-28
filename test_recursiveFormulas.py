# test_recursiveFormulas.py

import pytest
from recursiveFormulas import recProduct

def test_recProduct_4_5():
  assert recProduct(4,5) == 20


# Note to students: continue writing additional tests
# following the model above.

if __name__ == '__main__':
    pytest.main("--capture=sys --color=no")
