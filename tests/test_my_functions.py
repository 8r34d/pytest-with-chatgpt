import pytest
import time
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add("i like ", "bread")
    assert result == "i like bread"


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    # pytest tests -m slow
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="feature is broken")
def test_skip_example():
    result = my_functions.add(1, 4)
    assert result == 5


@pytest.mark.xfail(reason="cannot divide by zero")
def test_xfail_example():
    my_functions.divide(10, 0)
