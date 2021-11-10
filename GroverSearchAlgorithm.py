"""
Grover Search Algorithm

Simulates Grover's search algorithm on a classical machine

Author: Alex Lim

Date of Initial Creation: October 19, 2021

"""

import numpy as np

from QuantumCircuitMatrix import QuantumCircuitMatrix as qcm

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class GroverSearchAlgorithm:
    """Simulates Grover's search algorithm on a classical machine"""
    @staticmethod
    def two_qubit_search(*argv: int):
        """
        Applies Grover's search algorithm to two qubits

        :param argv: The qubits to switch from 0 to 1, defaults to 0
        :type argv: int
        :return: A matrix of the given value's location in a matrix
        :rtype: np.ndarray
        """
        numBits = qcm.qubits_to_bits(2)
        qubit_0 = np.zeros([numBits, numBits])
        if len(argv) == 0:
            qubit_0 += qcm.get_qubit_matrix(2)
        for args in argv:
            qubit_0 += qcm.get_qubit_matrix(2, args)
        qubit_0 = np.dot(qubit_0, qcm.H1_gate)
        qubit_1 = qcm.H1_gate
        qubit_0 = np.dot(qcm.CZ_gate, qubit_0)
        qubit_1 = np.dot(qubit_0, qubit_1)
        qubit_0 = np.dot(
            np.kron(qcm.Pauli_Z_gate, qcm.identity_2d_matrix),
            qubit_0)
        qubit_1 = np.dot(
            np.kron(qcm.Pauli_Z_gate, qcm.identity_2d_matrix),
            qubit_1)
        return qubit_1

    @staticmethod
    def qubit_search(numQubits: int = 2, *argv: int):
        """
        Applies Grover's searching algorithm to any number of qubits

        :param numQubits: The number of qubits, defaults to 2
        :type numQubits: int
        :param argv: The qubits to switch from 0 to 1, defaults to 0
        :type argv: int
        :return: A matrix of the given value's location in a matrix
        :rtype: np.ndarray
        """
        numBits = qcm.qubits_to_bits(numQubits)
        qubit_0 = np.zeros([numBits, numBits])
        if len(argv) == 0:
            qubit_0 += qcm.get_qubit_matrix(numQubits)
        for args in argv:
            qubit_0 += qcm.get_qubit_matrix(numQubits, args)
        qubit_0 = np.dot(
            qubit_0, np.kron(
                qcm.Hadamard_gate, np.identity(int((qubit_0.shape[0])/2))))
        qubit_1 = np.kron(
            qcm.Hadamard_gate, np.identity(int((qubit_0.shape[0])/2)))
        # qcm.print_qubits(qubit_0, qubit_1)
        qubit_0 = np.dot(
            np.kron(
                qcm.CZ_gate, np.identity(int((qubit_0.shape[0])/4))), qubit_0)
        qubit_1 = np.dot(qubit_0, qubit_1)
        # qcm.print_qubits(qubit_0, qubit_1)
        qubit_0 = np.dot(
            np.kron(qcm.Pauli_Z_gate, np.identity(int((qubit_0.shape[0])/2))),
            qubit_0)
        qubit_1 = np.dot(
            np.kron(qcm.Pauli_Z_gate, np.identity(int((qubit_0.shape[0])/2))),
            qubit_1)
        # qcm.print_qubits(qubit_0, qubit_1)
        return qubit_1


# qcm.print_qubits(GroverSearchAlgorithm.qubit_search(3, 2))
