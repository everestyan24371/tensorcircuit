from tensorcircuit import Circuit

class OpenQASMTranspiler:
    def transpile(self, quantum_circuit):
        qasm_code = ""
        num_qubits = quantum_circuit.num_qubits
        qasm_code += f"qreg q[{num_qubits}];\n"
        qasm_code += f"creg c[{num_qubits}];\n"  

        for gate, qubits, *params in quantum_circuit.operations:
            if gate == 'X':
                qasm_code += f"x q[{qubits[0]}];\n"
            elif gate == 'Y':
                qasm_code += f"y q[{qubits[0]}];\n"
            elif gate == 'Z':
                qasm_code += f"z q[{qubits[0]}];\n"
            elif gate == 'H':
                qasm_code += f"h q[{qubits[0]}];\n"
            elif gate == 'S':
                qasm_code += f"s q[{qubits[0]}];\n"
            elif gate == 'T':
                qasm_code += f"t q[{qubits[0]}];\n"
            elif gate == 'RX':
                theta = params[0]
                qasm_code += f"rx({theta}) q[{qubits[0]}];\n"
            elif gate == 'RY':
                theta = params[0]
                qasm_code += f"ry({theta}) q[{qubits[0]}];\n"
            elif gate == 'RZ':
                theta = params[0]
                qasm_code += f"rz({theta}) q[{qubits[0]}];\n"
            elif gate == 'CX':
                qasm_code += f"cx q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'CZ':
                qasm_code += f"cz q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'SWAP':
                qasm_code += f"swap q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'MEASURE':
                qasm_code += f"measure q[{qubits[0]}] -> c[{qubits[0]}];\n"
        return qasm_code