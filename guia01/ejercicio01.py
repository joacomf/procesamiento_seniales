import math

import numpy

from herramientas.signals.CosSignal import CosSignal

time_collection = numpy.linspace(-100 * math.pi, 100 * math.pi, 100).tolist()
print(time_collection)
signal = CosSignal(frecuency=100, amplitude=1)
signal.generate_function(time_collection)

print(signal.total_energy(time_collection))