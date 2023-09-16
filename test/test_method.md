<h2> USB Curve Tracer Test Method </h2>
The curve tracer is tested by sweeping a number of different resistor values.
Once all this data is collected, a best fit line for each tested resistor value
is found. The percent error between the theoretical resistor IV curve, and the measured
resistor value IV curve is found.

This method verifies the curve tracers correct operation at all the test resistances.
Even if the resistance happens to be the static resistance when sweeping a semiconductor
device. 

acceptance criteria: 
-The error between the theoretical resistor curve slope, and the measured
resistor curve slope is less than 15%. 
-The offset must be less than 0.001 for the measured curve. 

(remember, the curve tracer is only to get a rough idea of the device curve)

This test is not automated with the curve tracer in loop. Each resistor is manually measured,
and the data is saved in the test directory. 

The following resistor values are tested: 470, 330, 220