from herramientas.signals.CosSignal import CosSignal
import math

signal_2 = CosSignal(frecuency=100, amplitude=1)
signal_2.graph_limit(-2 * math.pi, 2 * math.pi)
