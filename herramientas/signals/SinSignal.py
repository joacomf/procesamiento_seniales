import matplotlib.pyplot as plot
import numpy

from herramientas.signals.Signal import Signal


class SinSignal(Signal):

	def __init__(self, frecuency=0, samples_amount=5, values=[], duration=1, amplitude=0, phase=0):
		Signal.__init__(self, frecuency, samples_amount, values, duration) 
		self.phase = phase
		self.amplitude = amplitude

	def value_at(self, time):
		x = time
		w = 2 * numpy.pi * self.frecuency
		value_at_point = self.amplitude * numpy.sin(x * w + self.phase)
		return value_at_point

	def graph(self, time_collection):
		self.generate_function(time_collection)

		plot.plot(time_collection, self.values)
		plot.show()

	def graph_limit(self, init, to):
		time_collection = numpy.linspace(init, to, self.amount_sample()).tolist()

		self.generate_function(time_collection)

		plot.plot(time_collection, self.values)
		plot.show()

	def graph_only(self, time_collection):
		plot.plot(time_collection, self.values)
		plot.show()
