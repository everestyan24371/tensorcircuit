class TQASMTranspiler:
    def transpile(self, quantum_circuit):
        tqasm_code = ""
        num_qubits = quantum_circuit.num_qubits
        tqasm_code += f"qreg q[{num_qubits}];\n"
        tqasm_code += f"creg c[{num_qubits}];\n"  

        for gate, qubits, *params in quantum_circuit.operations:
            if gate == 'X':
                tqasm_code += f"x q[{qubits[0]}];\n"
            elif gate == 'Y':
                tqasm_code += f"y q[{qubits[0]}];\n"
            elif gate == 'Z':
                tqasm_code += f"z q[{qubits[0]}];\n"
            elif gate == 'H':
                tqasm_code += f"h q[{qubits[0]}];\n"
            elif gate == 'S':
                tqasm_code += f"s q[{qubits[0]}];\n"
            elif gate == 'T':
                tqasm_code += f"t q[{qubits[0]}];\n"
            elif gate == 'RX':
                theta = params[0]
                tqasm_code += f"rx({theta}) q[{qubits[0]}];\n"
            elif gate == 'RY':
                theta = params[0]
                tqasm_code += f"ry({theta}) q[{qubits[0]}];\n"
            elif gate == 'RZ':
                theta = params[0]
                tqasm_code += f"rz({theta}) q[{qubits[0]}];\n"
            elif gate == 'CX':
                tqasm_code += f"cx q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'CZ':
                tqasm_code += f"cz q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'CS':
                tqasm_code += f"cs q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'CT':
                tqasm_code += f"ct q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'SWAP':
                tqasm_code += f"swap q[{qubits[0]}], q[{qubits[1]}];\n"
            elif gate == 'MEASURE':
                tqasm_code += f"measure q[{qubits[0]}] -> c[{qubits[0]}];\n"
        return tqasm_code