<h2> USB Curve Tracer </h2>
This is my attempt at making a curve tracer.  
Instead of implementing a display, data is piped to a PC where it is plotted using Python. 

<h3> Limitations </h3>
<ul>
<li>The curve tracer does not use sinusoidal waveforms for measurement; measuring reactive components 
(Capacitors and Inductors) probably will not work. </li>
<li>The curve tracer cannot be driven, so it cannot measure voltage sources.</li>
<li>The curve tracer does not include Kelvin connection functionality, so test lead resistance and 
contact resistance will be included in the measurement. </li>
<li>Precision parts are not used so this obviously effects the performance.</li>
</ul> 

<h3> Specs </h3>
<ul>
<li>12V External Power Supply</li>
</ul>

<h3> Examples </h3>
Here are a few preliminary curves.

![Resistor Plot](./resistor_plot.png)
![Zener Diode Plot](./zener_diode_plot.png)