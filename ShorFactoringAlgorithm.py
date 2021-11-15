"""
Shor Factoring Algorithm

Simulates Shor's factoring algorithm on a classical machine.\n
Shor's factoring algorithm finds the factors of a composite number in
polynomial time O(log(:math:`N`)). For reference, using the classical Dixon's
factoring method, the optimal complexity is O(exp(
:math:`2\\sqrt{2}\\sqrt{log(n)log(log(n))}`)).\n
See for information about Shor's factoring algorithm from:\n
* https://www.youtube.com/watch?v=lvTqbM5Dq4Q

Author: Alex Lim

Date of Initial Creation: October 20, 2021

"""

from random import randint

import numpy as np

import QiskitShorFactoringAlgorithm as QkSFA
from MiscFunctions import FactoringFunctions as FactorFuncs
from QuantumCircuitMatrix import QuantumCircuitMatrix as qcm

__author__ = "Alex Lim"
__credits__ = "Alex Lim"
__maintainer__ = "Alex Lim"


class ShorFactoringAlgorithm:
    """
    Simulates Shor's factoring algorithm on a classical machine.\n
    Shor's factoring algorithm finds the factors of a composite number in
    polynomial time O(log(:math:`N`)). For reference, using the classical
    Dixon's factoring method, the optimal complexity is O(exp(
    :math:`2\\sqrt{2}\\sqrt{log(n)log(log(n))}`)).\n
    See for information about Shor's factoring algorithm from:\n
    * https://www.youtube.com/watch?v=lvTqbM5Dq4Q
    """
    @staticmethod
    def c_amod15(a, power):
        """
        Controlled multiplication by a mod 15\n
        * Note: For example purposes, unnecessary for program to run

        :param a: Some number co-prime with 15
        :type a: int
        :param power: The number of times to repeat the controlled-U gate
        :type power: int
        :return: Controlled multiplication gate
        :rtype: np.ndarray
        """
        if a not in [2, 7, 8, 11, 13]:
            raise ValueError("'a' must be 2,7,8,11 or 13")
        matrix_of_qubits = qcm.get_zero_qubit_matrix(4)
        a = int(a)
        for iteration in range(power):
            if a in [2, 13]:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 1)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 2)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 2, 3)
            if a in [7, 8]:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 2, 3)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 2)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 1)
            if a == 11:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 3)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 2)
            if a in [7, 11, 13]:
                matrix_of_qubits = np.dot(matrix_of_qubits, np.kron(
                    qcm.Pauli_X_gate, np.identity(
                        int(matrix_of_qubits.shape[0]/qcm.Pauli_X_gate.shape[0]
                            ))
                ))
        return matrix_of_qubits

    @staticmethod
    def c_amodb(a, power, b):
        """
        Controlled multiplication by a mod b

        :param a: Some number co-prime with b
        :type a: int
        :param b: The modulus
        :type b: int
        :param power: The number of times to repeat the controlled-U gate
        :type power: int
        :return: Controlled multiplication gate
        :rtype: np.ndarray
        """
        if a not in [2, (b - 1) / 2, (b - 1) / 2 + 1, b - 4, b - 2]:
            raise ValueError("'a' must be 2, %i, %i, %i, or %i" %
                             (((b - 1) / 2), ((b - 1) / 2 + 1), b - 4, b - 2))
        matrix_of_qubits = qcm.get_zero_qubit_matrix(4)
        a = int(a)
        for iteration in range(power):
            if a in [2, b - 2]:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 1)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 2)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 2, 3)
            if a in [(b - 1) / 2, (b - 1) / 2 + 1]:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 2, 3)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 2)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 1)
            if a == b - 4:
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 1, 3)
                matrix_of_qubits = qcm.\
                    applied_swap_gate(matrix_of_qubits, 0, 2)
            if a in [(b - 1) / 2, b - 4, b - 2]:
                matrix_of_qubits = np.dot(matrix_of_qubits, np.kron(
                    qcm.Pauli_X_gate, np.identity(
                        int(matrix_of_qubits.shape[0] / qcm.Pauli_X_gate.shape[
                            0]))))
        return matrix_of_qubits

    @staticmethod
    def qubitFactoringPeriodFinding(num: int = 15,
                                    a: int = 7,
                                    n_count: int = 8):
        """
        Uses Shor's factoring algorithm to compute the period

        :param num: A natural number
        :type num: int
        :param a: A guess factor
        :type a: int
        :param n_count: The number of counting qubits
        :type n_count: int
        :return: The period
        :rtype: int
        """
        QFT = qcm.quantum_Fourier_transform(n_count)
        QFT_dagger = qcm.invert_matrix(QFT)
        qc = np.zeros([n_count, n_count])
        for q in range(n_count):
            qc[q][q] += \
                (ShorFactoringAlgorithm.c_amodb(a, int(2**q), num))[q][q]
        qubit_matrix = \
            np.dot(np.kron(qc, np.identity(
                int(QFT_dagger.shape[0]/qc.shape[0]))), QFT_dagger)
        return int(qubit_matrix.sum(0).sum(0).real / 4)

    @staticmethod
    def qubitFactoringQiskit(num: int, limit: int = 1000,
                             show_errors: bool = False,
                             n_count: int = 8,
                             drawCircuitDiagram: bool = False):
        """
        Applies Shor's factoring algorithm to qubits

        :param num: A natural number
        :type num: int
        :param limit: The maximum number of attempts to find more factors,
            defaults to 1000 (the default for sys.getrecursionlimit())
        :param show_errors: Whether to show or ignore errors, defaults to False
        :type show_errors: bool
        :param n_count: The number of counting qubits, defaults to 8
        :type n_count: int
        :param drawCircuitDiagram: Whether to draw the circuit diagram,
            defaults to False
        :type drawCircuitDiagram: bool
        :return: The factorization of num
        :rtype: list
        """
        return ShorFactoringAlgorithm.ShorFactoringAlgorithmClassical(
            num, limit, show_errors,
            QkSFA.QiskitShorFactoringAlgorithmGeneral, n_count,
            drawCircuitDiagram)

    @staticmethod
    def qubitFactoringQuantum(num: int, limit: int = 1000,
                              show_errors: bool = False):
        """
        Applies Shor's factoring algorithm to qubits

        :param num: A natural number
        :type num: int
        :param limit: The maximum number of attempts to find more factors,
            defaults to 1000 (the default for sys.getrecursionlimit())
        :param show_errors: Whether to show or ignore errors, defaults to False
        :type show_errors: bool
        :return: The factorization of num
        :rtype: list
        """
        return ShorFactoringAlgorithm.ShorFactoringAlgorithmClassical(
            num, limit, show_errors,
            ShorFactoringAlgorithm.qubitFactoringPeriodFinding)

    @staticmethod
    def ShorFactoringAlgorithmClassical(
            num: int, limit: int = 1000, show_errors: bool = False,
            func: type(FactorFuncs.period) = FactorFuncs.period, *argv):
        """
        Applies Shor's factoring algorithm using classical operations

        :param num: A natural number
        :type num: int
        :param limit: The maximum number of attempts to find more factors,
            defaults to 1000 (the default for sys.getrecursionlimit())
        :param show_errors: Whether to show or ignore errors, defaults to False
        :type show_errors: bool
        :param func: The period finding function to use with parameters
            (num, guessFactor),
            defaults to a classical period finding function at
            MiscFunctions.FactoringFunctions.period
        :type func: function
        :param argv: The addition arguments to pass to func
        :return: The factorization of num
        :rtype: list
        """
        factorization = list()
        while num % 2 == 0:
            factorization.append(2)
            num /= 2
        for i in range(limit):
            if num == 1:
                factorization.append(int(num))
                while 1 in factorization:
                    factorization.remove(1)
                return sorted(factorization)
            guessFactor = num
            try:
                guessFactor = randint(3, int(num) - 1)
            except ValueError as message:
                if show_errors:
                    print("ValueError: ", message)
                continue
            try:
                if guessFactor != num and guessFactor % num != 0:
                    period = 1
                    try:
                        func_params = list()
                        func_params.append(num)
                        func_params.append(guessFactor)
                        for args in argv:
                            func_params.append(args)
                        func_params = tuple(func_params)
                        period = func(*func_params)
                    except ValueError as message:
                        if show_errors:
                            print("ValueError: ", message)
                        continue
                    if period % 2 != 1:
                        if (guessFactor**(period / 2) + 1) % num != 0 and \
                                (guessFactor**(period / 2) - 1) % num != 0:
                            factorization.append(int(FactorFuncs.gcd(
                                int(guessFactor**(period / 2) + 1), num)))
                            factorization.append(int(FactorFuncs.gcd(
                                int(guessFactor**(period / 2) - 1), num)))
                            num /= FactorFuncs.gcd(
                                int(guessFactor**(period / 2) + 1), num)
                            num /= FactorFuncs.gcd(
                                int(guessFactor**(period / 2) - 1), num)
                            if period == 2:
                                factorization.append(int(FactorFuncs.gcd(
                                    int(guessFactor), num)))
                                num /= FactorFuncs.gcd(
                                    int(guessFactor), num)
                                factorization.append(int(FactorFuncs.gcd(
                                    int(guessFactor), num)))
                                num /= FactorFuncs.gcd(
                                    int(guessFactor), num)
                            factorization.append(int(num))
                            while 1 in factorization:
                                factorization.remove(1)
                            return sorted(factorization)
            except OverflowError as message:
                if show_errors:
                    print("Unable to find factor #"
                          + str(len(factorization) + 1)
                          + " because ", message)
        factorization.append(int(num))
        while 1 in factorization:
            factorization.remove(1)
        return sorted(factorization)
