from mqt.qudits.quantum_circuit import QuantumCircuit

circuit = QuantumCircuit()
circuit.load_from_file("./ditqasm_sample.qasm")

print(f"Number of qudits: {circuit.num_qudits}")
print(f"Dimensions of qudits: {circuit.dimensions}")
print(f"Total number of gates in the circuit: {circuit.number_gates}")
print(f"Number of quantum registers: {len(circuit.quantum_registers)}")
print(f"Number of classical registers: {circuit.num_cl}")
