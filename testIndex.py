import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        first_name = "test"
        self.assertEqual(first_name.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_split(self):
        s = 'John Smith'
        self.assertEqual(s.split(), ['John', 'Smith'])
        # Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)




if __name__ == '__main__':
    unittest.main()