from mqt.qudits.quantum_circuit import QuantumCircuit, QuantumRegister
from mqt.qudits.quantum_circuit.components import ClassicRegister
import numpy as np

qreg_qudits = QuantumRegister("qudits", 7, [7, 7, 7, 7, 7, 7, 7])
qreg_qubits = QuantumRegister("qubits", 2, [2, 2])
cl_reg = ClassicRegister("classic", 3)

# Initialize the circuit
circ = QuantumCircuit(qreg_qudits)
circ.append(qreg_qubits)
circ.append_classic(cl_reg)

# Apply operations
circ.x(qreg_qudits[0])
circ.h(qreg_qubits[0])
circ.cx([qreg_qudits[0], qreg_qudits[1]])
circ.cx([qreg_qudits[1], qreg_qudits[2]])
circ.r(qreg_qubits[1], [0, 1, np.pi, np.pi / 2])
circ.csum([qreg_qudits[2], qreg_qubits[1]])
circ.pm(qreg_qubits[0], [1, 0])
circ.rh(qreg_qudits[2], [0, 1])
circ.ls([qreg_qudits[2], qreg_qubits[0]], [np.pi / 3])
circ.ms([qreg_qudits[2], qreg_qubits[0]], [np.pi / 3])
circ.rz(qreg_qubits[1], [0, 1, np.pi / 5])
circ.s(qreg_qudits[6])
circ.virtrz(qreg_qudits[6], [1, np.pi / 5])
circ.z(qreg_qudits[4])
circ.randu([qreg_qudits[0], qreg_qubits[0], qreg_qudits[1]])
circ.cu_one(qreg_qudits[0], np.identity(7))
circ.cu_two([qreg_qudits[0], qreg_qubits[1]], np.identity(7 * 2))
circ.cu_multi([qreg_qudits[0], qreg_qubits[1], qreg_qubits[0]], np.identity(7 * 2 * 2))

file = circ.save_to_file(file_name="./lang_2_ditqasm")
