import numpy

class Generator:
    """
    Generator class of Signal Module
    """

    def __init__(self):
        pass

    @staticmethod
    def signal(distance, path_loss_exponent, environment_constant):
        """Generates signal

        Args:
            distance: distance in meters between two nodes.
            path_loss_exponent: Path Loss Exponent of the environment (0-5).
            environment_constant: Environment Constant (zero-mean Gaussian random variable with standard deviation – σ).

        Returns:
            Returns noise.
        """
        path_loss_exponent = path_loss_exponent if (path_loss_exponent >= 0 and path_loss_exponent <= 5)  else 2.5
        return -10 * path_loss_exponent * numpy.log10(distance) - environment_constant
    
    @staticmethod
    def noise(level=0.1):
        """Generates a noise

        Args:
            level: % level of noise.

        Returns:
            Returns noise.
        """
    
        return level * numpy.random.normal(0.5, 1)
