import numpy


class FourierAntiTransform:
    def __init__(self, signal=None, time=[], signal_values=[]):
        self.signal = signal
        self.time = time
        self.signal_values = signal_values
        self.values = []

    def calculate(self):
        values = self.signal_values

        if len(self.signal_values) == 0:
            values = numpy.array(self.signal.values)

        result = []
        samples = len(values)

        for sample in range(samples):
            partial = 0

            for k in range(samples):
                partial += values[k] * numpy.exp(2j * numpy.pi * k * sample * (1/samples))

            partial /= samples
            result.append(partial)

        self.values = numpy.array(result)
        # self.values = (numpy.fft.fft((-1 * values)/(2 * numpy.pi * samples)))

        return self.values

