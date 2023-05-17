import unittest
from translator import english_to_french, french_to_english

class TranslatorF2ETestCase(unittest.TestCase):

    # Test for null input in french_to_english
    def test_null_input_french_to_english(self):
        result = french_to_english(None)
        self.assertNotEqual(result, "Hello")
        print("french_to_english -  assertNotEqual Successful")

    # Test translation of the word 'Bonjour' using french_to_english
    def test_french_to_english_translation_bonjour(self):
        french_text = "Bonjour"
        result = french_to_english(french_text)
        self.assertEqual(result, "Hello")
        print("french_to_english -  assertEqual Successful")

class TranslatorE2FTestCase(unittest.TestCase):
 
    # Test for null input in english_to_french
    def test_null_input_english_to_french(self):
        result = english_to_french(None)
        self.assertNotEqual(result, "Bonjour")
        print("english_to_french -  assertNotEqual Successful")

    # Test translation of the word 'Hello' using english_to_french
    def test_english_to_french_translation_hello(self):
        english_text = "Hello"
        result = english_to_french(english_text)
        self.assertEqual(result, "Bonjour")
        print(".english_to_french -  assertEqual Successful")


if __name__ == '__main__':
    unittest.main()
