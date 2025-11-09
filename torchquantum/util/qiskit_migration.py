from qiskit import transpile, QuantumCircuit
from qiskit_aer import AerSimulator

def execute(experiments: QuantumCircuit, backend : AerSimulator, 
    parameter_binds=None, shots=None):
    # migration to qiskit>1.0
    
    transpiled_experiments = transpile(experiments, backend)
    run_kwargs = {}
    if parameter_binds:
        run_kwargs["parameter_binds"] = parameter_binds
    if shots:
        run_kwargs["shots"] = shots

    job = backend.run(transpiled_experiments, **run_kwargs)
    return job


