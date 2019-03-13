import unittest 
from fizzbuzz import *#(all)

class Fizzbuzztest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz('xyz','fgh'), 'fizz')
        self.assertEqual(fizz_buzz('xyzfg','ftrgh'),'buzz')
        self.assertEqual(fizz_buzz('xyz','h'),4)
