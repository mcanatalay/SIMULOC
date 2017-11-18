import numpy

class Generator:
    """
    Generator class of Signal Module
    """

    def __init__(self):
        pass

    def noise(self, level=0.1):
        """Generates a noise

        Args:
            level: % level of noise.

        Returns:
            Returns noise.
        """
    
        return level * numpy.random.normal(0.5, 1)
