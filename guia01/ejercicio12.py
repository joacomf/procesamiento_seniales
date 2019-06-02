import numpy
import matplotlib.pyplot as plot

from herramientas.signals.CosSignal import CosSignal
from herramientas.ScaleFunction import ScaleFunction

signal = CosSignal(frecuency=30, amplitude=1)
reflejado = ScaleFunction(signal, 5)

time_collection = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 100).tolist()

plot.plot(time_collection, reflejado.generate_function(time_collection))
plot.show()
