import unittest
import solution
   
class SolutionTest(unittest.TestCase):
    """Test solution"""
    def setUp(self):
        pass
    def test_solution1(self):
        """run first test"""
        self.assertEqual(solution.check(2, 5,[0.6, 0.6]), 7.000000)
    def test_solution2(self):
        """run first test"""
        self.assertEqual(solution.check(1, 20,[1]), 20.000000)
    def test_solution3(self):
        """run first test"""
        self.assertEqual(solution.check(3, 4,[1, 0.9, 0.1]), 4.500000)

    if __name__ == '__main__':
        unittest.main()


        





