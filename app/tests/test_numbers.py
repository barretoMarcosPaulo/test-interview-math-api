from app.domain.complex_number_library import Numbers


def test_sum_valid_input():
    numbers = Numbers()
    assert numbers.sum([1, 2, 3, 4, 5]) == 15
    assert numbers.sum([10, 20, 30]) == 60
    assert numbers.sum([0, 0, 0]) == 0


def test_sum_with_negative_numbers():
    numbers = Numbers()
    assert numbers.sum([-1, -2, -3]) == -6
    assert numbers.sum([-1, 1, -2, 2]) == 0
    assert numbers.sum([10, -5, -5]) == 0


def test_sum_empty_list():
    numbers = Numbers()
    assert numbers.sum([]) == 0


def test_average_valid_input():
    numbers = Numbers()
    assert numbers.average([1, 2, 3, 4, 5]) == 3.0
    assert numbers.average([10, 20, 30, 40]) == 25.0
    assert numbers.average([0, 0, 0, 0]) == 0.0


def test_average_with_negative_numbers():
    numbers = Numbers()
    assert numbers.average([-1, -2, -3]) == -2.0
    assert numbers.average([-1, 1, -2, 2]) == 0.0
    assert numbers.average([10, -5, -5]) == 0.0


def test_average_empty_list():
    numbers = Numbers()
    assert numbers.average([]) == 0.0


def test_average_single_element():
    numbers = Numbers()
    assert numbers.average([5]) == 5.0


def test_average_rounding():
    numbers = Numbers()
    assert numbers.average([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5.0
    assert (
        numbers.average([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        == 1.0
    )
