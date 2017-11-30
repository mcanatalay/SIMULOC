import unittest
from simuloc.signal import SignalGenerator

class SignalGeneratorTestCase(unittest.TestCase):
    """GeneratorTestCase tests the generator class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_noise(self):
        """Tests the boundry of noise generator."""
        self.assertTrue(SignalGenerator.noise(0.1) < 4)

    def test_signal(self):
        """Tests the boundry of signal generator."""
        signal = SignalGenerator.signal(38.71, 2.2, 11.3)
        self.assertTrue(signal < 0 and signal > -100)

if __name__ == '__main__':
    unittest.main()
