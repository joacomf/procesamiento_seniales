import matplotlib.pyplot as plot
import numpy

from herramientas.signals.Signal import Signal


class Function(Signal):

	def __init__(self, m=0, b=0, frecuency=0, samples_amount=0, values=[], duration=0):
		Signal.__init__(self, frecuency=0, samples_amount=0, values=[], duration=0)
		self.m = m
		self.b = b
		self.values = []

	def function(self, time_collection):
		self.values = []

		for x in time_collection:
			self.values.append(self.value_at(x))

		return self.values

	def value_at(self, time):
		return self.m * time + self.b

	def graph(self, time_collection):
		function = self.function(time_collection)
		plot.plot(time_collection, function)
		plot.show()

	def intersect(self, signal, time_collection):
		me = self.values
		you = signal.values

		plot.plot(time_collection, me)
		plot.plot(time_collection, you)

		idx = numpy.argwhere(numpy.diff(numpy.sign(numpy.array(me) - numpy.array(you)))).flatten()
		plot.plot(time_collection[idx[0]], you[idx[0]], 'ro')

		plot.show()