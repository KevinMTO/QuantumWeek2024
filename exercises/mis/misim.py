from mqt.qudits.quantum_circuit import QuantumCircuit
from mqt.qudits.quantum_circuit.components.quantum_register import QuantumRegister
from mqt.qudits.simulation import MQTQuditProvider
from mqt.qudits.visualisation import plot_state

circuit = QuantumCircuit()
qudit_reg = QuantumRegister("qudits", 1, [3])
ququart_reg = QuantumRegister("ququart", 1, [4])
circuit.append(qudit_reg)
circuit.append(ququart_reg)

h = circuit.h(ququart_reg[0])
csum = circuit.csum([ququart_reg[0], qudit_reg[0]])

provider = MQTQuditProvider()
print(f"Backends available with name 'sim': {provider.backends('sim')}")


backend = provider.get_backend("misim")
job = backend.run(circuit)
result = job.result()
state_vector = result.get_state_vector()

print(f"Number of operations: {len(circuit.instructions)}")
print(f"Number of qudits in the circuit: {circuit.num_qudits}")
plot_state(state_vector, circuit)
