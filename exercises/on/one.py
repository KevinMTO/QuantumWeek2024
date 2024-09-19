import numpy as np
from mqt.qudits.compiler import QuditCompiler
from mqt.qudits.compiler.compilation_minitools.naive_unitary_verifier import phy_sdit_sim
from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.simulation import MQTQuditProvider

# Create the original circuit
circuit = QuantumCircuit(1, [6], 0)
circuit.z(0)

# Simulate the original circuit
original_state = circuit.simulate()
print("Original circuit simulation result:")
print(original_state.round(3))

# Set up the provider and backend
provider = MQTQuditProvider()
backend_ion = provider.get_backend("faketraps2six")

# Compile the circuit
qudit_compiler = QuditCompiler()
passes = ["LocQRPass"]  # Change it to LocAdaPass ;)
new_circuit = qudit_compiler.compile(backend_ion, circuit, passes)
print(f"\nNumber of gates: {len(new_circuit.instructions)}")

# Simulate the compiled circuit
compiled_state = phy_sdit_sim(new_circuit)
print("\nCompiled circuit simulation result:")
print(compiled_state.round(3))
print()

# Compare the results
is_close = np.allclose(original_state, compiled_state)
print(f"\nAre the simulation results close? {is_close}")
