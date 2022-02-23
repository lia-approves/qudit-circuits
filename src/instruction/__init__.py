"""
BitOQutritSim instructions package

Enables instruction functionality for the BitOQutritSim package.

Author: Alex Lim

"""

from itertools import product
from typing import Iterable

import numpy as np
import pandas as pd

from src.QuantumCircuitMatrix import QuantumCircuitMatrix as QCM

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class Instruction(object):
    """Enables instruction functionality for the BitOQutritSim package."""
    def __init__(self, name: str = None,
                 instructions: tuple['Instruction'] = None,
                 num_qudits: int = None, dim: int = 3):
        """
        Creates a new instruction

        :param name: The name of the instruction
        :type name: str
        :param instructions: The instructions of the instruction
        :type instructions: Instruction
        :param num_qudits: The number of qudits
        :type num_qudits: int
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        """
        self._name = name
        self._instructions = None
        self._num_qudits = None
        self._dim = dim
        self.instructions = instructions
        self.num_qudits = num_qudits

    def __str__(self):
        """
        Returns the name of the instruction when converted to a string

        :return: The name of the instruction
        :rtype: str
        """
        return self.name

    def __len__(self):
        """
        Returns the number of instructions when the length is queried

        :return: The number of instructions
        :rtype: int
        """
        return len(self.instructions)

    def __getitem__(self, index: int):
        """
        Returns the instruction at the given index when the '[]' operator is
        used on an instruction instance

        :param index: The index of the instruction
        :type index: int
        :return: The instruction at the given index
        :rtype: Instruction
        """
        return self.instructions[index]

    @property
    def name(self):
        """
        Gets the instruction's name

        :return: The instruction's name
        :rtype: str
        """
        return self._name

    @property
    def instructions(self):
        """
        Gets the provided instructions

        :return: The instructions
        :rtype: Any
        """
        return self._instructions

    @property
    def dim(self):
        """
        Gets the dimension of the qudit (ie: qubit=2 and qutrit=3)

        :return: The qudit's dimension
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
    def name(self, name: str):
        """
        Sets the instruction's name

        :param name: The circuit object's name
        :type name: str
        """
        self._name = name

    @instructions.setter
    def instructions(
            self, instructions: 'Instruction' or Iterable['Instruction']):
        """
        Sets the circuit object's instructions

        :param instructions: The circuit object's instructions
        :type instructions: Instruction or Iterable[Instruction]
        """
        if instructions is None:
            self._instructions = None
        elif self.isinstruction(instructions):
            self._instructions = tuple([instructions])
        elif all([self.isinstruction(instr) for instr in instructions]):
            self._instructions = tuple(instructions)
        else:
            raise ValueError("'%s' objects cannot be used as instructions"
                             % type(instructions))

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
        self._num_qudits = num_qudits

    @classmethod
    def isinstruction(cls, obj: object):
        """
        Checks if obj is a valid instruction instance

        :param obj: An object
        :type obj: object
        :return: If obj is a valid instruction instance
        :rtype: bool
        """
        return isinstance(obj, Instruction) or isinstance(obj, np.ndarray)

    # TODO: implement choosing to switch which qudits are controls and targets
    # TODO: implement truth table to still function if matrix does not include all qudits
    def truth_table(self):
        """
        Displays and returns the truth table for the instruction instances

        :return: The truth table
        :rtype: pd.DataFrame
        """
        matrix_instr = self.to_matrix()
        tbl_input = list(product(range(self.dim), repeat=self.num_qudits))
        tbl_input = list(np.concatenate(tbl_input).flat)
        data = [[inp, QCM.qudit_int(np.dot(matrix_instr, QCM.get_ket(inp)))]
                for inp in tbl_input]
        df = pd.DataFrame(data, columns=pd.MultiIndex.from_product(
            [['Input', 'Output'], list(range(self.num_qudits))],
            names=['', 'Qudit:']))
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(df)
        return df

    def to_matrix(self):
        """
        Converts the instructions into matrix form

        :return: The instructions in matrix form
        :rtype: np.ndarray
        """
        if len(self) == 0:
            raise TypeError("%s.to_matrix() missing 1 required instruction"
                            % str(self))
        matrix_instr = 1
        for instr in self.instructions:
            if not isinstance(instr, np.ndarray):
                instr = instr.to_matrix()
            matrix_instr = np.dot(matrix_instr, instr)
        return matrix_instr

    # TODO: implement this
    @staticmethod
    def extend_gate(gate: 'Gate' or np.ndarray, num_qudits: int, dim: int = 3):
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
            return Instruction.extend_matrix(gate, num_qudits, dim)

    # TODO: implement this
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
        pass

    # TODO: implement this method to display the quantum instructions like in Qiskit
    def display(self):
        """Displays the quantum circuit"""
        pass
