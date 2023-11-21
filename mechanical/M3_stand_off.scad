// M3 Stand Off
OUTER_DIAMETER = 6;
INNER_DIAMETER = 3.7;
HEIGHT = 8;
OFFSET=2;
RESOLUTION=100;

difference()
{
    cylinder(h=HEIGHT, d=OUTER_DIAMETER, center=true, $fn=RESOLUTION);
    cylinder(h=HEIGHT+OFFSET, d=INNER_DIAMETER, center=true, $fn=RESOLUTION);
}