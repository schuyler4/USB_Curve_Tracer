<h2> USB Curve Tracer Test Method </h2>
<h3> Sweep Test </h3>
The curve tracer is tested by sweeping a number of different resistor values.
Once all this data is collected, a best fit line for each tested resistor value
is found. The percent error between the theoretical resistor IV curve, and the measured resistor value IV curve is found.

The following resistor values are tested:  680, 470, 330, 220, 33

This test is not automated with the curve tracer in loop. Each resistor is manually measured,
and the data is saved in the test directory. 

<b>acceptance criteria:</b>
The error between the theoretical resistor curve slope, and the measured
resistor curve slope is less than 15%. 
The offset must be less than 0.005 for the measured curve. 
(remember, the curve tracer is only to get a rough idea of the device curve)



