import math

from herramientas.signals.SinSignal import SinSignal


class CosSignal(SinSignal):

	def __init__(self, frecuency=0, samples_amount=5, values=None, duration=1, amplitude=0, phase=0):
		if values is None:
			values = []
		phase = phase + (math.pi / 2)
		SinSignal.__init__(self, frecuency, samples_amount, values, duration, amplitude, phase)