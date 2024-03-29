# Ejercicio 6 y 7

import matplotlib.pyplot as plot
import numpy
from scipy.fftpack import fft, ifft

t = numpy.linspace(0, 10, 1000)
portadora = numpy.cos(10 * numpy.pi * t)


def modulate(incoming_signal):
    modulacion = portadora * incoming_signal

    return modulacion


def demodulate(incoming_signal):
    signal = fft(incoming_signal * portadora)

    # box = fft(2 * numpy.sinc(2 * numpy.pi * t))
    box = box_window(len(incoming_signal), 0, 60, 2) + box_window(len(incoming_signal), len(incoming_signal)-40, len(incoming_signal), 2)
    demodulated = ifft(box * signal)

    return demodulated


def box_window(total, init, to, multiplier=1):
    box = numpy.zeros(total)

    box[init:to] = box[init:to] + multiplier

    return box


message = numpy.cos(2 * numpy.pi * t)

modulated_signal = modulate(message)
demodulated_signal = demodulate(modulated_signal)

_, subplot = plot.subplots(4, 1)

subplot[0].plot(t, portadora)
subplot[0].title.set_text("Señal portadora")

subplot[1].plot(t, message)
subplot[1].title.set_text("Señal moduladora")

subplot[2].plot(t, modulated_signal)
subplot[2].title.set_text("Señal modulada")

subplot[3].plot(t, demodulated_signal)
subplot[3].title.set_text("Señal demodulada")

subplot[0].grid()
subplot[1].grid()
subplot[2].grid()
subplot[3].grid()

plot.tight_layout()
plot.show()

