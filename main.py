import numpy as np
import streamlit as st


def calculate_capacitance(frequency, voltage, reactive_power):
    """
    Calculate the capacitance of a capacitor given its frequency, voltage, and reactive power.

    Parameters:
    frequency (float): The frequency in hertz (Hz).
    voltage (float): The voltage across the capacitor in volts (V).
    reactive_power (float): The reactive power of the capacitor in volt-amperes reactive (VAR).

    Returns:
    float: The capacitance in farads (F).
    """
    # Angular frequency (ω = 2 * π * frequency)
    angular_frequency = 2 * np.pi * frequency

    # Capacitance formula: C = Q / (V^2 * ω), where Q is reactive power (Q = P_reactive / V^2)
    capacitance = reactive_power / (voltage ** 2 * angular_frequency)

    return capacitance


def capacitor_cells(series_cap_count,
                    parallel_cap_count,
                    capacitor_overvoltage,
                    frequency,
                    double_star_tag):
    """
    Calculates parameters for capacitor cells in a 3-phase system.

    Parameters:
    -----------
    series_cap_count : int
        Number of capacitor cells in series.
    parallel_cap_count : int
        Number of capacitor cells in parallel.
    voltage_cell : float
        Voltage across a single cell (in volts).
    reactive_total : float
        Total reactive power of the system (in var).
    capacitor_overvoltage : float
        Overvoltage factor for the capacitor (unitless, > 1.0).
    frequency : float
        System frequency (in Hz).

    Returns:
    --------
    tuple
        - total_cap_count (int): Total number of capacitor cells.
        - rated_cell_voltage (float): Nominal voltage of a single capacitor cell (in volts).
        - rated_cell_power (float): Nominal reactive power handled by a single cell (in var).
        - rated_cell_capacitance (float): Capacitance of a single cell (in farads).
        - association_capacitance (float): Equivalent capacitance of the capacitor bank (in farads).
    """

    bank_capacitance = calculate_capacitance(frequency_system, line_voltage, reactive_power_three_phase)
    per_string_capacitors = series_cap_count * parallel_cap_count
    total_cap_count = 3 * double_star_tag * per_string_capacitors
    voltage_cell = phase_voltage / series_cap_count
    reactive_power_cell = reactive_power_three_phase / total_cap_count

    rated_cell_voltage = np.abs(voltage_cell) * capacitor_overvoltage
    rated_cell_power = np.abs(reactive_power_cell) * capacitor_overvoltage ** 2
    rated_cell_capacitance = calculate_capacitance(frequency, rated_cell_voltage, rated_cell_power)
    association_capacitance = double_star_tag * rated_cell_capacitance * parallel_cap_count * parallel_cap_count / series_cap_count

    rated_bank_power = rated_cell_power * total_cap_count
    rated_bank_voltage = np.sqrt(3) * rated_cell_voltage * series_cap_count

    cap_error = np.abs(association_capacitance - bank_capacitance) / bank_capacitance
    # print(f"cap_error = {cap_error / bank_capacitance:.2f} %")
    if cap_error > 0.01:
        print(f"possível erro na associação das capacitâncias {cap_error}")

    return (total_cap_count,
            rated_cell_voltage,
            rated_cell_power,
            rated_cell_capacitance,
            association_capacitance,
            rated_bank_power,
            rated_bank_voltage)


CAPACITOR_OVERVOLTAGE = 1.1
LINE_VOLTAGE = 12e3  # V
REACTIVE_POWER_THREE_PHASE = 6.5e6  # VAr
FREQUENCY_SYSTEM = 60  # Hz
DOUBLE_STAR_TAG = 2
SERIES_CAP_COUNT = 1
PARALLEL_CAP_COUNT = 1

# Streamlit App
st.title("Capacitor Bank Calculation")

# User inputs
capacitor_overvoltage = st.number_input("Capacitor Overvoltage", value=CAPACITOR_OVERVOLTAGE, step=0.01)
line_voltage = st.number_input("Line Voltage (kV)", value=LINE_VOLTAGE / 1e3, step=1.0)
line_voltage = 1e3 * line_voltage
phase_voltage = line_voltage / np.sqrt(3)  #V
reactive_power_three_phase = st.number_input("Reactive Power (MVAr)", value=REACTIVE_POWER_THREE_PHASE / 1e6, step=0.1)
reactive_power_three_phase = reactive_power_three_phase * 1e6
frequency_system = st.number_input("System Frequency (Hz)", value=FREQUENCY_SYSTEM, step=1)
double_star_tag = st.number_input("Double Star Tag", value=DOUBLE_STAR_TAG, step=1)
series_cap_count = st.number_input("Number of Series Capacitors", value=SERIES_CAP_COUNT, step=1)
parallel_cap_count = st.number_input("Number of Parallel Capacitors", value=PARALLEL_CAP_COUNT, step=1)

results = capacitor_cells(series_cap_count,
                          parallel_cap_count,
                          capacitor_overvoltage,
                          frequency_system,
                          double_star_tag)

# Transforming results into a dictionary
results_dict = {
    "total_cap_count": results[0],
    "rated_cell_voltage_kV": f"{results[1] / 1e3:.2f}",  # Convert V to kV and format
    "rated_cell_power_MVAr": f"{results[2] / 1e6:.2f}",  # Convert VAr to MVAr and format
    "rated_cell_capacitance_uF": f"{results[3] * 1e6:.2f}",  # Convert F to µF and format
    "association_capacitance_uF": f"{results[4] * 1e6:.2f}",  # Convert F to µF and format
    "rated_bank_power_MVAr": f"{results[5] / 1e6:.2f}",  # Convert VAr to MVAr and format
    "rated_bank_voltage_kV": f"{results[6] / 1e3:.2f}",  # Convert V to kV and format
}

st.write(results_dict)
