import math

# Constants
MU_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
MU_R_ALUMINUM = 1.00002  # Relative permeability of aluminum (unitless)
SIGMA_COPPER = 5.96e7  # Electrical conductivity of copper (S/m)
SIGMA_ALUMINUM = 3.5e7  # Electrical conductivity of aluminum (S/m)
RHO_COPPER = 1.68e-8  # Resistivity of copper (Ohm·m)

# 1. Skin Depth (delta)
def calculate_skin_depth(frequency):
    """
    Calculate the skin depth for a given material and frequency.
    :param material: "copper" or "aluminum"
    :param frequency: Frequency (Hz)
    :return: Skin depth (m)
    """
    sigma = SIGMA_ALUMINUM 
    mu_r = MU_R_ALUMINUM
    mu = MU_0 * mu_r
    omega = 2 * math.pi * frequency
    skin_depth = math.sqrt(2 / (mu * sigma * omega))
    return round(skin_depth * 1000, 4)

def calculate_number_of_turns(coil_diameter, wire_awg, num_layers):
    """
    Calculate the number of turns for a given coil diameter, wire diameter, and number of layers.
    :param coil_diameter: Diameter of the coil (m)
    :param wire_diameter: Diameter of the wire (m, including insulation)
    :param num_layers: Number of layers in the coil
    :return: Total number of turns
    """
    coil_diameter = coil_diameter / 1000
    wire_diameter = 0
    if wire_awg == 22:
        wire_diameter = 0.000643
    elif wire_awg == 24:
        wire_diameter = 0.000511
    elif wire_awg == 26:
        wire_diameter = 0.000405

    coil_circumference = math.pi * coil_diameter  # Circumference of the coil (m)
    turns_per_layer = int(coil_circumference / wire_diameter)  # Turns in one layer
    total_turns = turns_per_layer * num_layers  # Total turns with all layers
    return total_turns, wire_diameter

def calculate_inductance_with_dimensions(coil_diameter, wire_awg, num_layers):
    """
    Calculate the inductance of a coil based on its dimensions and wire properties.
    :param coil_diameter: Diameter of the coil (mm)
    :param wire_awg: AWG number of the wire
    :param num_layers: Number of layers in the coil
    :return: Inductance (H), radius (m), length (m), and total turns
    """
    # Calculate number of turns and wire diameter
    total_turns, wire_diameter = calculate_number_of_turns(coil_diameter, wire_awg, num_layers)

    # Calculate coil radius and length
    coil_radius = coil_diameter / 2000  # Convert to radius in meters (diameter / 2 / 1000)
    coil_length = num_layers * wire_diameter  # Total length of the coil in meters

    # Calculate inductance
    mu = MU_0  # Assuming free space or non-magnetic materials
    area = math.pi * (coil_radius ** 2)
    inductance = (mu * (total_turns ** 2) * area) / coil_length

    return round(inductance, 3), coil_radius, coil_length, total_turns

# 3. Resistance (R)
def calculate_resistance(num_turns, coil_diameter, wire_diameter):
    """
    Calculate the resistance of the coil.
    :param num_turns: Number of turns
    :param coil_diameter: Diameter of the coil (m)
    :param wire_diameter: Diameter of the wire (m)
    :return: Resistance (Ohms)
    """
    coil_diameter = coil_diameter / 1000
    wire_length = num_turns * math.pi * coil_diameter
    wire_area = math.pi * (wire_diameter / 2) ** 2
    return (RHO_COPPER * wire_length) / wire_area

# 4. Quality Factor (Q)
def calculate_quality_factor(frequency, inductance, resistance):
    """
    Calculate the quality factor of the coil.
    :param frequency: Frequency (Hz)
    :param inductance: Inductance (H)
    :param resistance: Resistance (Ohms)
    :return: Quality factor (unitless)
    """
    omega = 2 * math.pi * frequency
    return (omega * inductance) / resistance

# 5. Magnetic Field Outside Wall (B_outside)
def calculate_b_outside(num_turns, current, coil_length, wall_thickness, skin_depth):
    """
    Calculate the magnetic field outside the wall.
    :param num_turns: Number of turns
    :param current: Current (A)
    :param coil_length: Length of the coil (m)
    :param wall_thickness: Thickness of the wall (m)
    :param skin_depth: Skin depth (m)
    :return: Magnetic field outside (T)
    """
    b_core = (MU_0 * num_turns * current) / coil_length
    return b_core * math.exp(-wall_thickness / skin_depth)

# 6. Induced Voltage (V_induced)
def calculate_induced_voltage(num_turns, b_outside, coil_radius, frequency):
    """
    Calculate the induced voltage in the receiving coil.
    :param num_turns: Number of turns
    :param b_outside: Magnetic field outside (T)
    :param coil_radius: Radius of the receiving coil (m)
    :param frequency: Frequency (Hz)
    :return: Induced voltage (V)
    """
    area = math.pi * (coil_radius ** 2)
    flux = b_outside * area
    omega = 2 * math.pi * frequency
    return num_turns * omega * flux

# 7. Power Transferred (P)
def calculate_power_transferred(v_induced, resistance):
    """
    Calculate the power transferred to the receiving coil.
    :param v_induced: Induced voltage (V)
    :param resistance: Resistance of the receiving coil (Ohms)
    :return: Power transferred (W)
    """
    return (v_induced ** 2) / resistance

# 8. Efficiency (η)
def calculate_efficiency(power_out, power_in):
    """
    Calculate the efficiency of the system.
    :param power_out: Power delivered to the receiving coil (W)
    :param power_in: Power supplied to the transmitting coil (W)
    :return: Efficiency (percentage)
    """
    return (power_out / power_in) 

def calculate_coupling_coefficient(tx_radius, rx_radius, distance):
    """
    Calculate coupling coefficient based on coil geometries and separation.
    Returns a value between 0 and 1.
    """
    # Using modified Neumann formula for coaxial circular loops
    k = (2 * math.sqrt(tx_radius * rx_radius)) / (math.sqrt((tx_radius + rx_radius)**2 + distance**2))
    # Ensure k is between 0 and 1
    return min(k, 1.0)

def calculate_ac_resistance(dc_resistance, frequency, wire_diameter):
    """
    Account for AC resistance increase due to skin effect in the coil wire
    """
    skin_depth_copper = math.sqrt(2 * RHO_COPPER / (2 * math.pi * frequency * MU_0))
    factor = 1.0
    if wire_diameter > (2 * skin_depth_copper):
        factor = wire_diameter / (4 * skin_depth_copper)
    return dc_resistance * factor

def calculate_current(v_induced, power_transferred):
    """
    Calculate the current in the receiving coil.
    :param v_induced: Induced voltage (V)
    :param power_transferred: Power transferred (W)
    :return: Current (A)
    """
    # Calculate resistance using P = V^2 / R -> R = V^2 / P
    resistance = (v_induced ** 2) / power_transferred

    # Calculate current using I = V / R
    current = v_induced / resistance

    return current

# Combined Coil Efficiency Calculation
def calculate_combined_efficiency(transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth, target_voltage=3.3):
    """
    Calculate efficiency of power transfer between transmitting and receiving coils.
    :param transmitter_params: (coil_diameter, wire_awg, num_layers) for transmitting coil
    :param receiver_params: (coil_diameter, wire_awg, num_layers) for receiving coil
    :param frequency: Frequency of operation (Hz)
    :param current: Current in the transmitting coil (A)
    :param wall_thickness: Thickness of the aluminum wall (mm)
    :param skin_depth: Skin depth of the material (mm)
    :param target_voltage: Desired voltage on the receiving coil (V)
    :return: Efficiency (%), Induced Voltage (V), Power Transferred (W), Receiving Current (mA)
    """
    # Transmitting Coil Calculations
    tx_diameter, tx_awg, tx_layers = transmitter_params
    tx_wire_diameter = {22: 0.000643, 24: 0.000511, 26: 0.000405}[tx_awg]
    tx_inductance, tx_radius, tx_length, tx_turns = calculate_inductance_with_dimensions(tx_diameter, tx_awg, tx_layers)
    tx_resistance = calculate_resistance(tx_turns, tx_diameter, tx_wire_diameter)
    b_outside = calculate_b_outside(tx_turns, current, tx_length, wall_thickness / 1000, skin_depth / 1000)

    # Receiving Coil Calculations
    rx_diameter, rx_awg, rx_layers = receiver_params
    rx_wire_diameter = {22: 0.000643, 24: 0.000511, 26: 0.000405}[rx_awg]
    rx_inductance, rx_radius, rx_length, rx_turns = calculate_inductance_with_dimensions(rx_diameter, rx_awg, rx_layers)
    rx_resistance = calculate_resistance(rx_turns, rx_diameter, rx_wire_diameter)
    v_induced = calculate_induced_voltage(rx_turns, b_outside, rx_radius, frequency)

    k = calculate_coupling_coefficient(tx_radius, rx_radius, wall_thickness / 1000)

    # Adjust Induced Voltage for Coupling
    v_induced = v_induced * k

    # Power Transfer
    power_transferred = calculate_power_transferred(v_induced, rx_resistance)
    input_power = (current ** 2) * tx_resistance

    # Adjust for Target Voltage (3.3V)
    receiving_current = power_transferred / target_voltage  # I = P / V

    # Efficiency
    efficiency = calculate_efficiency(power_transferred, input_power)
    real_efficiency = receiving_current / current * 100

    return efficiency, v_induced, power_transferred, receiving_current * 1000, real_efficiency  # Return current in mA

# Example Usage
transmitter_params = (15, 26, 1)  #
receiver_params = (6, 22, 5)
frequency = 3200  # 10kHz
current = 0.03 # 25mA
wall_thickness = 3  # 3mm
skin_depth = calculate_skin_depth(frequency)  # Calculated from calculate_skin_depth()

efficiency, v_induced, power_transferred, current_mA, real_efficiency = calculate_combined_efficiency(
    transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth
)

v_induced = v_induced * 1000
power_transferred = power_transferred * 1000
current = current_mA

print(f"Induced Voltage: {v_induced:.3f} mV")
print(f"Power Transferred: {power_transferred:.3f} mW")
print(f"Current: {current_mA:.3f} mA")
print(f"Real Efficiency: {real_efficiency:.2f}%")


