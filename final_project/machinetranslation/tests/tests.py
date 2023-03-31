'''fgd'''
import unittest
from machinetranslation import translator
class test_english_to_french(unittest.TestCase):
    '''fs'''
    def test1(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')
class test_french_to_english(unittest.TestCase):
    '''fs'''
    def test1(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
unittest.main()
