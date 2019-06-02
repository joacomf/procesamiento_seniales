from herramientas.signals.StepSignal import StepSignal
# Implementar una función que construya la señal escalón u[t] con 5 segundos de duración y una frecuencia de muestreo f s = 5, y la grafique en el intervalo (−2,5; 2,5).
signal = StepSignal(frecuency=5, duration=5)
signal.graph(-2.5, 2.5)