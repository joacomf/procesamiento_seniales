import matplotlib.pyplot as plot
import numpy


class Signal:

	def __init__(self, frecuency=0, samples_amount=0, values=None, duration=0):
		if values is None:
			values = []
		self.frecuency = frecuency
		self.samples_amount = samples_amount
		self.values = values
		self.duration = duration
		self.time_collection = []

	def duration(self):
		return self.samples_amount / self.frecuency

	def amount_sample(self):
		return self.frecuency * self.duration

	def mean(self):
		return numpy.mean(self.values)

	def graph(self, initial=0, to=0):
		function = self.function(initial, to)
		plot.plot(self.time_collection, function)
		plot.show()

	def generate_function(self, time_collection):
		self.values = []

		for time in time_collection:
			self.values.append(self.value_at(time))

		return self.values

	def total_energy(self, time_collection):
		total_energy = 0
		for (idx,value) in enumerate(self.values):
			if idx != len(self.values) - 1:
				energy_at = value**2 * abs(time_collection[idx + 1] - time_collection[idx])
				total_energy += energy_at

		return total_energy

	def value_at(self, time):
		pass

	def function(self, initial, to):
		return None
