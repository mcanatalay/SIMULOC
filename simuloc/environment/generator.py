import numpy

class Generator:
    """
    Generator class of Environment Module
    """

    def __init__(self):
        pass

    @staticmethod
    def pathLossExponent(distance, frequency):
        """Generates Path Loss Exponent

        Args:
            distance: Distance between two nodes.
            frequency: Frequency of transmission.

        Returns:
            Returns pathLoss (dB).
        """

        return numpy.square((4 * numpy.pi * distance * frequency) / (299792458))

    @staticmethod
    def environmentConstant(standard_deviation):
        """Generates Environment Constant

        Args:
            standard_deviation: 0 to 10 (db)

        Returns:
            Returns environment constant.
        """

        standard_deviation = standard_deviation if (standard_deviation >= 0 and standard_deviation <= 10)  else 5
        return numpy.random.normal(0,standard_deviation)