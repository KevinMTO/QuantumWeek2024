from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.compiler.state_compilation.retrieve_state import generate_uniform_state
import numpy as np

dims = [3, 2]
state = generate_uniform_state(dims, "qudit-w-state")

circuit = QuantumCircuit(len(dims), dims, 0)
circuit.set_initial_state(state)
print(f"Number of instructions in the circuit: {len(circuit.instructions)}")


final_state_vector = circuit.simulate()
print(f"Final state is: {final_state_vector.round(3)}")
is_close = np.allclose(final_state_vector, state)
print(f"Is the simulated state close to the expected state? {is_close}")

