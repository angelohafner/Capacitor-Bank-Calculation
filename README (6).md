
# Capacitor Bank Calculation with Streamlit

This project is a **Streamlit** app for calculating various parameters related to capacitor banks in 3-phase systems.

## Features

- Calculates total capacitor count, rated cell voltage, rated power, and capacitance.
- Computes the equivalent capacitance of the capacitor bank.
- Allows user input for key parameters such as overvoltage factor, line voltage, reactive power, frequency, etc.

## Getting Started

### Prerequisites

Ensure you have Python installed and the following Python packages:

- `numpy`
- `streamlit`

Install the required packages using:

```bash
pip install numpy streamlit
```

### Running the Application

1. Save the code to a Python file, e.g., `capacitor_bank_calculator.py`.
2. Run the Streamlit application:

```bash
streamlit run capacitor_bank_calculator.py
```

3. Open the provided URL in your browser to interact with the app.

## Input Parameters

- **Capacitor Overvoltage**: Overvoltage factor for the capacitors.
- **Line Voltage (kV)**: The line voltage in kilovolts (kV).
- **Reactive Power (MVAr)**: The total reactive power in megavolt-amperes reactive (MVAr).
- **System Frequency (Hz)**: Frequency of the electrical system in hertz (Hz).
- **Double Star Tag**: Determines the configuration of the capacitor bank.
- **Number of Series Capacitors**: The number of capacitor cells connected in series.
- **Number of Parallel Capacitors**: The number of capacitor cells connected in parallel.

## Output Results

The app displays the following calculated parameters:

- **Total Capacitor Count**: Total number of capacitors in the bank.
- **Rated Cell Voltage (kV)**: Voltage across a single capacitor cell.
- **Rated Cell Power (MVAr)**: Reactive power handled by a single cell.
- **Rated Cell Capacitance (µF)**: Capacitance of a single capacitor cell.
- **Association Capacitance (µF)**: Equivalent capacitance of the capacitor bank.
- **Rated Bank Power (MVAr)**: Total power of the capacitor bank.
- **Rated Bank Voltage (kV)**: Total voltage of the capacitor bank.

## Example

Adjust the input parameters using the Streamlit sliders and number inputs, and the results will be dynamically updated.

## License

This project is licensed under the MIT License. Feel free to use, modify, and share!

---

### Author

Developed by Angelo Alfredo Hafner.
