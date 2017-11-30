import unittest
from simuloc.environment import EnvironmentGenerator

class EnvironmentGeneratorTestCase(unittest.TestCase):
    """GeneratorTestCase tests the generator class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pathLossExponent(self):
        """Tests the boundry of pathLossExponent generator."""
        self.assertTrue(EnvironmentGenerator.pathLossExponent(38.71,914*1000) < 5)

    def test_environmentConstant(self):
        """Tests the boundry of environmentConstant generator."""
        self.assertTrue(EnvironmentGenerator.environmentConstant(8.7) < 20)

if __name__ == '__main__':
    unittest.main()
