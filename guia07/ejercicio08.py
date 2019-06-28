from scipy.fftpack import fft, fftshift, fftfreq
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


def window_in_db(fft):

    fft_norm = abs(fft) / max(abs(fft))

    return 20 * numpy.log10(fft_norm)


t = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 50)
t2 = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 10000)


box = box_window(len(t), 0, 30)
box_ft = fft(box, 10000)
box_phase = numpy.angle(box_ft)
box_dbs = window_in_db(box_ft)

triangle = triangle_window(len(t), 0, 30)
triangle_ft = fft(triangle, 10000)
triangle_phase = numpy.angle(triangle_ft)
triangle_dbs = window_in_db(triangle_ft)

hamming = hamming_window(len(t), 0, 30)
hamming_ft = fft(hamming, 10000)
hamming_phase = numpy.angle(hamming_ft)
hamming_dbs = window_in_db(hamming_ft)


_, subplot = plot.subplots(3, 4)

subplot[0][0].stem(t, box)
subplot[0][0].title.set_text("Ventana Rectangular")

subplot[0][1].plot(t2, window_tft_centered(abs(box_ft)))
subplot[0][1].title.set_text("Transformada Ventana Rectangular")

subplot[0][2].plot(t2, window_tft_centered(box_dbs))
subplot[0][2].title.set_text("Transformada Ventana Rectangular dBs")

subplot[0][3].plot(t2, window_tft_centered(abs(box_phase)))
subplot[0][3].title.set_text("Fase Ventana Rectangular")

subplot[1][0].stem(t, triangle)
subplot[1][0].title.set_text("Ventana Triangular")

subplot[1][1].plot(t2, window_tft_centered(abs(triangle_ft)))
subplot[1][1].title.set_text("Transformada Ventana Triangular")

subplot[1][2].plot(t2, window_tft_centered(triangle_dbs))
subplot[1][2].title.set_text("Transformada Ventana Triangular dBs")

subplot[1][3].plot(t2, window_tft_centered(abs(triangle_phase)))
subplot[1][3].title.set_text("Fase ventana Triangular")

subplot[2][0].stem(t, hamming)
subplot[2][0].title.set_text("Ventana Hamming")

subplot[2][1].plot(t2, window_tft_centered(abs(hamming_ft)))
subplot[2][1].title.set_text("Transformada Ventana Hamming")

subplot[2][2].plot(t2, window_tft_centered(hamming_dbs))
subplot[2][2].title.set_text("Transformada Ventana Triangular dBs")

subplot[2][3].plot(t2, window_tft_centered(abs(hamming_phase)))
subplot[2][3].title.set_text("Fase Ventana Hamming")

plot.show()
