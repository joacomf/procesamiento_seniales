import matplotlib.pyplot as plot
import numpy
import math

from herramientas.Function import Function
from herramientas.ReflexFunction import ReflexFunction

signal = Function(m=2, b=3)
reflejado = ReflexFunction(signal)

time_collection = numpy.linspace(-100 * math.pi, 100 * math.pi, 100).tolist()

plot.plot(time_collection, reflejado.generate_function(time_collection))
plot.show()
