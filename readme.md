<h2> USB Curve Tracer </h2>
This is my attempt at making a curve tracer.  
Instead of implementing a display, data is piped to a PC where it is plotted using Python. It also controlled using
a command line interface on the PC. 

![Device Picture](./device_picture_REV2.JPG)

<h3> Specs </h3>
<ul>
<li>12V External Power Supply</li>
<li>Maximum Positive Sweep Voltage: 3.4</li>
<li>Minimum Negative Sweep Voltage: -4.6V</li>
<li>Full Sweep Time: 15s</li>
</ul>

<h3> Limitations </h3>
<ul>
<li>The curve tracer does not use sinusoidal waveforms for measurement; measuring reactive components 
(Capacitors and Inductors) probably will not work. </li>
<li>The curve tracer cannot be driven, so it cannot measure voltage sources.</li>
<li>The curve tracer does not include Kelvin connection functionality, so test lead resistance and 
contact resistance will be included in the measurement. </li>
</ul> 

<h3> Examples </h3>
<p>Here are a few diode curves taken with the revision 2 device. </p>

![Zener Diode Plot](./zener_diode_plot_REV2.png)
![1N4001 Diode](./1N4001_REV2.png)

<p>
Here is a Darlington Transistor sweep taken with revision 3 of the device. 
I'm not sure if it's right or not. 

![TIP122G Plot](./TIP122G_REV3_LM324.png)
</p>