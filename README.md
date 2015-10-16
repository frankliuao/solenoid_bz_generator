# solenoid_bz_generator
Calculate on-axis longitudinal magnetic field from user specified solenoids.

------
Usage:

  (Add the folder to your PYTHONPATH environment variable: export PYTHONPATH=$PYTHONPATH:`pwd`)

  In your Python code, do 
    
    from solenoid_bz_generator import solenoid_coils, plot_bz
  
  Start a new solenoid_coils class:
    
    your_coils = solenoid_coils()
  
  Add coils:
    
    your_coils.add_coil(z=z_0, l=l_0, r1=r1_0, r2=r2_0, j=j_0)
    
    your_coils.add_coil(z=z_1, l=l_1, r1=r1_1, r2=r2_1, j=j_1)
    
    ...
  
  Create a numpy array of longitudinal coordinates you want to calculate B_z at:
    
    z_array = numpy.arange(z_start, z_end, z_interval)
  
  Calculate the on-axis longitudinal B field:
    
    b_z = your_coils.calc_bz(z_array)
  
  Plot the field v.s. z:
    
    plot_bz(z_array, b_z)

------
Exmaple:

  For an example, just do python solenoid_bz_generator.py

  The code represents the solenoid coils for MICE (mice.iit.edu) Step IV.

  The main() function provides an exmaple on how to set up the calculation.
