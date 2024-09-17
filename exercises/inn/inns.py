from mqt.qudits.compiler.state_compilation.retrieve_state import generate_uniform_state
from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.simulation import MQTQuditProvider
from mqt.qudits.visualisation import plot_counts


circuit = QuantumCircuit(2, [3, 3])

state = generate_uniform_state(circuit.dimensions, "qudit-w-state")
circuit.set_initial_state(state)

provider = MQTQuditProvider()
print(f"Backends available with name 'inns': {provider.backends('inns')}")

backend = provider.get_backend("innsbruck01")
job = backend.run(circuit)
result = job.result()
counts = result.get_counts()

print(f"Number of operations: {len(circuit.instructions)}")
print(f"Number of qudits in the circuit: {circuit.num_qudits}")
plot_counts(counts, circuit)
