import math
import matplotlib.pyplot as plot
import numpy

from herramientas.signals.CosSignal import CosSignal

time_collection = numpy.linspace(-100 * math.pi, 100 * math.pi, 20).tolist()
signal = CosSignal(frecuency=10, amplitude=1)
signal_function = signal.generate_function(time_collection)
signal_2 = CosSignal(frecuency=20, amplitude=1)
signal_2_function = signal_2.generate_function(time_collection)
signal_3 = CosSignal(frecuency=50, amplitude=1)
signal_3_function = signal_3.generate_function(time_collection)
signal_4 = CosSignal(frecuency=100, amplitude=1)
signal_4_function = signal_4.generate_function(time_collection)


plot.plot(time_collection, signal_function)
plot.plot(time_collection, signal_2_function)
plot.plot(time_collection, signal_3_function)
plot.plot(time_collection, signal_4_function)

plot.show()