import pytest
from src.exercise import division

def test_exercise(capsys):
    division(3,2)
    out, err = capsys.readouterr()
    assert out == "1.5\n", "Should read '1.5'"
