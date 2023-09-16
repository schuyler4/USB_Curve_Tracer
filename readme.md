<h2> USB Curve Tracer </h2>
This is my attempt at making a curve tracer. Precision parts are not used so this obviously effects the performance. 
Instead of implementing a display, data is piped to a PC where it is plotted using Python. 

<h3> Limitations </h3>
- The curve tracer does not use sinusoidal waveforms for measurement; measuring reactive components 
(Capacitors and Inductors) probably will not work. 
- The curve tracer cannot be driven, so it cannot measure voltage sources.
- The curve tracer does not include Kelvin connection functionality, so test lead resistance and 
contact resistance will be included in the measurement.  

<h3> Specs </h3>
- 12V External Power Supply

<h3> Examples </h3>
Here are a few preliminary curves.

![Resistor Plot](./resistor_plot.png)
![Zener Diode Plot](./zener_diode_plot.png)