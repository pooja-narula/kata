import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from src import kata

class KataTest(unittest.TestCase):
    def assertEqualVerbose(self, expected, actual):
        print(f"Asserting: {expected} == {actual}")
        self.assertEqual(expected, actual)
    def test_add(self):
        inp=" cds + od"
        self.assertEqualVerbose(0, kata.add_num(inp,"+"))
        inp=" 3 + 2.2 "
        self.assertEqualVerbose(5.2, kata.add_num(inp,"+"))
        inp=" 3 + 2 "
        self.assertEqualVerbose(5, kata.add_num(inp,"+"))
        inp=" 3,000 + 2 "
        self.assertEqualVerbose(3002, kata.add_num(inp,"+"))
        inp=" 3,00,000 + 0.2 "
        self.assertEqualVerbose(300000.2, kata.add_num(inp,"+"))
        inp=" 3,000 + 20,700.20 "
        self.assertEqualVerbose(23700.2, kata.add_num(inp,"+"))

if __name__=="__main__":
    unittest.main()
