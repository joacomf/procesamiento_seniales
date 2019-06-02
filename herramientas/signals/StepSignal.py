import matplotlib.pyplot as plot
import numpy

from herramientas.signals.Signal import Signal


class StepSignal(Signal):

	def __init__(self, frecuency=0, duration=0):
		Signal.__init__(self, frecuency=frecuency, duration=duration)
		self.time_collection = []

	def function(self, initial=0, to=0):
		values = []
		self.time_collection = numpy.linspace(initial, to, self.amount_sample()).tolist()

		for time in self.time_collection:
			values.append(self.value_at(time))

		return values

	@staticmethod
	def value_at(time):
		return 1 if (time > 0) else 0

	def graph(self, initial=0, to=0):
		function = self.function(initial, to)
		plot.step(self.time_collection, function)
		plot.show()