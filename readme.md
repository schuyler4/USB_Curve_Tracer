<h2> USB Curve Tracer </h2>
This is my attempt at making a curve tracer.  
Instead of implementing a display, data is piped to a PC where it is plotted using Python. It also controlled using
a command line interface on the PC. 

![Device Picture](./device_picture.JPG)

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
<li>Precision parts are not used so this obviously effects the performance.</li>
</ul> 

<h3> Examples </h3>
<p>Here are a few diode curves. </p>

![Zener Diode Plot](./zener_diode_plot.png)
![1N4001 Diode](./1N4001.png)
There was a power buffering blip with the 1N4001 diode. 

<h3> Test Curves </h3>
<p>Here are the test curves with the theoretical
curve overlaid.</p>

![33 Test Curve](./test/test_plot/33.png)
![220 Test Curve](./test/test_plot/220.png)
![330 Test Curve](./test/test_plot/330.png)
![470 Test Curve](./test/test_plot/470.png)
![680 Test Curve](./test/test_plot/680.png)
