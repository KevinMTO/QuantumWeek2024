import numpy as np
from mqt.qudits.compiler import QuditCompiler
from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.simulation import MQTQuditProvider
from mqt.qudits.visualisation.plot_information import remap_result

# Create the original circuit
circuit = QuantumCircuit(2, [3, 3], 0)
circuit.h(0)
circuit.csum([0, 1])

# Simulate the original circuit
original_state = circuit.simulate()
print("Original circuit simulation result:")
print(original_state.round(3))

# Set up the provider and backend
provider = MQTQuditProvider()
backend_ion = provider.get_backend("faketraps2six")

# Compile the circuit
qudit_compiler = QuditCompiler()
passes = ["PhyEntQRCEXPass"]
new_circuit = qudit_compiler.compile(backend_ion, circuit, passes)

# Simulate the compiled circuit
compiled_state = new_circuit.simulate()
compiled_state_remapped = remap_result(compiled_state, new_circuit)
print("\nCompiled circuit simulation result:")
print(compiled_state_remapped.round(3))

# Compare the results
is_close = np.allclose(original_state, compiled_state_remapped)
print(f"\nAre the simulation results close? {is_close}")


