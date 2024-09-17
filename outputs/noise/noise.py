from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.quantum_circuit.components.quantum_register import QuantumRegister
from mqt.qudits.simulation import MQTQuditProvider
from mqt.qudits.simulation.noise_tools import Noise, NoiseModel
from mqt.qudits.visualisation import plot_counts

circuit = QuantumCircuit()
qudit_reg = QuantumRegister("qudits", 1, [3])
qubit_reg = QuantumRegister("qubit", 1, [2])
circuit.append(qudit_reg)
circuit.append(qubit_reg)

h = circuit.h(qubit_reg[0])
csum = circuit.csum([qubit_reg[0], qudit_reg[0]])

provider = MQTQuditProvider()
backend = provider.get_backend("tnsim")

# Depolarizing quantum errors
local_error = Noise(probability_depolarizing=0.5, probability_dephasing=0.5)
# Add errors to noise_tools model
noise_model = NoiseModel()  # We know that the architecture is only two qudits
# Local Gates
noise_model.add_quantum_error_locally(local_error, ["h"])

job = backend.run(circuit, noise_model=noise_model, shots=50)
result = job.result()
counts = result.get_counts()
plot_counts(counts, circuit)

