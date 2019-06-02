import matplotlib.pyplot as plot
import numpy

from herramientas.signals.Signal import Signal
from herramientas.OddPart import OddPart
from herramientas.EvenPart import EvenPart
import random


class RandomFunction(Signal):

	def value_at(self, time):
		return random.randint(-2, 2)


time_collection = numpy.linspace(-10, 10).tolist()

signal = RandomFunction()
odd = OddPart(signal)
even = EvenPart(signal)

plot.stem(time_collection, odd.generate_function(time_collection))
plot.stem(time_collection, even.generate_function(time_collection), "-ro")

plot.show()
