from herramientas.Function import Function
import numpy
# Utilizando la función del punto anterior, generar las rectas y1 = 2x +1 y y2 = −x. Dibujarlas en la misma gráfica con líneas gruesas de distintos colores y agregar etiquetas que indiquen a que ecuación corresponde cada recta. Marcar el punto de intersección.
time_collection = numpy.linspace(-1, 1, 5*5).tolist()

signal_A = Function(m=2, b=1)
function_A = signal_A.function(time_collection)
signal_B = Function(m=-1, b=0)
function_B = signal_B.function(time_collection)

signal_A.intersect(signal_B, time_collection)