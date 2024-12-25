from tensorcircuit import Circuit
from tensorcircuit.transpilers.tqasm_transpiler import TQASMTranspiler

def test_tqasm_transpiler():
    qc = Circuit(2)
    qc.X(0)
    qc.H(1)
    qc.CX(0, 1)

    transpiler = TQASMTranspiler()
    tqasm_code = transpiler.transpile(qc)

    assert "qreg q[2];" in tqasm_code
    assert "x q[0] ;" in tqasm_code
    assert "h q[1] ;" in tqasm_code
    assert "cx q[0], q[1] ;" in tqasm_code
   
    print(tqasm_code)