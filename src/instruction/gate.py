"""
Gate

Creates matrix-based quantum gate objects

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
    """Creates matrix-based quantum gate objects"""
    @overload
    def __init__(self, gate: 'Gate'):
        """
        Creates a new matrix-based quantum gate

        :param gate: A gate to make a shallow copy of
        :type gate: gate
        """
        Instruction.__init__(self, gate.name, gate.instructions,
                             gate.num_qudits, gate.dim)

    def __init__(self, name: str = None,
                 instructions: np.ndarray = None,
                 num_qudits: int = None, dim: int = 3):
        """
        Creates a new matrix-based quantum gate

        :param name: The name of the gate
        :type name: str
        :param instructions: The instructions of the gate
        :type instructions: np.ndarray
        :param num_qudits: The number of qudits
        :type num_qudits: int
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        """
        Instruction.__init__(self, name, instructions, num_qudits, dim)

    @property
    def num_qudits(self):
        """
        Gets the number of qudits

        :return: The number of qudits
        :rtype: int
        """
        return self._num_qudits

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
        elif self.instructions is not None and self.dim is not None:
            self.num_qudits = \
                int(np.log(self.instructions.shape[0]) / np.log(self.dim))
        else:
            self.num_qudits = None
        if self.num_qudits is not None \
                and self.instructions is not None and self.dim is not None:
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
