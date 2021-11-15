"""
Grover Search Algorithm

Simulates Grover's search algorithm on a classical machine.\n
Much like brute force guess and check programs, Grover's search algorithm can
be used to guess and check in order to more quickly finds solutions than
pure brute force. For example, this can be used to solve Sudoku boards.

Author: Alex Lim

Date of Initial Creation: October 19, 2021

"""

import numpy as np

from QuantumCircuitMatrix import QuantumCircuitMatrix as qcm

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class GroverSearchAlgorithm:
    """
    Simulates Grover's search algorithm on a classical machine.\n
    Much like brute force guess and check programs, Grover's search algorithm
    can be used to guess and check in order to more quickly finds solutions
    than pure brute force. For example, this can be used to solve Sudoku
    boards.
    """
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
    def qubit_search(qubit_0: np.ndarray,
            *argv: int, numQubits: int = 0,
                     oracle: np.ndarray = qcm.CZ_gate):
        """
        Applies Grover's searching algorithm to any number of qubits

        :param qubit_0: The matrix to check
        :type qubit_0: np.ndarray
        :param argv: The qubits to switch from 0 to 1, defaults to 0
        :type argv: int
        :param numQubits: The number of qubits, defaults to 2
        :type numQubits: int
        :param oracle: The oracle function as a square matrix, defaults to
            |11⟩, which is the controlled-Z gate
        :type oracle: np.ndarray
        :return: A matrix of the given value's location in a matrix
        :rtype: np.ndarray
        """
        if numQubits != 0:
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
                oracle, np.identity(
                    int((qubit_0.shape[0])/oracle.shape[0]))), qubit_0)
        qubit_1 = np.dot(qubit_0, qubit_1)
        # qcm.print_qubits(qubit_0, qubit_1)
        qubit_0 = np.dot(
            np.kron(qcm.Pauli_Z_gate, np.identity(
                int((qubit_0.shape[0])/qcm.Pauli_Z_gate.shape[0]))),
            qubit_0)
        qubit_0 = np.dot(np.kron(qcm.Hadamard_gate, np.identity(
            int(qubit_0.shape[0] / qcm.Hadamard_gate.shape[0]))), qubit_0)
        qubit_1 = np.dot(
            np.kron(qcm.Pauli_Z_gate, np.identity(
                int((qubit_0.shape[0])/qcm.Pauli_Z_gate.shape[0]))),
            qubit_1)
        # qcm.print_qubits(qubit_0, qubit_1)
        return qubit_1


class GroverSudokuSolver:
    """Implements Grover's search algorithm in order to solve Sudoku"""
    @staticmethod
    def convert_Sudoku_to_qubit_matrix(input_board: np.ndarray):
        """
        Converts a Sudoku board to a qubit matrix

        :param input_board: The Sudoku board
        :type input_board: np.ndarray
        :return: The Sudoku board's qubit matrix
        :rtype: np.ndarray
        """
        input_board_state = list()
        for tiles_1 in range(input_board.shape[0]):
            for tiles_2 in range(input_board.shape[0]):
                if input_board.item((tiles_1, tiles_2)):
                    input_board_state.append(
                        tiles_1 * input_board.shape[0] + tiles_2)
        input_board_state = tuple(input_board_state)
        Sudoku_matrix = qcm.get_qubit_matrix(
            input_board.shape[0] * 2, *input_board_state)
        return Sudoku_matrix

    @staticmethod
    def two_x_two_Sudoku_solver(input_board: np.ndarray):
        """
        Implements Grover's search algorithm in order to check a 2x2 Sudoku
        board

        :param input_board: The Sudoku board to solve
        :type input_board: np.ndarray
        :return: Whether the Sudoku board is a proper solution or not
        :rtype: bool
        """
        input_qubit_board = np.diag(
            [input_board.item(0, 0), input_board.item(0, 1),
             input_board.item(1, 0), input_board.item(1, 1)])
        if input_board.item((0, 0)):
            searched_board = GroverSearchAlgorithm.\
                qubit_search(input_qubit_board,
                             oracle=np.diag([-1, 1, -1, 1]))
        else:
            searched_board = GroverSearchAlgorithm. \
                qubit_search(input_qubit_board,
                             oracle=np.diag([1, -1, 1, -1]))
        if round(searched_board.sum(0).sum(0)) == -2:
            return True
        else:
            return False
