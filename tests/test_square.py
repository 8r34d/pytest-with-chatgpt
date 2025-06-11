import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_circumference", [(5, 20), (4, 16), (9, 36)])
def test_multiple_square_circumferences(side_length, expected_circumference):
    assert shapes.Square(side_length).circumference() == expected_circumference
