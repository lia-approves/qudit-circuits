"""
Misc Functions

Miscellaneous useful functions

Author: Alex Lim

Date of Initial Creation: October 21, 2021

"""

from warnings import catch_warnings, simplefilter

import numpy as np

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class MiscFunctions:
    """Miscellaneous useful functions"""
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

    @staticmethod
    def T(matrix: np.ndarray):
        """
        Gets the Hermitian transpose of matrix

        :param matrix: A matrix
        :type np.ndarray
        :return: The Hermitian transpose of matrix
        :rtype: np.ndarray
        """
        return matrix.conj().T

