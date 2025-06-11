import math
import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_circumference(self):
        assert self.circle.circumference() == 2 * math.pi * self.circle.radius

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
