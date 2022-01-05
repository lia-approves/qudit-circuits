"""
Misc Functions

Miscellaneous useful functions

Author: Alex Lim

Date of Initial Creation: October 21, 2021

"""

from warnings import catch_warnings, simplefilter

import numpy as np

from src.instruction.gate import Gate

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class MiscFunctions:
    """Miscellaneous useful functions"""
    @staticmethod
    def truth_table(*args: np.ndarray, dim: int = 3):
        """
        Displays a truth table for quantum gates

        :param args: Quantum gates
        :type args: np.ndarray
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        """
        highest_num_qudits = 1
        for argv in args:
            num_qudits_temp = int(np.log(int(argv.shape[0])) / np.log(dim))
            if num_qudits_temp > highest_num_qudits:
                highest_num_qudits = num_qudits_temp


    @staticmethod
    def extend_gate(gate: Gate or np.ndarray, num_qudits: int, dim: int = 3):
        """
        Extends a quantum gate to have identity gates for all qudits that the
            quantum gate is not interacting with

        :param gate: The quantum gate to be extended
        :type gate: Gate or np.ndarray
        :param num_qudits: The total number of qudits to extend the gate to
        :type num_qudits: int
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :return: The extended quantum gate
        :rtype: Gate or np.ndarray
        """
        if isinstance(gate, np.ndarray):
            return MiscFunctions.extend_matrix(gate, num_qudits, dim)

    @staticmethod
    def extend_matrix(gate_matrix: np.ndarray, num_qudits: int, dim: int = 3):
        """
        Extends a quantum gate matrix to have identity gates for all qudits
        that the quantum gate is not interacting with

        :param gate_matrix: The quantum gate matrix to be extended
        :type gate_matrix: np.ndarray
        :param num_qudits: The total number of qudits to extend the gate to
        :type num_qudits: int
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :return: The extended quantum gate
        :rtype: np.ndarray
        """


    @staticmethod
    def ket_basis(dim: int = 3):
        """
        Gets the generalized ket quantum basis for a qudit of dim dimensions

        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :return: The generalized ket quantum basis as column vectors
        :rtype: list[np.ndarray]
        """
        ket_basis = list()
        for d in range(dim):
            ket_basisTEMP = np.zeros([dim, 1])
            ket_basisTEMP[d, 0] = 1
            ket_basis.append(ket_basisTEMP)
        return ket_basis

    @staticmethod
    def print_qutrits(*argv: np.ndarray):
        """
        Prints the dimensions and matrices of qutrits

        :param argv: The qutrits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qutrits " + str(i) + " dimensions: " + str(args.shape))
            print("qutrits " + str(i) + ":")
            print(args)
            print()
            i += 1

    @staticmethod
    def print_trunc_qutrits(dec: int, *argv: np.ndarray):
        """
        Prints the dimensions and truncated matrices of qutrits

        :param dec: The number of decimals to truncate to
        :param argv: The qutrits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qutrit " + str(i) + " dimensions: " + str(args.shape))
            print("qutrit " + str(i) + ":")
            print(np.round(args, dec))
            print()
            i += 1

    @staticmethod
    def real_to_complex_matrix(real_matrix: np.ndarray):
        """
        Converts a real number matrix to a complex number matrix

        :param real_matrix: A real number matrix
        :type real_matrix: np.ndarray
        :return: A complex number matrix
        :rtype: np.ndarray
        """
        if real_matrix.dtype == np.complex_:
            return real_matrix
        else:
            return np.array(real_matrix, dtype=np.complex_)

    @staticmethod
    def complex_to_real_matrix(complex_matrix: np.ndarray,
                               show_warnings: bool = False):
        """
        Converts a complex number matrix to a real number matrix.\n
        * Note: The ComplexWarning is filtered and will not show up by default.

        :param complex_matrix: A complex number matrix
        :type complex_matrix: np.ndarray
        :param show_warnings: Whether to show or ignore warnings,
            defaults to False
        :type show_warnings: bool
        :raises ComplexWarning: Casting complex values to real discards the
            imaginary part
        :return: A real number matrix
        :rtype: np.ndarray
        """
        if complex_matrix.dtype != np.complex_:
            return complex_matrix
        else:
            if show_warnings:
                return np.array(complex_matrix, dtype=np.float_)
            with catch_warnings():
                simplefilter("ignore")
                return np.array(complex_matrix, dtype=np.float_)
