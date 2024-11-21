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

def calculate_inductance_with_ferrite(coil_diameter, wire_awg, num_layers, ferrite_mu_r=2000):
    """
    Calculate inductance with ferrite backing, with realistic enhancement
    """
    inductance, radius, length, turns = calculate_inductance_with_dimensions(coil_diameter, wire_awg, num_layers)
    
    # More conservative ferrite enhancement factor
    # Typically ferrite backing increases inductance by 30-80%
    ferrite_factor = 1 + (0.6 * math.atan(ferrite_mu_r/5000))  # Will give ~1.3-1.8x increase
    
    return inductance * ferrite_factor, radius, length, turns

def calculate_combined_efficiency_with_ferrite(transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth, ferrite_mu_r=2000):
    """
    Calculate efficiency with ferrite cores, using more realistic enhancement factors
    """
    tx_diameter, tx_awg, tx_layers = transmitter_params
    wire_diameters = {22: 0.000643, 24: 0.000511, 26: 0.000405}
    tx_wire_diameter = wire_diameters.get(tx_awg, 0.000643)
    
    # Calculate with ferrite enhancement
    tx_inductance, tx_radius, tx_length, tx_turns = calculate_inductance_with_ferrite(
        tx_diameter, tx_awg, tx_layers, ferrite_mu_r
    )
    
    tx_resistance = calculate_resistance(tx_turns, tx_diameter, tx_wire_diameter)
    tx_ac_resistance = calculate_ac_resistance(tx_resistance, frequency, tx_wire_diameter)
    
    # More realistic field enhancement with ferrite
    b_core = (MU_0 * tx_turns * current) / tx_length
    ferrite_field_enhancement = 1 + (0.5 * math.atan(ferrite_mu_r/5000))  # More conservative enhancement
    b_outside = (b_core * ferrite_field_enhancement) * math.exp(-wall_thickness / skin_depth)
    
    # Receiving coil calculations
    rx_diameter, rx_awg, rx_layers = receiver_params
    rx_wire_diameter = wire_diameters.get(rx_awg, 0.000643)
    rx_inductance, rx_radius, rx_length, rx_turns = calculate_inductance_with_ferrite(
        rx_diameter, rx_awg, rx_layers, ferrite_mu_r
    )
    
    rx_resistance = calculate_resistance(rx_turns, rx_diameter, rx_wire_diameter)
    rx_ac_resistance = calculate_ac_resistance(rx_resistance, frequency, rx_wire_diameter)
    
    # Enhanced coupling coefficient (more realistic)
    k = calculate_coupling_coefficient(tx_radius, rx_radius, wall_thickness/1000)
    k = k * (1 + 0.4 * math.atan(ferrite_mu_r/5000))  # More conservative enhancement
    k = min(k, 0.85)  # Cap at realistic maximum
    
    # Calculate mutual inductance
    mutual_inductance = k * math.sqrt(tx_inductance * rx_inductance)
    
    # Calculate induced voltage
    v_induced = calculate_induced_voltage(rx_turns, b_outside, rx_radius, frequency) * k
    
    # Power calculations with core losses
    omega = 2 * math.pi * frequency
    
    # Account for core losses
    core_loss_factor = 0.95  # Typical ferrite core efficiency at low frequencies
    
    input_power = current**2 * tx_ac_resistance
    output_power = (v_induced**2) / (4 * rx_ac_resistance) * core_loss_factor
    
    efficiency = (output_power / input_power) * 100
    
    return efficiency, v_induced, output_power

# Test with ferrite cores
transmitter_params = (15, 22, 2)  # 20mm diameter, AWG26, 2 layers
receiver_params = (6, 22, 5)    # 6mm diameter, AWG22, 5 layers
frequency = 3200
current = 0.03
wall_thickness = 3
skin_depth = calculate_skin_depth(frequency)

# Calculate with typical ferrite material (μr ≈ 2000)
efficiency, v_induced, power_transferred = calculate_combined_efficiency_with_ferrite(
    transmitter_params, receiver_params, frequency, current, wall_thickness, skin_depth, 
    ferrite_mu_r=2000
)

v_induced = v_induced * 1000  # Convert to mV
power_transferred = power_transferred * 1000  # Convert to mW

print(f"With Ferrite Cores (Corrected):")
print(f"Efficiency: {efficiency:.2f}%")
print(f"Induced Voltage: {v_induced:.3f} mV")
print(f"Power Transferred: {power_transferred:.3f} mW")


def main():
    freq = int(input("Enter Freq: "))
    skin_depth = calculate_skin_depth(freq)
    print(skin_depth)
    coil_diameter = float(input("Enter coil diam (mm): "))
    wire_awg = int(input("Enter wire AWG, 22, 24, 26: "))
    num_layers = int(input("How many layers: "))
    turns, wire_diameter = calculate_number_of_turns(coil_diameter, wire_awg, num_layers)
    print(str(turns) + " turns")
    inductance, coil_radius, coil_length, total_turns = calculate_inductance_with_dimensions(coil_diameter, wire_awg, num_layers)
    print(str(inductance) + " mH")
    resistance = calculate_resistance(turns, coil_diameter, wire_diameter)
    print(round(resistance, 4))
    q_factor = calculate_quality_factor(freq, inductance, resistance)
    print(q_factor)
    current = float(input("Enter current (mA): ")) / 1000  # Convert mA to A
    skin_depth = float(skin_depth.split()[0]) / 1000
    wall = float(input("Enter wall thickness (mm): ")) / 1000
    b_outside = calculate_b_outside(turns, current, coil_length, wall, skin_depth)
    print(b_outside)
    coil_radius = coil_diameter / 2000
    mV = calculate_induced_voltage(turns, b_outside, coil_radius, freq)
    print(mV * 1000)
    power_transferred = calculate_power_transferred(mV, resistance)
    print(power_transferred * 1000)
