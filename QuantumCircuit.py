### Alex Lim
### October 19, 2021
### QuantumCircuit


import numpy as np
# import random as random
# import cmath as cmath


# Information about quantum logic gates from https://en.wikipedia.org/wiki/Quantum_logic_gate

"""
The Bell states (or EPR pairs) are specific quantum states of two qubits that represent
the simplest (and maximal) examples of quantum entanglement; conceptually,
they fall under the study of quantum information science.
The Bell states are a form of entangled and normalized basis vectors.
"""

### Identity gates ###
"""The identity gate is the identity matrix"""
# Identity gate for a single qubit
identity_2d_matrix = np.diag([1,1])
# Identity gate for two qubits
identity_3d_matrix = np.diag([1,1,1])

### Pauli gates ###
"""
The Pauli gates (X, Y, Z) are the three Pauli matrices and act on a single qubit.
The Pauli X, Y, and Z equate, respectively,
    to a rotation around the x, y, and z axes of the Bloch sphere by pi radians.
"""
# Pauli-X gate for a single qubit
    # (equivalent to the NOT gate for classical computers with respect to the standard basis |0⟩, |1⟩)
Pauli_X_gate = np.array([[0,1],
                         [1,0]])
# Pauli-Y gate for a single qubit
Pauli_Y_gate = np.array([[0,-1j],
                         [1j,0]])
# Pauli-Z gate for a single qubit
Pauli_Z_gate = np.array([[1,0],
                         [0,-1]])
# CNOT gate (or controlled Pauli-X gate)
    # maps the basis states |a,b⟩ ⟼ |a, a ⊕ b⟩, where ⊕ is XOR.
# CNOT_gate = np.kron(identity_2d_matrix, Pauli_X_gate)
CNOT_gate = np.kron(np.diag([1, 0]), identity_2d_matrix) + \
            np.kron(np.diag([0, 1]), Pauli_X_gate)
# CNOT_gate = np.array([[1, 0, 0, 0],
#                       [0, 1, 0, 0],
#                       [0, 0, 0, 1],
#                       [0, 0, 1, 0]])


### Hadamard gate ###
"""
Represents a rotation of pi about the axis (\hat{x}+\hat{z})/\sqrt{2} at the Bloch sphere.
Maps the basis states (ie: creates a superposition if given a basis state):
    |0⟩ ⟼ (|0⟩+|1⟩)/sqrt(2)
    |1⟩ ⟼ (|0⟩-|1⟩)/sqrt(2)
"""
# Hadamard gate for a single qubit
Hadamard_gate = np.array([[1,1],
                          [1,-1]]) / np.sqrt(2)
# Hadamard transformation for a single qubit (or the Hermitian)
H1_gate = np.kron(Hadamard_gate, identity_2d_matrix)


### Entangling gate ###
entangling_gate = np.dot(CNOT_gate, H1_gate)
# print("Entangling Gate:")
# print(entangling_gate)
# print("\n")


### Swap gate ###
"""Swaps two qubits with respect to the basis |00⟩, |01⟩, |10⟩, |11⟩"""
swap_gate = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]])


### One Qubit System Basis ###
Zero_qubit = np.array([1, 0])
One_qubit = np.array([0, 1])


### Two Qubit System Basis ###
Zero_Zero_qubit = np.array([1, 0, 0, 0])
Zero_One_qubit = np.array([0, 1, 0, 0])
One_Zero_qubit = np.array([0, 0, 1, 0])
One_One_qubit = np.array([0, 0, 0, 1])


### Initial States for One Qubit System
# initial_state = Zero_qubit
# initial_state = One_qubit


### Initial States for Two Qubit System
initial_state = np.array([1, 0, 0, 0])
# initial_state = np.array([0, 0, 0, 0])
# initial_state = np.array([0, 1, 2, 3])
# initial_state = np.array([0.5, 0, 0.5, 0])
# initial_state = np.array([0, 1/np.sqrt(2), 0, 1/np.sqrt(2)])
# initial_state = np.array([0, 1, 0, 0])

# initial_state = Zero_Zero_qubit + One_Zero_qubit
# initial_state = One_One_qubit
# initial_state = Zero_Zero_qubit + One_Zero_qubit


### Final Bell States for One Qubit System
# final_state = np.dot(Hadamard_gate, initial_state) * np.sqrt(2)


### Final Bell States for Two Qubit System
final_state = np.dot(entangling_gate, initial_state) * np.sqrt(2)


### Final State for Swapped Two Qubit Ststem
# final_state = np.dot(swap_gate, initial_state)


### Print Statements ###
print("Entangling Gate:")
print(entangling_gate)
print("\n")
print("Initial State:")
print(initial_state)
print("\n")
print("Final State:")
print(final_state)
print("\n")













