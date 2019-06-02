
class DisplacementFunction:

	def __init__(self, signal, value):
		self.signal = signal
		self.value = value
		self.values = []

	def generate_function(self, time_collection):
		self.values = []

		for time in time_collection:
			self.values.append(self.value_at(time));

		return self.values

	def value_at(self, time):
		return self.signal.value_at(time - self.value)