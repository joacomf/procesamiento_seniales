import matplotlib.pyplot as plot
import numpy

t = numpy.linspace(0, 10, 1000)
portadora = numpy.cos(2 * numpy.pi * t)


def modulate(time, incoming_signal):
    modulacion = portadora * incoming_signal

    return modulacion


def demodulate(time, incoming_signal):
    demodulated = incoming_signal / portadora

    return demodulated


def lin(t):
    y = t * 2 - 4

    return y


message = numpy.sin(20 * numpy.pi * t)

modulated_signal = modulate(t, message)
demodulated_signal = demodulate(t, modulated_signal)

_, subplot = plot.subplots(4, 1)

subplot[0].plot(t, portadora)
subplot[1].plot(t, message)
subplot[2].plot(t, modulated_signal)
subplot[3].plot(t, demodulated_signal)
plot.show()

