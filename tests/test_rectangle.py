
def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_circumference(my_rectangle):
    assert my_rectangle.circumference() == 10 * 2 + 20 * 2


def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle

