import unittest

from translator import english_to_french, french_to_english

class TestEnFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour' ) # test translation from English to French
        self.assertEqual(english_to_french(' '), ' ')  # test NULL input
    
class TestFrEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test translation French to English
        self.assertEqual(french_to_english(' '), ' ') # test NULL input
        
unittest.main()