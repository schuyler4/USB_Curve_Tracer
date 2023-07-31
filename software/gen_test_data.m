% Genertate a bunch of points from the diode model

VT = 25.852E-3; % mV
IS = 25E-16;
n = 1.9;
SAMPLE_COUNT = 500

forward_voltages = linspace(0, 1.7, SAMPLE_COUNT);

forward_currents = IS*(exp(forward_voltages/(n*VT)) - 1);

figure
plot(forward_voltages, forward_currents)
title("Diode IV Plot");
xlabel("Forward Voltage (V)");
ylabel("Forward Current (A)");
set(gca, 'YScale', 'log');
grid on

current_voltage = zeros(SAMPLE_COUNT, 2);

for i = 1:SAMPLE_COUNT
  current_voltage(i, 1) = forward_voltages(i);
  current_voltage(i, 2) = forward_currents(i);
end

writematrix(current_voltage)
type("points.txt")
