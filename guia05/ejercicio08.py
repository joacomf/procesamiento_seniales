import matplotlib.pyplot as plot
import numpy

from herramientas.transforms.FourierTransform import FourierTransform
from herramientas.transforms.FourierUtils import FourierUtils
from herramientas.signals.SquareSignalGenerator import SquareSignalGenerator

init, to = (0, 50)
fs = 600
time = numpy.linspace(init, to, fs).tolist()

generator = SquareSignalGenerator(9, init=init, to=to, fs=fs)
signal = generator.generate()

fourier = FourierTransform(signal=generator, time=time)
ft = fourier.calculate()

utils = FourierUtils(signal_values=signal, transform_values=ft)
parserval = utils.parseval_relationship_maintains()
print("Se cumple relación de Parserval: " + str(parserval))

_, subplot = plot.subplots(2, 1)

subplot[0].plot(time, signal)
subplot[0].set_xlabel('Tiempo')
subplot[0].set_ylabel('Amplitud')
subplot[0].grid()
subplot[0].title.set_text("Señal cuadrada generada por suma de armónicos")

subplot[1].plot(time, ft, 'r')
subplot[1].set_xlabel('|X(w)|')
subplot[1].set_ylabel('Frecuencia (Hz)')
subplot[1].grid()
subplot[1].title.set_text("Transformada del señal cuadrada")

plot.tight_layout()
plot.show()
