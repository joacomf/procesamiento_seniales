class EvenPart:
	def __init__(self, signal):
		self.signal = signal
		self.values = []

	def generate_function(self, time_collection):
		self.values = []

		for time in time_collection:
			self.values.append(self.value_at(time));

		return self.values

	def value_at(self, time):
		return 0.5 * (self.signal.value_at(time) + self.signal.value_at(-time))