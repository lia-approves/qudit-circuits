"""
Quantum Circuit Matrix

Creates quantum circuits in the form of matrices.\n
See for information about quantum logic gates from:\n
* https://www.illc.uva.nl/Research/Publications/Dissertations/DS-2002-04.text.pdf
* https://en.wikipedia.org/wiki/Quantum_logic_gate

Author: Alex Lim

Date of Initial Creation: October 19, 2021

"""

import math

import numpy as np

from MiscFunctions import MiscFunctions as Misc

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class QuantumCircuitMatrix:
    """
    Creates quantum circuits in the form of matrices.\n
    See for information about quantum logic gates from:\n
    * https://www.illc.uva.nl/Research/Publications/Dissertations/DS-2002-04.text.pdf
    * https://en.wikipedia.org/wiki/Quantum_logic_gate
    """
    def __init__(self):
        """Initializes quantum gates for use in this class"""
        self.identity_2d_matrix = None
        self.identity_3d_matrix = None
        self.Pauli_X_gate = None
        self.Pauli_Y_gate = None
        self.Pauli_Z_gate = None
        self.CNOT_gate = None
        self.Hadamard_gate = None
        self.H1_gate = None
        self.swap_gate = None

    ### Identity gates ###
    """The identity gate is the identity matrix"""
    # Identity gate for a single qubit
    identity_2d_matrix = np.diag([1, 1])
    """Identity gate for a single qubit"""
    # Identity gate for two qubits
    identity_3d_matrix = np.diag([1, 1, 1])
    """Identity gate for two qubits"""

    @staticmethod
    def Pauli_X_Gate():
        """
        The Pauli gates (X, Y, Z) are the three Pauli matrices
        and act on a single qubit.\n
        The Pauli X, Y, and Z equate, respectively,
        to a rotation around the x, y, and z axes of the Bloch sphere
        by pi radians.

        :return: Pauli-X gate for a single qubit (equivalent to the NOT gate
            for classical computers with respect to the standard basis |0⟩,
            |1⟩)
        :rtype: np.ndarray
        """
        return np.array([[0, 1],
                         [1, 0]])

    @staticmethod
    def Pauli_Y_Gate():
        """
        The Pauli gates (X, Y, Z) are the three Pauli matrices
        and act on a single qubit.\n
        The Pauli X, Y, and Z equate, respectively,
        to a rotation around the x, y, and z axes of the Bloch sphere
        by pi radians.

        :return: Pauli-Y gate for a single qubit
        :rtype: np.ndarray
        """
        return np.array([[0, -1j],
                         [1j, 0]])

    @staticmethod
    def Pauli_Z_Gate():
        """
        The Pauli gates (X, Y, Z) are the three Pauli matrices
        and act on a single qubit.\n
        The Pauli X, Y, and Z equate, respectively,
        to a rotation around the x, y, and z axes of the Bloch sphere
        by pi radians.

        :return: Pauli-Z gate for a single qubit
        :rtype: np.ndarray
        """
        return np.array([[1, 0],
                         [0, -1]])

    @staticmethod
    def CNOT_Gate():
        """
        maps the basis states |a,b⟩ ⟼ |a, a ⊕ b⟩, where ⊕ is XOR.

        :return: CNOT gate (or controlled Pauli-X gate)
        :rtype: np.ndarray
        """
        return np.kron(np.diag([1, 0]),
                       QuantumCircuitMatrix.identity_2d_matrix) + \
               np.kron(np.diag([0, 1]),
                       QuantumCircuitMatrix.Pauli_X_gate)

    @staticmethod
    def CY_Gate():
        """
        :return: CY gate (or controlled Pauli-Y gate)
        :rtype: np.ndarray
        """
        return np.kron(np.diag([1, 0]),
                       QuantumCircuitMatrix.identity_2d_matrix) + \
               np.kron(np.diag([0, 1]),
                       QuantumCircuitMatrix.Pauli_Y_gate)

    @staticmethod
    def CZ_Gate():
        """
        :return: CZ gate (or controlled Pauli-Z gate)
        :rtype: np.ndarray
        """
        return np.kron(np.diag([1, 0]),
                       QuantumCircuitMatrix.identity_2d_matrix) + \
               np.kron(np.diag([0, 1]),
                       QuantumCircuitMatrix.Pauli_Z_gate)

    ### Pauli gates ###
    # Pauli-X gate for a single qubit
    # (equivalent to the NOT gate for classical computers
    # with respect to the standard basis |0⟩, |1⟩)
    Pauli_X_gate = np.array([[0, 1],
                             [1, 0]])
    """
    Pauli-X gate for a single qubit (equivalent to the NOT gate for classical
    computers with respect to the standard basis |0⟩, |1⟩)\n
    The Pauli gates (X, Y, Z) are the three Pauli matrices
    and act on a single qubit.\n
    The Pauli X, Y, and Z equate, respectively,
    to a rotation around the x, y, and z axes of the Bloch sphere
    by pi radians.
    """

    # Pauli-Y gate for a single qubit
    Pauli_Y_gate = np.array([[0, -1j],
                             [1j, 0]])
    """
    Pauli-Y gate for a single qubit\n
    The Pauli gates (X, Y, Z) are the three Pauli matrices
    and act on a single qubit.\n
    The Pauli X, Y, and Z equate, respectively,
    to a rotation around the x, y, and z axes of the Bloch sphere
    by pi radians.
    """

    # Pauli-Z gate for a single qubit
    Pauli_Z_gate = np.array([[1, 0],
                             [0, -1]])
    """
    Pauli-Z gate for a single qubit\n
    The Pauli gates (X, Y, Z) are the three Pauli matrices
    and act on a single qubit.\n
    The Pauli X, Y, and Z equate, respectively,
    to a rotation around the x, y, and z axes of the Bloch sphere
    by pi radians.
    """

    # CNOT gate (or controlled Pauli-X gate)
    # maps the basis states |a,b⟩ ⟼ |a, a ⊕ b⟩, where ⊕ is XOR.
    CNOT_gate = np.kron(np.diag([1, 0]), identity_2d_matrix) + \
                np.kron(np.diag([0, 1]), Pauli_X_gate)
    """
    CNOT gate (or controlled Pauli-X gate)\n
    maps the basis states |a,b⟩ ⟼ |a, a ⊕ b⟩, where ⊕ is XOR.
    """

    # CY gate (or controlled Pauli-Y gate)
    CY_gate = np.kron(np.diag([1, 0]), identity_2d_matrix) + \
              np.kron(np.diag([0, 1]), Pauli_Y_gate)
    """CY gate (or controlled Pauli-Y gate)"""

    # CZ gate (or controlled Pauli-Z gate)
    CZ_gate = np.kron(np.diag([1, 0]), identity_2d_matrix) + \
              np.kron(np.diag([0, 1]), Pauli_Z_gate)
    """CZ gate (or controlled Pauli-Z gate)"""

    ### Hadamard gate ###
    @staticmethod
    def Hadamard_Gate():
        """
        Represents a rotation of pi about the axis
        :math:`(\\hat{x}+\\hat{z})/\\sqrt{2}` at the Bloch sphere.\n
        Maps the basis states
        (ie: creates a superposition if given a basis state):\n
        :math:`|0⟩ ⟼ (|0⟩+|1⟩)/\\sqrt{2}`\n
        :math:`|1⟩ ⟼ (|0⟩-|1⟩)/\\sqrt{2}`

        :return: The Hadamard gate for a single qubit
        :rtype: np.ndarray
        """
        return np.array([[1, 1],
                         [1, -1]]) / np.sqrt(2)

    # Hadamard gate for a single qubit
    Hadamard_gate = np.array([[1, 1],
                              [1, -1]]) / np.sqrt(2)
    """
    Hadamard gate for a single qubit\n
    Represents a rotation of pi about the axis
    :math:`(\\hat{x}+\\hat{z})/\\sqrt{2}` at the Bloch sphere.\n
    Maps the basis states
    (ie: creates a superposition if given a basis state):\n
    :math:`|0⟩ ⟼ (|0⟩+|1⟩)/\\sqrt{2}`\n
    :math:`|1⟩ ⟼ (|0⟩-|1⟩)/\\sqrt{2}`
    """

    # Hadamard transformation for a single qubit (or the Hermitian)
    H1_gate = np.kron(Hadamard_gate, identity_2d_matrix)
    """Hadamard transformation for a single qubit (or the Hermitian)"""

    ### Swap gate ###
    swap_gate = np.array([[1, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 1]])
    """Swaps two qubits with respect to the basis |00⟩, |01⟩, |10⟩, |11⟩"""

    @staticmethod
    def qubits_to_bits(numQubits: int):
        """
        Converts the processing power of qubits to bits

        :param numQubits: The number of qubits
        :type numQubits: int
        :return: The equivalent number of bits
        :rtype: int
        """
        return 2**numQubits

    @staticmethod
    def bits_to_qubits(numBits: int):
        """
        Converts the processing power of bits to qubits

        :param numBits: The number of bits
        :type numBits: int
        :return: The equivalent number of qubits
        :rtype: int
        """
        return math.ceil(np.log2(numBits))

    @staticmethod
    def identityGate(numQubits: int):
        """
        The identity gate is the identity matrix

        :param numQubits: The number of qubits
        :type numQubits: int
        :return: The identity gate (in matrix form)
        :rtype: np.ndarray
        """
        numBits = QuantumCircuitMatrix.qubits_to_bits(numQubits)
        return np.identity(numBits)

    @staticmethod
    def get_qubit_matrix(numQubits: int, *argv: int):
        """
        creates a square matrix for qubits

        :param numQubits: The number of entangled qubits
        :type numQubits: int
        :param argv: The qubits to switch from 0 to 1, defaults to 0
        :type argv: int
        :return: The square matrix for qubits
        :rtype: np.ndarray
        """
        numBits = QuantumCircuitMatrix.qubits_to_bits(numQubits)
        qubit_matrix = np.zeros([numBits, numBits])
        for args in argv:
            qubit_matrix[args, args] = 1
        if len(argv) == 0:
            qubit_matrix[0, 0] = 1
        return qubit_matrix

    @staticmethod
    def quantum_not_gate_matrix(numQubits: int):
        """
        creates a quantum equivalent of the classical not gate
        for any number of qubits

        :param numQubits: The number of entangled qubits
        :type numQubits: int
        :return: Pauli-X gate if numQubits=1,
            CNOT gate if numQubits=2,
            Toffoli gate if numQubits>2
        :rtype: np.ndarray
        """
        if numQubits == 0:
            return np.array([])
        if numQubits == 1:
            return QuantumCircuitMatrix.Pauli_X_gate
        if numQubits == 2:
            return QuantumCircuitMatrix.CNOT_gate
        q_not_gate_matrix = \
            np.kron(
                np.diag([1,0]),
                QuantumCircuitMatrix.identityGate(numQubits-1)) + \
            np.kron(
                np.diag([0,1]),
                QuantumCircuitMatrix.quantum_not_gate_matrix(numQubits-1))
        return q_not_gate_matrix

    @staticmethod
    def quantum_Fourier_transform(numQubits: int):
        """
        The quantum Fourier transform is the classical discrete Fourier
        transform applied to the vector of amplitudes of a quantum state,
        where we usually consider vectors of length N=2^n

        :param numQubits: The number of qubits
        :type numQubits: int
        :return: A quantum Fourier transform matrix for numQubits
        :rtype: np.ndarray
        """
        numBits = QuantumCircuitMatrix.qubits_to_bits(numQubits)
        quantum_Fourier_transform_matrix = Misc.real_to_complex_matrix(
            np.zeros([numBits, numBits]))
        # Using basic wave formula:
        quantum_phase = np.e ** (2j * np.pi / numBits)
        # # Using Euler's formula on basic wave formula:
        # quantum_phase = np.cos(2*np.pi/numBits) + np.sin(2*np.pi/numBits)*1j
        for i in range(numBits):
            for j in range(numBits):
                quantum_Fourier_transform_matrix[i][j] += quantum_phase ** (
                            i * j)
        quantum_Fourier_transform_matrix /= np.sqrt(numBits)
        return quantum_Fourier_transform_matrix

    @staticmethod
    def invert_matrix(matrix):
        """
        Calculates the inverse of a matrix

        :param matrix: A square matrix
        :type matrix: np.ndarray
        :return: The inverse of matrix
        :rtype np.ndarray:
        """
        from numpy.linalg import inv
        return inv(matrix)

    @staticmethod
    def applied_swap_gate(qubits: np.ndarray, *argv: int):
        """
        Applies the swap gate to qubits

        :param qubits: A matrix of qubits
        :type qubits: np.ndarray
        :param argv: Specified qubits to apply swap gate to, must be a multiple
            of 2 because swap gate will apply to every pair of two, must not
            have the same number more than once
        :type argv: int
        :return: A swapped qubit matrix
        :rtype: np.ndarray
        """
        swapped_qubit_matrix = np.zeros([qubits.shape[0]])
        for bits in range(qubits.shape[0]):
            swapped_qubit_matrix[bits] += qubits[bits][bits]
        if len(argv) == 0:
            swapped_qubit_matrix = np.dot(
                swapped_qubit_matrix,
                np.kron(
                    QuantumCircuitMatrix.swap_gate, np.identity(
                        int(int(qubits.shape[0]) /
                            int(QuantumCircuitMatrix.swap_gate.shape[0])))
                ))
        else:
            swapping_gate_matrix = np.identity(qubits.shape[0])
            for args in range(int(len(argv)/2)):
                qubit_0 = argv[args]
                qubit_1 = argv[args+1]
                if swapping_gate_matrix[qubit_0*2+1][qubit_0*2+1] != 0 and \
                        swapping_gate_matrix[qubit_1*2][qubit_1*2] != 0:
                    swapping_gate_matrix[qubit_0*2+1][qubit_0*2+1] -= 1
                    swapping_gate_matrix[qubit_1*2][qubit_1*2] -= 1
                    swapping_gate_matrix[qubit_0*2+1][qubit_1*2] += 1
                    swapping_gate_matrix[qubit_1*2][qubit_0*2+1] += 1
                    swapped_qubit_matrix = np.dot(
                        swapped_qubit_matrix, swapping_gate_matrix)
        swapped_qubit_matrix = np.diag(swapped_qubit_matrix)
        return swapped_qubit_matrix

    @staticmethod
    def print_qubits(*argv: np.ndarray):
        """
        Prints the dimensions and matrices of qubits

        :param argv: The qubits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qubit " + str(i) + " dimensions: " + str(args.shape))
            print("qubit " + str(i) + ":")
            print(args)
            print()
            i += 1

    @staticmethod
    def print_truncated_qubits(numDecimals: int, *argv: np.ndarray):
        """
        Prints the dimensions and truncated matrices of qubits

        :param numDecimals: The number of decimals to truncate to
        :param argv: The qubits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qubit " + str(i) + " dimensions: " + str(args.shape))
            print("qubit " + str(i) + ":")
            print(np.round(args, numDecimals))
            print()
            i += 1

    @staticmethod
    def QuantumPeriodFinding(func, *argv, n_count: int = 8):
        """
        Uses Shor's period finding-algorithm to compute the period of func

        :param func: A quantum function
        :type func: function
        :param argv: The arguments to pass to func
        :param n_count: The number of counting qubits
        :type n_count: int
        :return: The period
        :rtype: int
        """
        QFT = QuantumCircuitMatrix.quantum_Fourier_transform(n_count)
        QFT_dagger = QuantumCircuitMatrix.invert_matrix(QFT)
        qc = np.zeros([n_count, n_count])
        for q in range(n_count):
            qc[q][q] += \
                (func(argv))[q][q]
        qubit_matrix = \
            np.dot(np.kron(qc, np.identity(
                int(QFT_dagger.shape[0] / qc.shape[0]))), QFT_dagger)
        return int(qubit_matrix.sum(0).sum(0).real / 4)
