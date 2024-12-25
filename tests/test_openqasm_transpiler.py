from tensorcircuit import Circuit
from tensorcircuit.transpilers.openqasm_transpiler import OpenQASMTranspiler
def test_openqasm_transpiler():
    qc = Circuit(2)
    qc.X(0)
    qc.H(1)
    qc.CX(0, 1)
    qc.measure_all()

    transpiler = OpenQASMTranspiler()
    qasm_code = transpiler.transpile(qc)

    assert "qreg q[2];" in qasm_code
    assert "creg c[2];" in qasm_code
    assert "x q[0];" in qasm_code
    assert "h q[1];" in qasm_code
    assert "cx q[0], q[1];" in qasm_code
    assert "measure q[0] -> c[0];" in qasm_code
    assert "measure q[1] -> c[1];" in qasm_code

    print(qasm_code)

# 执行测试
test_openqasm_transpiler()