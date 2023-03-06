import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour' ) # test translation from English to French
        self.assertEqual(englishToFrench(' '), ' ')  # test NULL input
    
class TestFrEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test translation French to English
        self.assertEqual(frenchToEnglish(' '), ' ') # test NULL input
        
unittest.main()