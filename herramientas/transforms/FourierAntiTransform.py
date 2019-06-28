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

        samples = len(values)

        # Divido por la cantidad de muestras para ajustar, ya que tengo un espectro discreto
        # Invierto los valores para que x(-t) quede x(t) y se cumpla la propiedad de la dualidad
        self.values = numpy.array((numpy.fft.fft(values / samples)).tolist()[::-1])

        return self.values

