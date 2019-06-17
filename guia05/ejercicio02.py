import matplotlib.pyplot as plot
import numpy

from herramientas.signals.SinSignal import SinSignal
from herramientas.transforms.FourierTransform import FourierTransform
from herramientas.transforms.FourierAntiTransform import FourierAntiTransform


time = numpy.linspace(-50,  50, 600).tolist()

sin = SinSignal(amplitude=2, frecuency=1/(2*numpy.pi))
sin.generate_function(time)

fourier = FourierTransform(sin, time)
ft = fourier.calculate()

antifourier = FourierAntiTransform(signal_values=ft)
aft = antifourier.calculate()

_, subplot = plot.subplots(3, 1)

subplot[0].plot(time, sin.values)
subplot[0].set_xlabel('Tiempo')
subplot[0].set_ylabel('Amplitud')

subplot[1].plot(time, ft, 'r')
subplot[1].set_xlabel('|X(w)|')
subplot[1].set_ylabel('Frecuencia (Hz)')

subplot[2].plot(time, aft)
subplot[2].set_xlabel('Tiempo')
subplot[2].set_ylabel('Amplitud')

plot.show()
