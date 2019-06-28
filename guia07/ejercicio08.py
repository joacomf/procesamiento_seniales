from scipy.fftpack import fft
import numpy
import matplotlib.pyplot as plot


def box_window(total, init, to, multiplier=1):
    box = numpy.zeros(total)

    box[init:to] = box[init:to] + multiplier

    return box


def triangle_window(total, init, to):
    delta = init + to
    N = delta / 2
    L = (delta + 1) / 2

    window = numpy.zeros(total)

    for i in range(init, to):
        window[i] = 1 - abs((i - N)/L)

    return window


def hamming_window(total, init, to):
    M = init + to

    window = numpy.zeros(total)

    for i in range(init, to):
        window[i] = 0.54 - 0.46 * numpy.cos((2 * numpy.pi * i) / (M - 1))

    return window


def window_tft_centered(tft):
    center = int(len(tft) / 2)

    tft_list = tft.tolist()

    return tft_list[center:] + tft_list[:center]


t = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 50)
t2 = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 1000)
box = box_window(len(t), 0, 30)
box_ft = fft(box, 1000)

triangle = triangle_window(len(t), 0, 30)
triangle_ft = fft(triangle, 1000)

hamming = hamming_window(len(t), 0, 30)
hamming_ft = fft(hamming, 1000)

_, subplot = plot.subplots(3, 3)

subplot[0][0].stem(t, box)
subplot[0][0].title.set_text("Ventana Rectangular")

subplot[0][1].plot(t2, window_tft_centered(abs(box_ft)))
subplot[0][1].title.set_text("Transformada ventana rectangular")

subplot[1][0].stem(t, triangle)
subplot[1][0].title.set_text("Ventana Triangular")

subplot[1][1].plot(t2, window_tft_centered(abs(triangle_ft)))
subplot[1][1].title.set_text("Transformada Ventana Triangular")

subplot[2][0].stem(t, hamming)
subplot[2][0].title.set_text("Ventana Hamming")

subplot[2][1].plot(t2, window_tft_centered(abs(hamming_ft)))
subplot[2][1].title.set_text("Transformada Ventana Hamming")

plot.tight_layout()
plot.show()
