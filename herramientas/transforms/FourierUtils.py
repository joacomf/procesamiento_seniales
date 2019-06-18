import numpy


class FourierUtils:

    def __init__(self, signal=None, signal_values=[], transform_values=[]):
        self.signal = signal
        self.transform_values = transform_values
        self.signal_values = signal_values

    def get_phase(self):
        imaginary = numpy.imag(self.signal_values)
        real = numpy.real(self.signal_values)

        phase = numpy.arctan2(imaginary, real)

        return phase

    def parseval_relationship_maintains(self):

        signal_enery = numpy.sum(abs(numpy.array(self.signal_values))**2)
        transform_enery = numpy.sum(abs(numpy.array(self.transform_values)) ** 2)

        transform_enery = transform_enery / len(self.transform_values)

        return numpy.allclose(signal_enery, transform_enery)

    def module_pow(self, value):
        return pow(abs(self.signal.value_at(value)), 2)
