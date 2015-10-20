# solenoid_bz_generator
Calculate on-axis longitudinal magnetic field from user specified solenoids.

-----
Requirements:

  matplotlib

  numpy

------
Usage:

  (Add the folder to your PYTHONPATH environment variable: 
  ```bash
  export PYTHONPATH=$PYTHONPATH:`pwd`
  ```

  In your Python code, do 
  ```python
  >>> from solenoid_bz_generator import solenoid_coils, plot_bz
  ```
  
  Start a new solenoid_coils class:
  ```python
  >>> your_coils = solenoid_coils()
  ```
  Add coils:
  ```python  
  >>> your_coils.add_coil(z=z_0, l=l_0, r1=r1_0, r2=r2_0, j=j_0)
    
  >>> your_coils.add_coil(z=z_1, l=l_1, r1=r1_1, r2=r2_1, j=j_1)
    
  >>> ...
  ```
  Create a numpy array of longitudinal coordinates you want to calculate B_z at:
  ```python
  >>> z_array = numpy.arange(z_start, z_end, z_interval)
  ```
  Calculate the on-axis longitudinal B field:
  ```python
  >>> b_z = your_coils.calc_bz(z_array)
  ```
  Plot the field v.s. z:
  ```python  
  >>> plot_bz(z_array, b_z)
  ```
------
Exmaple:

  For a quick example, just do 
  ```bash
  > python solenoid_bz_generator.py
  ```
  The coil setup represents the ideal scenario for MICE (mice.iit.edu) Step IV.

  The main() function provides an exmaple on how to set up the coils, calculate
  and plot.

  For other examples, for instance the cooling channel coils as built running 
  at their nominal currents, or the cooling channel coils as built but running
  in a "modified baseline mode" with degraded M1@ SSD, do
  ```bash
  > python solenoid_bz_generator.py SCENARIO_NUMBER
  ```
  where SCENARIO_NUMBER can be any number between 1 to 4. 
