import matplotlib.pyplot as plot
import numpy

from herramientas.signals.StepSignal import StepSignal
from herramientas.DisplacementFunction import DisplacementFunction

signal = StepSignal()
reflejado = DisplacementFunction(signal, 2);

time_collection = numpy.linspace(-5, 5, 100).tolist()

plot.plot(time_collection, reflejado.generate_function(time_collection))
plot.show()
