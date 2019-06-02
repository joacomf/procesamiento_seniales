import math
import numpy

from herramientas.signals.CosSignal import CosSignal

# Utilizando la función del punto anterior, generar las rectas y1 = 2x +1 y y2 = −x. Dibujarlas en la misma gráfica con líneas gruesas de distintos colores y agregar etiquetas que indiquen a que ecuación corresponde cada recta. Marcar el punto de intersección.

time_collection = numpy.linspace(0, 10 * math.pi, 20).tolist()
signal = CosSignal(frecuency=20, amplitude=1)
signal.graph(time_collection)
