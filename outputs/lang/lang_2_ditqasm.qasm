DITQASM 2.0;
qreg qudits [7][7,7,7,7,7,7,7];
qreg qubits [2][2,2];
creg meas[9];
x qudits[0];
h qubits[0];
cx (0, 1, 1, 0.0) qudits[0], qudits[1];
cx (0, 1, 1, 0.0) qudits[1], qudits[2];
rxy (0, 1, 3.141592653589793, 1.5707963267948966) qubits[1];
csum qudits[2], qubits[1];
pm (1, 0) qubits[0];
rh (0, 1) qudits[2];
ls (1.0471975511965976) qudits[2], qubits[0];
ms (1.0471975511965976) qudits[2], qubits[0];
rz (0, 1, 0.6283185307179586) qubits[1];
s qudits[6];
virtrz (1, 0.6283185307179586) qudits[6];
z qudits[4];
rdu qudits[0], qubits[0], qudits[1];
cuone (CUo7_tyRD.npy) qudits[0];
cutwo (CUt[7, 2]_vcDC.npy) qudits[0], qubits[1];
cumulti (CUm[7, 2, 2]_ZAId.npy) qudits[0], qubits[1], qubits[0];
measure qudits[0] -> meas[0];
measure qudits[1] -> meas[1];
measure qudits[2] -> meas[2];
measure qudits[3] -> meas[3];
measure qudits[4] -> meas[4];
measure qudits[5] -> meas[5];
measure qudits[6] -> meas[6];
measure qubits[0] -> meas[7];
measure qubits[1] -> meas[8];
