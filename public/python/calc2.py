import math

# Constants
MU_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
MU_R_FERRITE = 1000  # Relative permeability of the ferrite core (example value)
MU_R_ALUMINUM = 1.00002  # Relative permeability of aluminum (unitless)
SIGMA_COPPER = 5.96e7  # Electrical conductivity of copper (S/m)
SIGMA_ALUMINUM = 3.5e7  # Electrical conductivity of aluminum (S/m)
RHO_COPPER = 1.68e-8  # Resistivity of copper (Ohm·m)

# 1. Skin Depth (delta)
def calculate_skin_depth(frequency):
    sigma = SIGMA_ALUMINUM 
    mu_r = MU_R_ALUMINUM
    mu = MU_0 * mu_r
    omega = 2 * math.pi * frequency
    skin_depth = math.sqrt(2 / (mu * sigma * omega))
    return round(skin_depth * 1000, 4)

# 2. Number of Turns
def calculate_number_of_turns(coil_diameter, wire_awg, num_layers):
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

# 3. Inductance with Ferrite Core
def calculate_inductance_with_ferrite(coil_diameter, wire_awg, num_layers):
    total_turns, wire_diameter = calculate_number_of_turns(coil_diameter, wire_awg, num_layers)
    coil_radius = coil_diameter / 2000  # Convert to radius in meters (diameter / 2 / 1000)
    coil_length = num_layers * wire_diameter  # Total length of the coil in meters

    mu = MU_0 * MU_R_FERRITE
    area = math.pi * (coil_radius ** 2)
    inductance = (mu * (total_turns ** 2) * area) / coil_length

    return round(inductance, 3), coil_radius, coil_length, total_turns

# 4. Resistance (R)
def calculate_resistance(num_turns, coil_diameter, wire_diameter):
    coil_diameter = coil_diameter / 1000
    wire_length = num_turns * math.pi * coil_diameter
    wire_area = math.pi * (wire_diameter / 2) ** 2
    return (RHO_COPPER * wire_length) / wire_area

# 5. Quality Factor (Q)
def calculate_quality_factor(frequency, inductance, resistance):
    omega = 2 * math.pi * frequency
    return (omega * inductance) / resistance

# 6. Magnetic Field with Ferrite Core
def calculate_b_outside_with_ferrite(num_turns, current, coil_length, wall_thickness, skin_depth):
    b_core = (MU_0 * MU_R_FERRITE * num_turns * current) / coil_length  # Enhanced B_core with ferrite
    return b_core * math.exp(-wall_thickness / skin_depth)

# 7. Induced Voltage (V_induced)
def calculate_induced_voltage(num_turns, b_outside, coil_radius, frequency):
    area = math.pi * (coil_radius ** 2)
    flux = b_outside * area
    omega = 2 * math.pi * frequency
    return num_turns * omega * flux

# 8. Power Transferred (P)
def calculate_power_transferred(v_induced, resistance):
    return (v_induced ** 2) / resistance

# 9. Efficiency (η)
def calculate_efficiency(power_out, power_in):
    return (power_out / power_in) * 100

# Combined Coil Efficiency with Ferrite
def calculate_combined_efficiency_with_ferrite(transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth):
    tx_diameter, tx_awg, tx_layers = transmitter_params
    tx_inductance, tx_radius, tx_length, tx_turns = calculate_inductance_with_ferrite(tx_diameter, tx_awg, tx_layers)
    tx_resistance = calculate_resistance(tx_turns, tx_diameter, 0.000643)  # AWG22 wire diameter
    b_outside = calculate_b_outside_with_ferrite(tx_turns, current, tx_length, wall_thickness / 1000, skin_depth / 1000)

    rx_diameter, rx_awg, rx_layers = receiver_params
    rx_inductance, rx_radius, rx_length, rx_turns = calculate_inductance_with_ferrite(rx_diameter, rx_awg, rx_layers)
    rx_resistance = calculate_resistance(rx_turns, rx_diameter, 0.000643)  # AWG22 wire diameter
    v_induced = calculate_induced_voltage(rx_turns, b_outside, rx_radius, frequency)

    power_transferred = calculate_power_transferred(v_induced, rx_resistance)
    input_power = (current ** 2) * tx_resistance
    efficiency = calculate_efficiency(power_transferred, input_power)

    return efficiency, v_induced, power_transferred

# Example Usage
transmitter_params = (15, 22, 2)  # Transmitting coil: 15mm diameter, AWG22, 2 layers
receiver_params = (6, 22, 4)  # Receiving coil: 6mm diameter, AWG22, 4 layers
frequency = 3200  # 10kHz
current = 0.03  # 25mA
wall_thickness = 3  # mm
skin_depth = calculate_skin_depth(frequency)  # mm (from calculate_skin_depth())

efficiency, v_induced, power_transferred = calculate_combined_efficiency_with_ferrite(
    transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth
)

v_induced = v_induced * 1000  # Convert to mV
power_transferred = power_transferred * 1000  # Convert to mW

print(f"Efficiency: {efficiency:.2f}%")
print(f"Induced Voltage: {v_induced:.3f} mV")
print(f"Power Transferred: {power_transferred:.3f} mW")