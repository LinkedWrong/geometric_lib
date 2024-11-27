import unittest
import math

# Accessing modules without direct import
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

circle = type('circle', (), {'area': circle_area, 'perimeter': circle_perimeter})
rectangle = type('rectangle', (), {'area': rectangle_area, 'perimeter': rectangle_perimeter})
square = type('square', (), {'area': square_area, 'perimeter': square_perimeter})
triangle = type('triangle', (), {'area': triangle_area, 'perimeter': triangle_perimeter})




class TestCircle(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(1), math.pi)
        self.assertAlmostEqual(circle.area(0), 0)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5**2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle.perimeter(0), 0)
        self.assertAlmostEqual(circle.perimeter(2.1), 2 * math.pi * 2.1)



class TestRectangle(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(2, 3), 6)
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(4.2, 2.5), 10.5)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 3), 10)
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(4.2, 2.5), 13.4)




class TestSquare(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(3.5), 12.25)


    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(3.5), 14)




class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle.area(2, 3), 3)
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(4.2, 2.5), 5.25)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(2, 3, 4), 9)
        self.assertEqual(triangle.perimeter(0, 5, 5), 10)
        self.assertEqual(triangle.perimeter(4.2, 2.5, 3.1), 9.8)




if __name__ == '__main__':
    unittest.main()
