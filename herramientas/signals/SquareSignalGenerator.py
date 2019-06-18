import matplotlib.pyplot as plot
import numpy

from herramientas.signals.SinSignal import SinSignal
from herramientas.signals.StepSignal import StepSignal
from herramientas.DisplacementFunction import DisplacementFunction
from herramientas.ReflexFunction import ReflexFunction


class SquareSignalGenerator:

    def __init__(self, n=0, init=0, to=1, fs=101):
        self.values = []
        self.summatory = []
        self.n = n
        self.fs = fs
        self.time = numpy.linspace(init, to, fs, endpoint=False).tolist()

    def generate(self):
        summatory = numpy.zeros(self.fs)

        armonicas = (2 ** self.n) + 1
        for k in range(1, armonicas, 2):
            armonico_base = SinSignal(amplitude=(4 / (k * numpy.pi)), frecuency=k)
            armonico_base.generate_function(self.time)

            result = armonico_base.get_values()
            summatory += result

        self.summatory = summatory
        self.values = summatory

        return summatory

    def graph(self):
        plot.plot(self.time, self.summatory)
        plot.show()

    def error(self):
        square = StepSignal(101, 1)

        function = DisplacementFunction(ReflexFunction(square), 0.5)
        square_values = numpy.array(function.generate_function(self.time))

        square_inverse = numpy.array(DisplacementFunction(square, 0.5).generate_function(self.time)) * -1

        return [square_values, abs((numpy.array(self.summatory)) - (square_values + square_inverse))]
