import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from src import kata

class KataTest(unittest.TestCase):
    def assertEqualVerbose(self, expected, actual):
        print(f"{self._testMethodName} Input:{repr(self.inp)} Asserting: {expected} == {actual}")
        self.assertEqual(expected, actual)
    def test_add_empty(self):
        self.inp=""
        self.assertEqualVerbose(0, kata.add_num(self.inp))
    def test_add_float(self):
        self.inp="3,2.2"
        self.assertEqualVerbose(5.2, kata.add_num(self.inp))
    def test_add_negative(self):
        self.inp="3,-2 "
        self.assertRaisesRegex(Exception, "negatives not allowed: -2", kata.add_num, self.inp)
    def test_add_default_delim(self):
        self.inp="3,2"
        self.assertEqualVerbose(5, kata.add_num(self.inp))
    def test_add_optional_delim(self):
        self.inp="1\n3,2"
        self.assertEqualVerbose(6, kata.add_num(self.inp))
    def test_add_delim(self):
        self.inp="//+\n3+2"
        self.assertEqualVerbose(5, kata.add_num(self.inp))
    def test_add_special_delim(self):
        spcl=['.','-']
        for s in spcl:
            self.inp="//"+s+"\n3"+s+"2"+s+"1"
            self.assertEqualVerbose(6, kata.add_num(self.inp))
    def test_add_input_extractor_comma(self):
        self.inp="//+\n3,000+2,000"
        self.assertEqualVerbose(5000, kata.add_num(self.inp))
    def test_add_input_extractor_text(self):
        self.inp="3km , 2km, 1.5km"
        self.assertEqualVerbose(6.5, kata.add_num(self.inp))
if __name__=="__main__":
    unittest.main()
