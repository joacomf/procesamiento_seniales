# Ejercicio 6 y 7

import matplotlib.pyplot as plot
import numpy

t = numpy.linspace(0, 10, 1000)
portadora = numpy.cos(2 * numpy.pi * t)


def modulate(incoming_signal):
    modulacion = portadora * incoming_signal

    return modulacion


def demodulate(incoming_signal):
    signal = numpy.fft.fft((incoming_signal * portadora))
    ventaneo = box_window(len(signal), 50, 90, 1) * signal + box_window(len(signal), len(signal) - 90, len(signal) - 60, 1) * signal
    demodulated = numpy.fft.ifft(ventaneo * signal)

    return [demodulated, signal]


def box_window(total, init, to, multiplier=1):
    box = numpy.zeros(total)

    box[init:to] = box[init:to] + multiplier

    return box


print(box_window(50, 10, 15))

message = numpy.sin(20 * numpy.pi * t)

modulated_signal = modulate(message)
demodulated_signal = demodulate(modulated_signal)

_, subplot = plot.subplots(5, 1)

subplot[0].plot(t, portadora)
subplot[0].title.set_text("Señal portadora")

subplot[1].plot(t, message)
subplot[1].title.set_text("Señal moduladora")

subplot[2].plot(t, modulated_signal)
subplot[2].title.set_text("Señal modulada")

subplot[3].plot(t, demodulated_signal[0])
subplot[3].title.set_text("Señal demodulada")
subplot[4].plot(t, demodulated_signal[1])
subplot[4].title.set_text("Señal demodulada")

subplot[0].grid()
subplot[1].grid()
subplot[2].grid()
subplot[3].grid()

plot.tight_layout()
plot.show()

