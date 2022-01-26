import qiskit as qk
from qiskit import QuantumCircuit

qk.IBMQ.load_account()

# Create circuit with 1 quantum and 1 classical bit
circuit = QuantumCircuit(1, 1)

# Apply Hadamard gate to quantum bit --> Superposition
circuit.h(0)

# Measure quantum bit and store result in classical bit
circuit.measure(0, 0)

quantum_computer = qk.BasicAer.get_backend('qasm_simulator')

job = qk.execute(circuit, quantum_computer, shots=1)

counts = job.result().get_counts()

result = "heads" if  next(iter(counts.keys())) == "0" else "tails"

print(f"The quantum coin is: {result}")
