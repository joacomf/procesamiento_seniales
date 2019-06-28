import numpy


class FourierUtils:

    def __init__(self, signal=None, signal_values=[], transform_values=[]):
        self.signal = signal
        self.transform_values = transform_values
        self.signal_values = signal_values

    def parseval_relationship_maintains(self):

        signal_enery = numpy.sum(abs(numpy.array(self.signal_values))**2)
        transform_enery = numpy.sum(abs(numpy.array(self.transform_values)) ** 2)

        # Al ser discreto no necesito el factor de ajuste 2PI, solo necesito dividir por el total de muestras
        transform_enery = transform_enery / len(self.transform_values)

        # Corroboro que la energía de ambas señales sean muy cercana(para evitar error númerico computacional con el ==)
        return numpy.allclose(signal_enery, transform_enery)