from herramientas.Function import Function
import numpy

time_collection = numpy.linspace(-1, 1, 5*5).tolist()

signal = Function(m=2, b=3, frecuency=5, duration=5)
signal.graph(time_collection)