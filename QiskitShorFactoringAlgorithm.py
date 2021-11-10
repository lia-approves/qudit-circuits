"""
Qiskit Shor Factoring Algorithm

Simulates Shor's factoring algorithm on a classical machine using Qiskit.
See for information from:
* https://qiskit.org/textbook/ch-algorithms/index.html
* https://youtu.be/mAHC1dWKNYE

Author: Alex Lim
Date of Initial Creation: October 20, 2021

"""

from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from qiskit import Aer, assemble, circuit, QuantumCircuit, transpile
from qiskit.visualization import plot_histogram

from MiscFunctions import FactoringFunctions

__author__ = "Alex Lim"
__credits__ = "Alex Lim"
__maintainer__ = "Alex Lim"


def QiskitShorFactoringAlgorithmGeneral(num: int = 15,
                                        a: int = 7,
                                        n_count: int = 8,
                                        drawCircuitDiagram: bool = False):
    """
    Uses Shor's factoring algorithm to compute the period

    :param num: A natural number, defaults to 15
    :type num: int
    :param a: A guess factor, defaults to 7
    :type a: int
    :param n_count: The number of counting qubits, defaults to 8
    :type n_count: int
    :param drawCircuitDiagram: Whether to draw the circuit diagram, defaults to
        False
    :type drawCircuitDiagram: bool
    :return: The period, or 1 if an error occurs
    :rtype: int
    """
    def c_amod15(a, power):
        """
        Controlled multiplication by a mod 15\n
        * Note: For example purposes, unnecessary for the program to run

        :param a: Some number co-prime with 15
        :type a: int
        :param power: The number of times to repeat the controlled-U gate
        :type power: int
        :return: Controlled multiplication gate
        :rtype: circuit.ControlledGate
        """
        if a not in [2, 7, 8, 11, 13]:
            raise ValueError("'a' must be 2,7,8,11 or 13")
        U = QuantumCircuit(4)
        for iteration in range(power):
            if a in [2,13]:
                U.swap(0,1)
                U.swap(1,2)
                U.swap(2,3)
            if a in [7,8]:
                U.swap(2,3)
                U.swap(1,2)
                U.swap(0,1)
            if a == 11:
                U.swap(1,3)
                U.swap(0,2)
            if a in [7,11,13]:
                for q in range(4):
                    U.x(q)
        U = U.to_gate()
        U.name = "%i^%i mod 15" % (a, power)
        c_U = U.control()
        return c_U

    def c_amod21(a, power):
        """
        Controlled multiplication by a mod 21\n
        * Note: For example purposes, unnecessary for the program to run

        :param a: Some number co-prime with 21
        :type a: int
        :param power: The number of times to repeat the controlled-U gate
        :type power: int
        :return: Controlled multiplication gate
        :rtype: circuit.ControlledGate
        """
        if a not in [2, 10, 11, 17, 19]:
            raise ValueError("'a' must be 2, 10, 11, 17, or 19")
        U = QuantumCircuit(4)
        for iteration in range(power):
            if a in [2, 19]:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
            if a in [10, 11]:
                U.swap(2, 3)
                U.swap(1, 2)
                U.swap(0, 1)
            if a == 17:
                U.swap(1, 3)
                U.swap(0, 2)
            if a in [10, 17, 19]:
                for q in range(4):
                    U.x(q)
        U = U.to_gate()
        U.name = "%i^%i mod 21" % (a, power)
        c_U = U.control()
        return c_U

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
        :rtype: circuit.ControlledGate
        """
        if a not in [2, (b - 1) / 2, (b - 1) / 2 + 1, b - 4, b - 2]:
            raise ValueError("'a' must be 2, %i, %i, %i, or %i" %
                             (((b - 1) / 2), ((b - 1) / 2 + 1), b - 4, b - 2))
        U = QuantumCircuit(4)
        for iteration in range(power):
            if a in [2, b-2]:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
            if a in [(b-1)/2, (b-1)/2+1]:
                U.swap(2, 3)
                U.swap(1, 2)
                U.swap(0, 1)
            if a == b-4:
                U.swap(1, 3)
                U.swap(0, 2)
            if a in [(b - 1) / 2, b - 4, b - 2]:
                for q in range(4):
                    U.x(q)
        U = U.to_gate()
        U.name = "%i^%i mod %i" % (a, power, b)
        c_U = U.control()
        return c_U

    def qft_dagger(numQubits: int):
        """
        n-qubit inverse quantum Fourier transform

        :param numQubits: The first n qubits in the circuit
        :type numQubits: int
        :return: The QFT†
        :rtype: circuit.ControlledGate
        """
        qc = QuantumCircuit(numQubits)
        for qubit in range(numQubits // 2):
            qc.swap(qubit, numQubits - qubit - 1)
        for j in range(numQubits):
            for m in range(j):
                qc.cp(-np.pi / float(2 ** (j - m)), m, j)
            qc.h(j)
        qc.name = "QFT†"
        return qc


    # Create QuantumCircuit with n_count counting qubits
    # and 4 qubits for U to act on
    qc = QuantumCircuit(n_count + 4, n_count)

    # Initialize counting qubits in state |+>
    for q in range(n_count):
        qc.h(q)

    # Initialize auxiliary register in state |1>
    qc.x(3 + n_count)
    try:
        # Do controlled-U operations
        for q in range(n_count):
            qc.append(c_amodb(a, 2 ** q, num),
                      [q] + [i + n_count for i in range(4)])
    except ValueError:
        return 1

    # Apply inverse quantum Fourier transform
    qc.append(qft_dagger(n_count), range(n_count))

    # Measure circuit
    qc.measure(range(n_count), range(n_count))
    aer_sim = Aer.get_backend('aer_simulator')
    t_qc = transpile(qc, aer_sim)
    qobj = assemble(t_qc)
    results = aer_sim.run(qobj).result()
    counts = results.get_counts()
    plot_histogram(counts)

    rows, measured_phases = [], []
    for output in counts:
        decimal = int(output, 2)        # Convert (base 2) string to decimal
        phase = decimal/(2**n_count)    # Find corresponding eigenvalue
        measured_phases.append(phase)
        # Adding values to a table to be printed to the terminal
        rows.append([f"{output}(bin) = {decimal:>3}(dec)",
                     f"{decimal}/{2**n_count} = {phase:.2f}"])
    # Print the table's rows
    headers = ["Register Output", "Phase"]
    df = pd.DataFrame(rows, columns=headers)
    print(df)

    rows = []
    for phase in measured_phases:
        frac = Fraction(phase).limit_denominator(num)
        rows.append([phase, f"{frac.numerator}/{frac.denominator}", frac.denominator])
    # Print the table's data
    headers=["Phase", "Fraction", "Guess for r"]
    df = pd.DataFrame(rows, columns=headers)
    print(df)

    if drawCircuitDiagram:
        qc.draw(output='mpl', filename='my_circuit.png')
        plt.show()

        # # Temporarily halt program for diagram
        # k = input("press close to exit")

    guessList = list()
    for phase in measured_phases:
        frac = Fraction(phase).limit_denominator(num)
        guessList.append(frac.denominator)

    return FactoringFunctions.most_common_element(guessList)
