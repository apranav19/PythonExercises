from triangle import Triangle, TriangleError
import unittest

class TriangleTests(unittest.TestCase):
    def test_triangles_with_negative_sides_are_illegal(self):
        self.assertRaises(
            TriangleError,
            Triangle, 3, 4, -5
        )
        
if __name__ == '__main__':
    unittest.main()
