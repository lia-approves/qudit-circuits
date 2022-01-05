"""
Gate

Creates quantum gate objects

Author: Alex Lim

Date of Initial Creation: January 3, 2022

"""

import numpy as np

from src.instruction import Instruction

from typing import overload

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class Gate(Instruction):
    """Creates quantum gate objects"""
    @overload
    def __init__(self, gate: 'Gate'):
        Instruction.__init__(self, gate.name, gate.instructions,
                             gate.num_qudits, gate.dim)

    def __init__(self, name: str = None,
                 instructions: np.ndarray = None,
                 num_qudits: int = None, dim: int = 3):
        Instruction.__init__(self, name, instructions, num_qudits, dim)

    # def __init__(self, gate_name: str = None, matrix: np.ndarray = None,
    #              num_qudits: int = None, dim: int = 3):
    #     self._gate_name = gate_name
    #     self._matrix = matrix
    #     self._num_qudits = None
    #     self._dim = dim
    #     self.num_qudits = num_qudits

    def __str__(self):
        return self._gate_name

    @property
    def name(self):
        """
        Gets the gate object's name

        :return: The gate object's name
        :rtype: str
        """
        return self._gate_name

    @property
    def matrix(self):
        """
        Gets the gate object's matrix

        :return: The gate object's matrix
        :rtype: np.ndarray
        """
        return self._matrix

    @property
    def dim(self):
        """
        Gets the dimension of the qudit (ie: qubit=2 and qutrit=3)

        :return: The gate object's dimension
        :rtype: int
        """
        return self._dim

    @property
    def num_qudits(self):
        """
        Gets the number of qudits

        :return: The number of qudits
        :rtype: int
        """
        return self._num_qudits

    @name.setter
    def name(self, gate_name: str):
        """
        Sets the gate object's name

        :param gate_name: The gate object's name
        :type gate_name: str
        """
        self._gate_name = gate_name

    @matrix.setter
    def matrix(self, matrix: np.ndarray):
        """
        Sets the gate object's matrix

        :param matrix: The gate object's matrix
        :type matrix: np.ndarray
        """
        self._matrix = matrix

    @dim.setter
    def dim(self, dim: int = 3):
        """
        Sets the dimension of the qudit (ie: qubit=2 and qutrit=3)

        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        """
        self._dim = dim

    @num_qudits.setter
    def num_qudits(self, num_qudits: int = None):
        """
        Sets the number of qudits

        :param num_qudits: The number of qudits, defaults to the minimum number
            of required qudits
        :type num_qudits: int
        """
        if num_qudits is not None:
            self.num_qudits = num_qudits
        elif self.matrix is not None and self.dim is not None:
            self.num_qudits = \
                int(np.log(self.matrix.shape[0]) / np.log(self.dim))
        else:
            self.num_qudits = None
        if self.num_qudits is not None \
                and self.matrix is not None and self.dim is not None:
            num_bits = self.dim ** self.num_qudits
            if num_bits > self.matrix.shape[0]:
                num_cat = num_bits - self.matrix.shape[0]
                self.matrix = np.concatenate(
                    (self.matrix, np.zeros([num_cat, num_bits])), axis=0
                )
                self.matrix = np.concatenate(
                    (self.matrix, np.concatenate(
                        np.zeros((num_bits, num_cat)), np.identity(num_cat),
                        axis=0)
                     ), axis=1
                )
            elif num_bits < self.matrix.shape[0]:
                for i in range(2):
                    self.matrix = np.delete(
                        self.matrix, range(self.num_qudits, num_bits), axis=i)

    # TODO: implement this method to display the quantum gate like in Qiskit
    def display(self):
        """Displays the quantum gate"""
        pass
