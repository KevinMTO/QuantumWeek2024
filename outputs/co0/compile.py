import numpy as np
from mqt.qudits.quantum_circuit import QuantumCircuit
from scipy.stats import unitary_group


# Create the original circuit
circuit = QuantumCircuit(1, [5, 3], 0)

circuit.cu_one(0, unitary_group.rvs(5))
circuit.h(0)
circuit.x(0)
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])
circuit.rh(0, [0, 1])
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.pm(0, [2, 1, 3, 4, 0])
circuit.pm(0, [2, 1, 3, 4, 0])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])
circuit.pm(0, [2, 1, 3, 4, 0])
circuit.pm(0, [2, 1, 3, 4, 0])
circuit.x(0)
circuit.x(0)
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])
circuit.rh(0, [0, 1])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])
circuit.r(1, [0, 1, np.pi, np.pi / 2])
circuit.cx([0, 1], [0, 1, 0, np.pi/3])


# Simulate the original circuit
original_state = circuit.simulate()
print("Original circuit simulation result:")
print(original_state.round(3))

new_circuit0 = circuit.compileO0("faketraps2six")
print(f"\nNUmber of gates, without any optimization: {len(new_circuit0.instructions)}")

compiled_state0 = new_circuit0.simulate()
print("\nCompiled circuit simulation result:")
print(compiled_state0.round(3))
is_close_s0 = np.allclose(original_state, compiled_state0)
print(f"\nAre the simulation results close? {is_close_s0}")

new_circuit1 = circuit.compileO1("faketraps2six")
print(f"\nNUmber of gates, with resynth optimization: {len(new_circuit1.instructions)}")

compiled_state1 = new_circuit1.simulate()
print("\nCompiled circuit simulation result:")
print(compiled_state1.round(3))
is_close_s1 = np.allclose(original_state, compiled_state1)
print(f"\nAre the simulation results close? {is_close_s0}")

