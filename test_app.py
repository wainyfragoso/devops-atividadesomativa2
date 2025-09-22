import pytest
from main import soma, subtrai, multiplica, divide, eh_par

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 2) == 3

def test_multiplica():
    assert multiplica(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(5) is False
