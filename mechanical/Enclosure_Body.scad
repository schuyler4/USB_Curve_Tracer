module BasicBox()
{
    circuit_board_width = 117;
    wall_thickness = 6;
    height = 60;
    
    difference()
    {
        cube(size=[circuit_board_width + wall_thickness, 
                   circuit_board_width + wall_thickness, 
                   height + wall_thickness], center=true);
        
        translate([0, 0, wall_thickness])
        cube(
        size=[circuit_board_width, 
              circuit_board_width, 
              height], center=true);
    }
}

module MountingStandOff()
{
    stand_off_radius = 4;
    stand_off_height = 5;
    curve_resolution = 1000;
    m3_through_hole_diameter = 3.4;
    clearance=1;
    wall_thickness=4;
    
    difference()
    {
        cylinder(h = stand_off_height, 
                 d = 2*stand_off_radius,
                 center=true,
                 $fn=curve_resolution);
        
        cylinder(h = stand_off_height+clearance+wall_thickness,
                 d = m3_through_hole_diameter, 
                 center=true, 
                 $fn=curve_resolution);
    }
}

module ScrewTabs()
{
    wall_thickness=4;
    cube()
}

BasicBox();
MountingStandOff();

