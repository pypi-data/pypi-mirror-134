# Guan is an open-source python package developed and maintained by https://www.guanjihuan.com/about. The primary location of this package is on website https://py.guanjihuan.com.

# calculate conductance

import numpy as np
import copy
import guan

def calculate_conductance(fermi_energy, h00, h01, length=100):
    right_self_energy, left_self_energy, gamma_right, gamma_left = guan.self_energy_of_lead(fermi_energy, h00, h01)
    for ix in range(length):
        if ix == 0:
            green_nn_n = guan.green_function(fermi_energy, h00, broadening=0, self_energy=left_self_energy)
            green_0n_n = copy.deepcopy(green_nn_n)
        elif ix != length-1:
            green_nn_n = guan.green_function_nn_n(fermi_energy, h00, h01, green_nn_n, broadening=0)
            green_0n_n = guan.green_function_in_n(green_0n_n, h01, green_nn_n)
        else:
            green_nn_n = guan.green_function_nn_n(fermi_energy, h00, h01, green_nn_n, broadening=0, self_energy=right_self_energy)
            green_0n_n = guan.green_function_in_n(green_0n_n, h01, green_nn_n)
    conductance = np.trace(np.dot(np.dot(np.dot(gamma_left, green_0n_n), gamma_right), green_0n_n.transpose().conj()))
    return conductance

def calculate_conductance_with_fermi_energy_array(fermi_energy_array, h00, h01, length=100):
    dim = np.array(fermi_energy_array).shape[0]
    conductance_array = np.zeros(dim)
    i0 = 0
    for fermi_energy_0 in fermi_energy_array:
        conductance_array[i0] = np.real(calculate_conductance(fermi_energy_0, h00, h01, length))
        i0 += 1
    return conductance_array

def calculate_conductance_with_disorder(fermi_energy, h00, h01, disorder_intensity=2.0, disorder_concentration=1.0, length=100):
    right_self_energy, left_self_energy, gamma_right, gamma_left = guan.self_energy_of_lead(fermi_energy, h00, h01)
    dim = np.array(h00).shape[0]
    for ix in range(length):
        disorder = np.zeros((dim, dim))
        for dim0 in range(dim):
            if np.random.uniform(0, 1)<=disorder_concentration:
                disorder[dim0, dim0] = np.random.uniform(-disorder_intensity, disorder_intensity)
        if ix == 0:
            green_nn_n = guan.green_function(fermi_energy, h00+disorder, broadening=0, self_energy=left_self_energy)
            green_0n_n = copy.deepcopy(green_nn_n)
        elif ix != length-1:
            green_nn_n = guan.green_function_nn_n(fermi_energy, h00+disorder, h01, green_nn_n, broadening=0)
            green_0n_n = guan.green_function_in_n(green_0n_n, h01, green_nn_n)
        else:
            green_nn_n = guan.green_function_nn_n(fermi_energy, h00+disorder, h01, green_nn_n, broadening=0, self_energy=right_self_energy)
            green_0n_n = guan.green_function_in_n(green_0n_n, h01, green_nn_n)
    conductance = np.trace(np.dot(np.dot(np.dot(gamma_left, green_0n_n), gamma_right), green_0n_n.transpose().conj()))
    return conductance

def calculate_conductance_with_disorder_intensity_array(fermi_energy, h00, h01, disorder_intensity_array, disorder_concentration=1.0, length=100, calculation_times=1):
    dim = np.array(disorder_intensity_array).shape[0]
    conductance_array = np.zeros(dim)
    i0 = 0
    for disorder_intensity_0 in disorder_intensity_array:
        for times in range(calculation_times):
            conductance_array[i0] = conductance_array[i0]+np.real(calculate_conductance_with_disorder(fermi_energy, h00, h01, disorder_intensity=disorder_intensity_0, disorder_concentration=disorder_concentration, length=length))
        i0 += 1
    conductance_array = conductance_array/calculation_times
    return conductance_array

def calculate_conductance_with_disorder_concentration_array(fermi_energy, h00, h01, disorder_concentration_array, disorder_intensity=2.0, length=100, calculation_times=1):
    dim = np.array(disorder_concentration_array).shape[0]
    conductance_array = np.zeros(dim)
    i0 = 0
    for disorder_concentration_0 in disorder_concentration_array:
        for times in range(calculation_times):
            conductance_array[i0] = conductance_array[i0]+np.real(calculate_conductance_with_disorder(fermi_energy, h00, h01, disorder_intensity=disorder_intensity, disorder_concentration=disorder_concentration_0, length=length))
        i0 += 1
    conductance_array = conductance_array/calculation_times
    return conductance_array

def calculate_conductance_with_scattering_length_array(fermi_energy, h00, h01, length_array, disorder_intensity=2.0, disorder_concentration=1.0, calculation_times=1):
    dim = np.array(length_array).shape[0]
    conductance_array = np.zeros(dim)
    i0 = 0
    for length_0 in length_array:
        for times in range(calculation_times):
            conductance_array[i0] = conductance_array[i0]+np.real(calculate_conductance_with_disorder(fermi_energy, h00, h01, disorder_intensity=disorder_intensity, disorder_concentration=disorder_concentration, length=length_0))
        i0 += 1
    conductance_array = conductance_array/calculation_times
    return conductance_array