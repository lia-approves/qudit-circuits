"""
BitOQutritSim instructions package

Enables instruction functionality for the BitOQutritSim package.

Author: Alex Lim

"""

from typing import Iterable, Union

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class Instruction(object):
    """Enables instruction functionality for the BitOQutritSim package."""
    def __init__(self, name: str = None,
                 instructions: tuple['Instruction'] = None,
                 num_qudits: int = None, dim: int = 3):
        self._name = name
        self._instructions = None
        self._num_qudits = None
        self._dim = dim
        self.instructions = instructions
        self.num_qudits = num_qudits

    def __str__(self):
        return self._name

    def __len__(self):
        return len(self.instructions)

    def __getitem__(self, index: int):
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
        elif isinstance(instructions, Instruction):
            self._instructions = tuple([instructions])
        elif all([isinstance(instr, Instruction) for instr in instructions]):
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

    # TODO: implement this method to display the quantum instructions like in Qiskit
    def display(self):
        """Displays the quantum circuit"""
        pass
