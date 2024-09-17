from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.quantum_circuit.components.quantum_register import QuantumRegister
from mqt.qudits.simulation import MQTQuditProvider
from mqt.qudits.visualisation import plot_counts

circuit = QuantumCircuit()
reg_qutrit = QuantumRegister("qutrit_0", 1, [3])
qutrit_reg = QuantumRegister("qutrit_1", 1, [3])
circuit.append(reg_qutrit)
circuit.append(qutrit_reg)

h = circuit.h(qutrit_reg[0])
csum = circuit.csum([qutrit_reg[0], reg_qutrit[0]])

provider = MQTQuditProvider()
backend = provider.get_backend("faketraps2trits")
job = backend.run(circuit)
result = job.result()
counts = result.get_counts()
plot_counts(counts, circuit)
