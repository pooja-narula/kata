import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from src import kata
kata=kata.Kata()
OKCYAN= '\033[96m'
OKGREEN= '\033[92m'
BOLD='\033[1m'
ENDC='\033[0m'
class KataTest(unittest.TestCase):
    def prettyPrint(self, testResult):
        fname=self._testMethodName.split("_")
        test_fname="".join(fname[1:2])
        test_case="_".join(fname[2:])
        print(f"[{test_fname}] {OKCYAN}[{test_case}]{ENDC}  Input: {OKGREEN}{BOLD}{repr(self.inp)}{ENDC} {testResult}")
    def assertEqualVerbose(self, expected, actual):
        self.prettyPrint(f'Asserting: {expected} == {actual}')
        self.assertEqual(expected, actual)
    def assertRaisesRegexVerbose(self, exception, regex, fn, arg):
        self.prettyPrint(f'Asserting exception == {regex}')
        self.assertRaisesRegex(exception, regex, fn, arg)
    def test_add_empty(self):
        self.inp=""
        self.assertEqualVerbose(0, kata.add_num(self.inp))
    def test_add_float(self):
        self.inp="3,2.2"
        self.assertEqualVerbose(5.2, kata.add_num(self.inp))
    def test_add_negative(self):
        self.inp="3,-2,-7 "
        self.assertRaisesRegexVerbose(Exception, "negatives not allowed: -2,-7", kata.add_num, self.inp)
    def test_add_default_delim(self):
        self.inp="3,2"
        self.assertEqualVerbose(5, kata.add_num(self.inp))
    def test_add_optional_delim(self):
        self.inp="1\n3,2"
        self.assertEqualVerbose(6, kata.add_num(self.inp))
    def test_add_delim(self):
        self.inp="//+\n3+2"
        self.assertEqualVerbose(5, kata.add_num(self.inp))
    def test_add_delim_anylength(self):
        self.inp="//+++\n3+++2"
        self.assertEqualVerbose(5, kata.add_num(self.inp))
    def test_add_multiple_delim(self):
        self.inp="//[++][*]\n3++2*5"
        self.assertEqualVerbose(10, kata.add_num(self.inp))
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
