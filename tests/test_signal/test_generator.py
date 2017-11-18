import unittest
from simuloc.signal import Generator

class GeneratorTestCase(unittest.TestCase):
    """GeneratorTestCase tests the generator class."""

    def setUp(self):
        """Creates a instance of the generator class."""
        self.cinst = Generator()

    def tearDown(self):
        pass

    def test_noise(self):
        """Tests the boundry of noise generator."""
        self.assertTrue(self.cinst.noise(0.1) < 4)

if __name__ == '__main__':
    unittest.main()
