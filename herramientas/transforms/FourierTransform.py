import numpy


class FourierTransform:
    def __init__(self, signal=None, time=[], signal_values=[]):
        self.signal = signal
        self.time = time
        self.signal_values = signal_values
        self.values = []

    def calculate(self):
        values = numpy.array(self.signal.values)

        if self.signal is None:
            values = self.signal_values

        self.values = numpy.fft.fft(values)

        return self.values

