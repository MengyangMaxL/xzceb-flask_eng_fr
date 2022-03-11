import unittest
from translator import englishToFrench,frenchToEnglish

class TestMyModule(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

    def test_englishToFrench_2(self):
        self.assertEqual(englishToFrench(),)
    	
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

    def test_frenchToEnglish_2(self):
        self.assertEqual(frenchToEnglish(),)
    

if __name__=='__main__':
    unittest.main()