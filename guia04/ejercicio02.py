import matplotlib.pyplot as plot

from herramientas.signals.SquareSignalGenerator import SquareSignalGenerator

_, subplots = plot.subplots(nrows=5, ncols=2)

for i in range(1, 6):
    subplot_number = i - 1

    generator = SquareSignalGenerator(i, 101)
    time = generator.time
    signal = generator.generate()
    error = generator.error()

    subplots[subplot_number][0].plot(time, signal)
    subplots[subplot_number][1].plot(time, error[1])

plot.show()



