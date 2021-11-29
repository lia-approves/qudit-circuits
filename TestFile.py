"""
Test File

Applies various miscellaneous tests

Author: Alex Lim

Date of Initial Creation: October 19, 2021

"""

import numpy as np

from src.QuantumCircuitMatrix import QuantumCircuitMatrix as qcm


__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


def print_tests(test_name: str, func, *args):
    """
    Prints the information from the tests

    :param test_name: The name of the test
    :type test_name: str
    :param func: The function to run tests for
    :type func: function
    :param args: The input for each tests
    """
    print(str(test_name) + ":")
    i = 1
    for argv in args:
        print("Test " + str(i) + ":")
        print("Input:\n" + str(argv))
        print("Output:\n" + str(func(argv)))
        print()
        i += 1


def check_tests_predetermined(test_name: str, func,
                              input_list: list, output_list: list):
    """
    Checks each test with already known correct output

    :param test_name: The name of the test
    :type test_name: str
    :param func: The function to run tests for
    :type func: function
    :param input_list: The input for each test
    :type input_list: list
    :param output_list: The known correct output for each test
    :type output_list: list
    """
    print(str(test_name) + ":")
    i = 1
    for inputs, outputs in zip(input_list, output_list):
        output = func(inputs)
        try:
            result = "Passed" if output == outputs else "Failed"
        except ValueError:
            result = "Passed" if np.allclose(output, outputs) else "Failed"
        print("Test " + str(i) + ": " + result)
        print("Input:\n" + str(inputs))
        print("Output:\n" + str(output))
        if result == "Failed":
            print("Expected Output:\n" + str(outputs))
        print()
        i += 1


def check_tests_dynamic(test_name: str, test_func, working_func, *args):
    """
    Checks each test with the output from a function known to always work

    :param test_name: The name of the test
    :type test_name: str
    :param test_func: The function to run tests for
    :type test_func: function
    :param working_func: The function to check the output of test_func
    :type working_func: function
    :param args: The input for each tests
    """
    input_list = list(args)
    output_list = list()
    for argv in args:
        output_list.append(working_func(argv))
    check_tests_predetermined(test_name, test_func, input_list, output_list)


class QuantumCircuitMatrixTests:
    """Applies tests for Quantum Circuit Matrix"""
    @staticmethod
    def quantum_not_gate_matrix(numQubits: int = 3):
        """
        creates a quantum equivalent of the classical not gate
        for any number of qubits

        :param numQubits: The number of entangled qubits
        :type numQubits: int
        """
        print(qcm.quantum_not_gate_matrix(numQubits))


def GroverSearchAlgorithmTests():
    """Applies tests for Grover Search Algorithm"""
    from CompletedExamples.GroverSearchAlgorithm import\
        GroverSearchAlgorithm as GroverSA
    inputs = list()
    inputs.append(np.diag([0, 0, 0, 0]))
    inputs.append(np.diag([0, 1, 0, 0]))
    inputs.append(np.diag([0, 0, 1, 0]))
    inputs.append(np.diag([0, 0, 0, 1]))
    outputs = list()
    outputs.append(np.diag([0, 0, 0, 0]))
    outputs.append(np.diag([0, 1, 0, 0]))
    outputs.append(np.diag([0, 0, -1, 0]))
    outputs.append(np.diag([0, 0, 0, 1]))
    check_tests_predetermined("Grover's Search Algorithm",
                              GroverSA.qubit_search,
                              inputs, outputs)


def GroverSearchSudokuSolverTests():
    """Applies Sudoku tests for Grover Search Algorithm"""
    from CompletedExamples.GroverSearchAlgorithm import \
        GroverSudokuSolver as GroverSS
    inputs = list()
    inputs.append(np.array([[1, 0],
                            [0, 1]]))
    inputs.append(np.array([[1, 0],
                            [0, 0]]))
    inputs.append(np.array([[0, 1],
                            [0, 0]]))
    inputs.append(np.array([[0, 0],
                            [1, 0]]))
    inputs.append(np.array([[0, 0],
                            [0, 1]]))
    inputs.append(np.array([[0, 1],
                            [1, 0]]))
    outputs = list()
    outputs.append(True)
    outputs.append(False)
    outputs.append(False)
    outputs.append(False)
    outputs.append(False)
    outputs.append(True)
    check_tests_predetermined("Grover's Search Algorithm",
                              GroverSS.two_x_two_Sudoku_solver,
                              inputs, outputs)


def ShorFactoringAlgorithmTests():
    """Applies tests for Shor Factoring Algorithm"""
    from CompletedExamples.ShorFactoringAlgorithm \
        import ShorFactoringAlgorithm as ShorFA
    inputs = list()
    inputs.append(15)
    inputs.append(21)
    inputs.append(27)
    inputs.append(42)
    inputs.append(117)
    inputs.append(144)
    outputs = list()
    outputs.append([3, 5])
    outputs.append([3, 7])
    outputs.append([3, 3, 3])
    outputs.append([2, 3, 7])
    outputs.append([3, 3, 13])
    outputs.append([2, 2, 2, 2, 3, 3])
    outputs.append([3, 41])
    check_tests_predetermined("Shor Factoring Algorithm",
                              ShorFA.qubitFactoringQuantum,
                              inputs, outputs)
