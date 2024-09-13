from app.domain.complex_number_library import Number


def test_sum():
    number = Number()
    assert number.sum(3, 5) == 8
    assert number.sum(-1, 1) == 0
    assert number.sum(-3, -7) == -10
    assert number.sum(0, 5) == 5
    assert number.sum(-1, 4) == 3


def test_divide():
    number = Number()
    assert number.divide(10, 2) == 5.0
    assert number.divide(7, 3) == 2.33
    assert number.divide(5, 0) == 0.0
