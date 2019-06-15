import numpy
import matplotlib.pyplot as plot

from herramientas.signals.Signal import Signal
from herramientas.ReflexFunction import ReflexFunction
from herramientas.DisplacementFunction import DisplacementFunction
from herramientas.ScaleFunction import ScaleFunction


class CosFrom0ToPI(Signal):

    def value_at(self, time):
        value_at_point = 0

        if 0 <= time < numpy.pi:
            value_at_point = (2 * numpy.cos(time))

        return value_at_point


time_collection = numpy.linspace(-10 * numpy.pi, 10 * numpy.pi, 100).tolist()

signal = CosFrom0ToPI()

signal_t = ReflexFunction(signal)
signal_t_plus_pi = DisplacementFunction(signal, 2 * numpy.pi)
signal_t_minus_pi = DisplacementFunction(signal, -2 * numpy.pi)
signal_minus_t_plus_pi = ReflexFunction(DisplacementFunction(signal, - numpy.pi))
signal_times_4 = ScaleFunction(signal, 4)
signal_quarter = ScaleFunction(signal, 0.25)
signal_half_reflected = ReflexFunction(ScaleFunction(signal, 0.5))

_, subplot = plot.subplots(nrows=7, ncols=1)

subplot[0].plot(time_collection, signal_t.generate_function(time_collection))
subplot[1].plot(time_collection, signal_t_plus_pi.generate_function(time_collection))
subplot[2].plot(time_collection, signal_t_minus_pi.generate_function(time_collection))
subplot[3].plot(time_collection, signal_minus_t_plus_pi.generate_function(time_collection))
subplot[4].plot(time_collection, signal_times_4.generate_function(time_collection))
subplot[5].plot(time_collection, signal_quarter.generate_function(time_collection))
subplot[6].plot(time_collection, signal_half_reflected.generate_function(time_collection))

plot.show()
