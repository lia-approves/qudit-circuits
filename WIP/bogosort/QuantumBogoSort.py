"""
Quantum BogoSort

A classical simulation of a quantum simulation of a quantum adaptation
of a classical input permutation sorting algorithm taking advantage of
quantum classical machines.

Author: Alex Lim

Date of Initial Creation: October 21, 2021

"""

import numpy as np
from numpy import dot as i, kron as d, ndarray as k

from WIP.bogosort.bogosort import bogosort
from src.MiscFunctions import MiscFunctions as idk
from src.QuantumCircuitMatrix import QuantumCircuitMatrix as e

__author__ = "Alex Lim"
__credits__ = "Alex Lim"
__maintainer__ = "Alex Lim"


class QuantumBogoSort(object):
    """
    A classical simulation of a quantum simulation of a quantum adaptation
    of a classical input permutation sorting algorithm taking advantage of
    quantum classical machines.
    """
    @staticmethod
    def QuantumBogoSort(a):
        """
        A classical simulation of a quantum simulation of a quantum adaptation
        of a classical input permutation sorting algorithm taking advantage of
        quantum classical machines.

        :param a: e
        :type a: k
        :return: e
        :rtype: k
        """
        return QuantumBogoSort._QuantumBogoSortHelper(a,a)

    @staticmethod
    def _QuantumBogoSortHelper(a,b):
        return bogosort.permutatioOrdino(b) if \
            bogosort.is_sorted(i(d(idk.random_ndarray(e.identity_2d_matrix,
                    e.Pauli_X_gate, e.Pauli_Y_gate, e.Pauli_Z_gate,
                    e.Hadamard_gate),
              np.identity(int((a.shape[0])/2))), a)) else QuantumBogoSort. \
            _QuantumBogoSortHelper(i(d(idk.random_ndarray(e.identity_2d_matrix,
                                    e.Pauli_X_gate, e.Pauli_Y_gate,
                                    e.Pauli_Z_gate,e.Hadamard_gate)
                               ,
                              np.identity(int((a.shape[0])/2))), a),b)
