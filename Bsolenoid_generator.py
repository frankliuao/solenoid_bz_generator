# coding=ASCII
"""Generate on-axis magnetic field for given solenoid coils

"""
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

class solenoid_coils(object):

    def __init__(self):
        self.coil_z_list = []
        self.coil_current_density_list = []
        self.number_of_coils = 0
        self.coil_length_list = []
        self.coil_r1_list = []
        self.coil_r2_list = []

    def add_coil(self, z, l, r1, r2, j):
        self.coil_z_list.append(float(z))
        self.coil_current_density_list.append(float(j))
        self.coil_length_list.append(float(l))
        self.coil_r1_list.append(float(r1))
        self.coil_r2_list.append(float(r2))
        self.number_of_coils += 1

    def profile_func(self, z):

        return 0.5+z/2/(self.coil_r2-self.coil_r1)*\
                   np.log((self.coil_r2+np.sqrt(self.coil_r2**2+z**2))/
                          (self.coil_r1+np.sqrt(self.coil_r1**2+z**2)))

    def calc_bz_point(self, z):
        self.current_density = np.array(self.coil_current_density_list)
        self.coil_z = np.array(self.coil_z_list)
        self.coil_length = np.array(self.coil_length_list)
        self.coil_r1 = np.array(self.coil_r1_list)
        self.coil_r2 = np.array(self.coil_r2_list)
        bz_all = np.sum(4*np.pi*1e-7*self.current_density*
                    (self.coil_r2-self.coil_r1)*\
                    (self.profile_func(z-(self.coil_z-self.coil_length/2))-
                     self.profile_func(z-(self.coil_z+self.coil_length/2))))
        return bz_all

    def calc_bz(self, z_array):
        calc_bz_point = np.vectorize(self.calc_bz_point)
        return(calc_bz_point(z_array))


def plot_bz(z, bz):
    f_handle = plt.figure()
    axes_handle = f_handle.add_subplot(111)
    axes_handle.plot(z, bz)
    axes_handle.set_xlabel("Z (m)")
    axes_handle.set_ylabel("B_z(T)")
    plt.show()


def main():
    mice_coils = solenoid_coils()
    mice_coils.add_coil(z=16.96-3.2, l=0.1106, r1=0.258, r2=0.3258, j=134e6)
    mice_coils.add_coil(z=16.96-2.45, l=1.3143, r1=0.258, r2=0.2801, j=147e6)
    mice_coils.add_coil(z=16.96-1.7, l=0.1106, r1=0.258, r2=0.3189, j=131e6)
    mice_coils.add_coil(z=16.96-1.3, l=0.1995, r1=0.258, r2=0.2889, j=135e6)
    mice_coils.add_coil(z=16.96-0.861, l=0.2013, r1=0.258, r2=0.3042, j=113e6)
    mice_coils.add_coil(z=16.96-0.203, l=0.2133, r1=0.267, r2=0.3618, j=104e6)
    mice_coils.add_coil(z=16.96+0.203, l=0.2133, r1=0.267, r2=0.3618, j=-104e6)
    mice_coils.add_coil(z=16.96+0.861, l=0.2013, r1=0.258, r2=0.3042, j=-113e6)
    mice_coils.add_coil(z=16.96+1.3, l=0.1995, r1=0.258, r2=0.2889, j=-135e6)
    mice_coils.add_coil(z=16.96+1.7, l=0.1106, r1=0.258, r2=0.3189, j=-131e6)
    mice_coils.add_coil(z=16.96+2.45, l=1.3143, r1=0.258, r2=0.2801, j=-147e6)
    mice_coils.add_coil(z=16.96+3.2, l=0.1106, r1=0.258, r2=0.3258, j=-134e6)
    bz = mice_coils.calc_bz(np.arange(12, 22, 0.05))
    plot_bz(np.arange(12, 22, 0.05), bz)


if __name__ == "__main__":
    main()