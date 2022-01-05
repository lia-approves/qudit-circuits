"""
Circuit

Creates quantum circuit objects

Author: Alex Lim

Date of Initial Creation: January 4, 2022

"""

from typing import Iterable, overload

import numpy as np

from src.instruction.gate import Gate

from src.instruction import Instruction

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class Circuit(Instruction):
    """Creates quantum circuit objects"""
    @overload
    def __init__(self, circuit: 'Circuit'):
        Instruction.__init__(self, circuit.name, circuit.instructions,
                             circuit.num_qudits, circuit.dim)

    def __init__(self, name: str = None,
                 instructions: tuple['Instruction'] = None,
                 num_qudits: int = None, dim: int = 3):
        Instruction.__init__(self, name, instructions, num_qudits, dim)

    def clear(self):
        """Removes all instructions from the circuit"""
        [self.pop() for i in range(len(self))]

    def copy(self):
        """
        Returns a shallow copy of the circuit

        :return: A shallow copy of the circuit
        :rtype: Circuit
        """
        return Circuit(self)

    def append(self, instruction: Instruction):
        """
        Adds an instruction to the end of the circuit

        :param instruction: The instruction
        :type instruction: Instruction
        """
        if isinstance(instruction, Instruction):
            instructions = list()
            if isinstance(self.instructions, Iterable):
                instructions.extend(self.instructions)
            instructions.append(instruction)
            self._instructions = tuple(instructions)
        else:
            raise ValueError("'%s' objects cannot be used as instructions"
                             % type(instruction))

    def extend(self, instructions: Iterable[Instruction]):
        """
        Appends all instructions to the end of the circuit

        :param instructions: The instructions
        :type instructions: Iterable[Instruction]
        """
        [self.append(instr) for instr in instructions]

    def pop(self, index: int = None):
        """
        Removes an instruction at a given position and returns it

        :param index: The index of the inserted instruction, defaults to the
            last instruction
        :type index: int
        :return: The removed instruction
        :rtype: Instruction
        """
        if index is None:
            index = len(self)
        instructions = list()
        if isinstance(self.instructions, Iterable):
            instructions.extend(self.instructions)
        removed_instruction = instructions.pop(index)
        self.instructions = tuple(instructions)
        return removed_instruction

    def index(self, name: str, case_sensitive: bool = True):
        """
        Returns the index of the first instruction in the circuit with a
        matching name

        :param name: The name of the instruction
        :type name: str
        :param case_sensitive: If the name is case-sensitive, defaults to True
        :type case_sensitive: bool
        """
        for i in range(len(self)):
            if str(self[i]) == name or \
                    (not case_sensitive and (self[i]).lower() == name.lower()):
                return i
        raise ValueError("%s.index(%s): %s not in %s"
                         % (str(self), name, name, str(self)))

    def count(self, name: str, case_sensitive: bool = True):
        """
        Returns the index of the first instruction in the circuit with a
        matching name

        :param name: The name of the instruction
        :type name: str
        :param case_sensitive: If the name is case-sensitive, defaults to True
        :type case_sensitive: bool
        """
        num_occurrences = 0
        for i in range(len(self)):
            if str(self[i]) == name or \
                    (not case_sensitive and (self[i]).lower() == name.lower()):
                num_occurrences += 1
        return num_occurrences

    def insert(self, index: int, instruction: Instruction):
        """
        Inserts an instruction at a given position

        :param index: The index of the inserted instruction
        :type index: int
        :param instruction: The instruction
        :type instruction: Instruction
        """
        if isinstance(instruction, Instruction):
            instructions = list()
            if isinstance(self.instructions, Iterable):
                instructions.extend(self.instructions)
            instructions.insert(index, instruction)
            self.instructions = tuple(instructions)
        else:
            raise ValueError("'%s' objects cannot be used as instructions"
                             % type(instruction))

    def remove(self, name: str, case_sensitive: bool = True):
        """
        Removes the first instruction in the circuit with a matching name

        :param name: The name of the instruction
        :type name: str
        :param case_sensitive: If the name is case-sensitive, defaults to True
        :type case_sensitive: bool
        """
        self.pop(self.index(name, case_sensitive))

    def reverse(self):
        """Reverses the order of the instruction in the circuit"""
        self.instructions = list(self.instructions)
        self.instructions.reverse()
        self.instructions = tuple(self.instructions)

    # TODO: implement this method to display the quantum circuit like in Qiskit
    def display(self):
        """Displays the quantum circuit"""
        pass
