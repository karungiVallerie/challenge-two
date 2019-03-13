from vowel import string_vowel
import unittest

class TestVowel(unittest.TestCase):
    def test_vowel(self):
        result = string_vowel('word')
        print("result>>>", result)
        self.assertEqual(result, ('o',0))
if __name__ =='__main__':
    unittest.main()