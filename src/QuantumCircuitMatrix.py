"""
Quantum Circuit Matrix

Creates quantum circuits in the form of matrices.

Author: Alex Lim

Date of Initial Creation: October 19, 2021

"""

import math
from itertools import permutations
from numbers import Real
from typing import Union

import numpy as np

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class QuantumCircuitMatrix(object):
    """Creates quantum circuits in the form of matrices."""
    @staticmethod
    def get_bra(*args: Union[int, np.ndarray, str, bytes],
                qutrit_string: str = "",
                show_errors: bool = False):
        """
        Gets the specified bra

        :param args: An individual bra
        :type args: int or np.ndarray or str or bytes
        :param qutrit_string: A string of qutrit bras
        :type qutrit_string: str
        :param show_errors: Whether to show or ignore errors, defaults to False
        :type show_errors: bool
        :return: The combined bra, defaults to ⟨0|
        :rtype: np.ndarray
        """
        zero_bra = np.array([[1, 0, 0]])  # ⟨0|
        one_bra = np.array([[0, 1, 0]])   # ⟨1|
        two_bra = np.array([[0, 0, 1]])   # ⟨2|
        plus_bra = (zero_bra + one_bra + two_bra) / np.sqrt(3)
        """:math:`⟨+| := (⟨0| + ⟨1| + ⟨2|)/\\sqrt{3}`"""
        dim = 3
        omega = np.e ** (2 * np.pi * 1j / dim)
        o = omega
        omega_bra = (zero_bra + o * one_bra + (o ** 2) * two_bra) / np.sqrt(3)
        """:math:`⟨ω| := (⟨0| + ω⟨1| + ω^2⟨2|)/\\sqrt{3}`"""
        omega_squared_bra = \
            (zero_bra + (o ** 2) * one_bra + o * two_bra) / np.sqrt(3)
        """:math:`⟨ω^2| := (⟨0| + ω^2⟨1| + ω⟨2|)/\\sqrt{3}`"""
        bra = 1
        if len(args) != 0:
            for argv in args[::-1]:
                if isinstance(argv, np.ndarray):
                    bra = np.kron(argv, bra)
                elif isinstance(argv, str):
                    bra_temp = QuantumCircuitMatrix.get_bra(qutrit_string=argv)
                    bra = np.kron(bra_temp, bra)
                elif not isinstance(argv, int):
                    try:
                        argv = int(argv)
                    except TypeError as message:
                        if show_errors:
                            print("TypeError: ", message)
                        continue
                if isinstance(argv, int):
                    if argv == 0:
                        bra = np.kron(zero_bra, bra)
                    elif argv == 1:
                        bra = np.kron(one_bra, bra)
                    elif argv == 2:
                        bra = np.kron(two_bra, bra)
                    else:
                        num_qutrits = 1
                        while QuantumCircuitMatrix.\
                                qutrits_to_bits(num_qutrits) < argv:
                            num_qutrits += 1
                        bra = np.kron(
                            QuantumCircuitMatrix.
                                get_qutrit_vector(num_qutrits, argv), bra)
        if len(qutrit_string) != 0:
            bra_temp = 1
            for i in range(len(qutrit_string)):
                q = qutrit_string[i]
                if q == "0":
                    q_bra = zero_bra
                elif q == "1":
                    q_bra = one_bra
                elif q == "2":
                    q_bra = two_bra
                elif q == "+":
                    q_bra = plus_bra
                elif q == "o":
                    if i+1 < len(qutrit_string) and qutrit_string[i+1] == "^":
                        if i+2 >= len(qutrit_string)\
                                or qutrit_string[i+2] != "2":
                            raise SyntaxError("missing \"2\" after \"^\"")
                        q_bra = omega_squared_bra
                    else:
                        q_bra = omega_bra
                else:
                    raise ValueError("get_bra does not support \"%s\". "
                                     "Please try get_qutrit_vector "
                                     "or directly use numpy ndarrays." % q)
                bra_temp = np.kron(q_bra, bra_temp)
            if not isinstance(bra, np.ndarray) and bra == 1:
                bra = bra_temp
            else:
                bra = np.kron(bra_temp, bra)
        if not isinstance(bra, np.ndarray) and bra == 1:
            return zero_bra
        return bra

    @staticmethod
    def bra_basis(dim: int = 3):
        """
        Gets the generalized bra quantum basis for a qudit of dim dimensions

        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :return: The generalized bra quantum basis as column vectors
        :rtype: list
        """
        bra_basis = list()
        for d in range(dim):
            bra_basis_temp = np.zeros([1, dim])
            bra_basis_temp[0, d] = 1
            bra_basis.append(bra_basis_temp)
        return bra_basis

    @staticmethod
    def get_ket(*args: Union[int, np.ndarray, str, bytes],
                qutrit_string: str = "",
                show_errors: bool = False):
        """
        Gets the specified ket

        :param args: An individual ket
        :type args: int or np.ndarray or str or bytes
        :param qutrit_string: A string of qutrit kets:
            use "+" for "+", "o" for "ω", and "o^2" for "ω²"
        :type qutrit_string: str
        :param show_errors: Whether to show or ignore errors, defaults to False
        :type show_errors: bool
        :return: The combined ket, defaults to |0⟩
        :rtype: np.ndarray
        """
        zero_ket = np.array([[1],
                             [0],
                             [0]])  # |0⟩
        one_ket = np.array([[0],
                            [1],
                            [0]])   # |1⟩
        two_ket = np.array([[0],
                            [0],
                            [1]])   # |2⟩
        plus_ket = (zero_ket + one_ket + two_ket) / np.sqrt(3)
        """:math:`|+⟩ := (|0⟩ + |1⟩ + |2⟩)/\\sqrt{3}`"""
        dim = 3
        omega = np.e ** (2 * np.pi * 1j / dim)
        o = omega
        omega_ket = (zero_ket + o * one_ket + (o ** 2) * two_ket) / np.sqrt(3)
        """:math:`|ω⟩ := (|0⟩ + ω|1⟩ + ω^2|2⟩)/\\sqrt{3}`"""
        omega_squared_ket =\
            (zero_ket + (o ** 2) * one_ket + o * two_ket) / np.sqrt(3)
        """:math:`|ω^2⟩ := (|0⟩ + ω|1⟩^2 + ω|2⟩)/\\sqrt{3}`"""
        ket = 1
        if len(args) != 0:
            for argv in args[::-1]:
                if isinstance(argv, np.ndarray):
                    ket = np.kron(argv, ket)
                elif isinstance(argv, str):
                    ket_temp = QuantumCircuitMatrix.get_ket(qutrit_string=argv)
                    ket = np.kron(ket_temp, ket)
                elif not isinstance(argv, int):
                    try:
                        argv = int(argv)
                    except TypeError as message:
                        if show_errors:
                            print("TypeError: ", message)
                        continue
                if isinstance(argv, int):
                    if argv == 0:
                        ket = np.kron(zero_ket, ket)
                    elif argv == 1:
                        ket = np.kron(one_ket, ket)
                    elif argv == 2:
                        ket = np.kron(two_ket, ket)
                    else:
                        num_qutrits = 1
                        while QuantumCircuitMatrix. \
                                qutrits_to_bits(num_qutrits) < argv:
                            num_qutrits += 1
                        ket = np.kron(QuantumCircuitMatrix.
                                      get_qutrit_vector(num_qutrits, argv), ket)
        if len(qutrit_string) != 0:
            ket_temp = 1
            for i in range(len(qutrit_string)):
                q = qutrit_string[i]
                if q == "0":
                    q_ket = zero_ket
                elif q == "1":
                    q_ket = one_ket
                elif q == "2":
                    q_ket = two_ket
                elif q == "+":
                    q_ket = plus_ket
                elif q == "o":
                    if i+1 < len(qutrit_string) and qutrit_string[i+1] == "^":
                        if i+2 >= len(qutrit_string)\
                                or qutrit_string[i+2] != "2":
                            raise SyntaxError("missing \"2\" after \"^\"")
                        q_ket = omega_squared_ket
                    else:
                        q_ket = omega_ket
                else:
                    raise ValueError("get_ket does not support \"%s\". "
                                     "Please try get_qutrit_vector "
                                     "or directly use numpy ndarrays." % q)
                ket_temp = np.kron(q_ket, ket_temp)
            if isinstance(ket, int) and ket == 1:
                ket = ket_temp
            else:
                ket = np.kron(ket_temp, ket)
        if isinstance(ket, int) and ket == 1:
            return zero_ket
        return ket

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
            ket_basis_temp = np.zeros([dim, 1])
            ket_basis_temp[d, 0] = 1
            ket_basis.append(ket_basis_temp)
        return ket_basis

    @staticmethod
    def get_prod(ket: Union[int, np.ndarray, str, bytes],
                 bra: Union[int, np.ndarray, str, bytes]):
        """
        Gets the outer product of a specified ket and bra

        :param ket: The ket
        :type ket: int or np.ndarray or str or bytes
        :param bra: The bra
        :type bra: int or np.ndarray or str or bytes
        :return: The outer product of a specified ket and bra
        :rtype: np.ndarray
        """
        ket = QuantumCircuitMatrix.get_ket(ket)
        bra = QuantumCircuitMatrix.get_bra(bra)
        return np.kron(ket, bra)

    @staticmethod
    def identity_gate(num_qutrits: int = 1):
        """
        Creates the identity gate using outer products.\n
        The identity gate is the identity matrix.

        :param num_qutrits: The number of qutrits, defaults to 1
        :type num_qutrits: int
        :return: The identity gate
        :rtype: np.ndarray
        """
        return sum(QuantumCircuitMatrix.identity_gate_helper(num_qutrits))

    @staticmethod
    def identity_gate_helper(num_qutrits: int):
        """Helper method for identity_gate"""
        get_prod = QuantumCircuitMatrix.get_prod
        zero_prod = get_prod(0, 0)  # |0⟩⟨0|
        one_prod = get_prod(1, 1)   # |1⟩⟨1|
        two_prod = get_prod(2, 2)   # |2⟩⟨2|
        if num_qutrits == 1:
            return [zero_prod, one_prod, two_prod]
        identity_gate_list = list()
        for q in QuantumCircuitMatrix.identity_gate_helper(num_qutrits - 1):
            identity_gate_list.append(np.kron(q, zero_prod))  # q ⊗ |0⟩⟨0|
            identity_gate_list.append(np.kron(q, one_prod))   # q ⊗ |1⟩⟨1|
            identity_gate_list.append(np.kron(q, two_prod))   # q ⊗ |2⟩⟨2|
        return identity_gate_list

    @staticmethod
    def gate_perm_order(gate: str, dim: int = 3, gate_name: str = ""):
        """
        Finds the order of the nontrivial permutation of the standard basis
        states

        :param gate: The permutation of the standard basis states in format:
            "+num", "-num", or "num,num,...,num"
        :type gate: str
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :param gate_name: The name of the gate
        :type gate_name: str
        :returns: The specified gate permutation for a single qudit
        :rtype: np.ndarray
        """
        accepted_operators = ["+", "-", ",", " "]
        accepted_numbers = [str(i) for i in range(0, 10)]
        basis_order = list(range(dim))
        if dim < 10 and not any([op in gate for op in accepted_operators]):
            if len(gate) % 2 == 0:
                for i in range(0, len(gate), 2):
                    basis_order[int(gate[i])] ^= basis_order[int(gate[i + 1])]
                    basis_order[int(gate[i + 1])] ^= basis_order[int(gate[i])]
                    basis_order[int(gate[i])] ^= basis_order[int(gate[i + 1])]
            else:
                raise SyntaxError("invalid syntax. \"%s\" "
                                  "does not contain a valid operator"
                                  % gate)
        k = -1
        for i in range(len(gate)):
            error = False
            if gate[i] == "+":
                j = i + 1
                while j < len(gate) and not gate[j] in accepted_operators:
                    if not gate[j] in accepted_numbers:
                        raise SyntaxError("invalid syntax. \"%s\" "
                                          "has invalid character \"%s\" "
                                          "at index %s"
                                          % (gate, gate[j], str(j)))
                    j += 1
                for cycle in range(int(int(gate[i + 1:j]) % dim)):
                    basis_order = basis_order[dim - 1:] + basis_order[:-1]
            elif gate[i] == "-":
                j = i + 1
                while j < len(gate) and not gate[j] in accepted_operators:
                    if not gate[j] in accepted_numbers:
                        raise SyntaxError("invalid syntax. \"%s\" "
                                          "has invalid character \"%s\" "
                                          "at index %s"
                                          % (gate, gate[j], str(j)))
                    j += 1
                for cycle in range(int(int(gate[i + 1:j]) % dim)):
                    basis_order = basis_order[1:] + basis_order[:1]
            elif (gate[i] == "," or gate[i] == " ") and k != -1:
                j = i + 1
                while j < len(gate) and gate[j] == " ":
                    j += 1
                while j < len(gate) and not gate[j] in accepted_operators:
                    if not gate[j] in accepted_numbers:
                        raise SyntaxError("invalid syntax. \"%s\" "
                                          "has invalid character \"%s\" "
                                          "at index %s"
                                          % (gate, gate[j], str(j)))
                    j += 1
                if int(gate[k:i]) > dim or int(gate[i:j]) > dim:
                    raise IndexError("list index out of range. \"%s\" "
                                     "has invalid operands \"%s\" and \"%s\""
                                     % (gate, gate[k:i], gate[i:j]))
                basis_order[int(gate[k:i])] ^= basis_order[int(gate[i:j])]
                basis_order[int(gate[i:j])] ^= basis_order[int(gate[k:i])]
                basis_order[int(gate[k:i])] ^= basis_order[int(gate[i:j])]
                k = -1
            elif gate[i] in accepted_numbers:
                if k == -1:
                    k = i
            else:
                error = True
            if error:
                raise SyntaxError("invalid syntax. \"%s\" "
                                  "has invalid character \"%s\" "
                                  "at index %s"
                                  % (gate, gate[i], str(i)))
        return basis_order

    @staticmethod
    def X_gate(gate: str = "", dim: int = 3):
        """
        Creates the Pauli-X gate:
        :math:`X|k⟩ = |k+1⟩`\n
        where the addition :math:`|k+1⟩` is taken modulo :math:`d`.\n
        We define the Pauli group as the set of unitaries generated by tensor
        produts of :math:`X` and :math:`Z` gates.  We write
        :math:`\\mathcal{P}_n^d` for the Pauli's acting on :math:`n` qudits.\n
        For qubits this :math:`X` gate is just the NOT gate.\n
        For a qubit there is only one non-trivial permutation of the standard
        basis states, which is implemented by the :math:`X` gate. For qutrits,
        there are five non-trivial permutations of the basis states. By
        analogy, we will all call these ternary X gates. These gates are
        :math:`X_{+1}`, :math:`X_{−1}`, :math:`X_{01}`, :math:`X_{12}`, and
        :math:`X_{02}`. The gate :math:`X_{±1}` sends :math:`|t⟩` to
        :math:`|(t±1)` mod 3⟩ for :math:`t ∈ \{0,1,2\}`; :math:`X_{01}` is just
        the qubit :math:`X` gate which is the identity when the input is |2⟩;
        :math:`X_{12}` sends |1⟩ to |2⟩ and |2⟩ to |1⟩, and likewise for
        :math:`X_{02}`.

        Examples
        --------
        >>> from src.instruction.QuantumCircuitMatrix import QuantumCircuitMatrix as qcm
        >>> qcm.X_gate("+1")
        array([[0, 0, 1],
               [1, 0, 0],
               [0, 1, 0]])
        >>> qcm.X_gate("-1")
        array([[0, 1, 0],
               [0, 0, 1],
               [1, 0, 0]])
        >>> qcm.X_gate("01")
        array([[0, 1, 0],
               [1, 0, 0],
               [0, 0, 1]])
        >>> qcm.X_gate("12")
        array([[1, 0, 0],
               [0, 0, 1],
               [0, 1, 0]])
        >>> qcm.X_gate("02")
        array([[0, 0, 1],
               [0, 1, 0],
               [1, 0, 0]])

        :param gate: The permutation of the standard basis states in format:
            "+num", "-num", or "num,num,...,num"
        :type gate: str
        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :returns: The specified Pauli-X gate for a single qudit, or all
            non-trivial permutations of the standard basis states if none
            specified thereof
        :rtype: np.ndarray or list[np.ndarray]
        """
        kets = QuantumCircuitMatrix.ket_basis(dim)
        if len(gate) == 0:
            basis_states = list()
            for permutation in list(permutations(range(dim))):
                if permutation != tuple(range(dim)):
                    basis_state = kets[permutation[0]]
                    for elem_order in permutation[1:]:
                        basis_state = np.concatenate(
                            [basis_state, kets[elem_order]], axis=1)
                    basis_states.append(basis_state)
            return basis_states
        basis_order = QuantumCircuitMatrix.\
            gate_perm_order(gate=gate, dim=dim, gate_name="Pauli_X_gate")
        return np.concatenate([basis for order, basis in
                               sorted(zip(basis_order, kets))], 1).astype(int)

    @staticmethod
    def Z_gate(dim: int = 3):
        """
        Creates the Pauli-Z gate:
        :math:`Z|k⟩ = ω^k|k⟩`\n
        where :math:`ω := e^{2\pi i/d}` such that :math:`ω^d = 1`.
        Unless otherwise stated, assume :math:`ω = e^{2\\pi i/3}`.\n
        We define the Pauli group as the set of unitaries generated by tensor
        produts of :math:`X` and :math:`Z` gates.  We write
        :math:`\\mathcal{P}_n^d` for the Pauli's acting on :math:`n` qudits.

        :param dim: The dimension of the qudit (ie: qubit=2 and qutrit=3),
            defaults to 3
        :type dim: int
        :return: Pauli-Z gate for a single qudit
        :rtype: np.ndarray
        """
        omega = np.e ** (2 * np.pi * 1j / dim)
        kets = QuantumCircuitMatrix.ket_basis(dim)
        return np.concatenate([(omega ** k) * ket
                               for ket, k in zip(kets, range(dim))], 1)

    # TODO: add Clifford unitaries (Definition 2.3 on pg 3)

    @staticmethod
    def Z_phase_gate(a: Real, b: Real):
        """
        The Z phase shift gate for a single qutrit:\n
        :math:`Z(a,b) := [|0⟩ & ω^a |1⟩ & ω^b |2⟩]`

        :param a: A power to raise ω
        :type a: Real
        :param b: A power to raise ω
        :type b: Real
        :return: The Z phase shift gate for a single qutrit
        :rtype: np.ndarray
        """
        dim = 3
        omega = np.e ** (2 * np.pi * 1j / dim)
        kets = QuantumCircuitMatrix.ket_basis(dim)
        return np.concatenate(kets[:1] +
                              [np.power(omega, k) * ket
                               for ket, k in zip(kets[1:], [a, b])], 1)

    @staticmethod
    def S_gate():
        """
        The qutrit S gate:
        :math:`S := Z(0,1)`

        :return: The qutrit S gate
        """
        return QuantumCircuitMatrix.Z_phase_gate(0, 1)

    @staticmethod
    def H_gate():
        """
        The Hadamard gate for a single qutrit\n
        maps :math:`|0⟩ ⟼ |+⟩, |0⟩ ⟼ |ω⟩, and |2⟩ ⟼ |ω^2⟩`

        :return: The Hadamard gate for a single qutrit
        :rtype: np.ndarray
        """
        dim = 3
        omega = np.e ** (2 * np.pi * 1j / dim)
        o = omega
        return np.array([[1, 1,    1   ],
                         [1, o,    o**2],
                         [1, o**2, o   ]]) / np.sqrt(3)

    @staticmethod
    def H_dagger_gate():
        """
        The inverse Hadamard gate or :math:`H^†` for a single qutrit\n
        :math:`H^† = H^3`

        :return: The Hadamard gate for a single qutrit
        :rtype: np.ndarray
        """
        return QuantumCircuitMatrix.H_gate() ** 3

    @staticmethod
    def X_phase_gate(a: Real, b: Real):
        """
        The X phase shift gate for a single qudit:\n
        :math:`X(a,b) := HZ(a,b)H^†`

        :param a: A power to raise ω
        :type a: Real
        :param b: A power to raise ω
        :type b: Real
        :return: The X phase shift gate for a single qutrit
        :rtype: np.ndarray
        """
        H = QuantumCircuitMatrix.H_gate()
        Z_phase = QuantumCircuitMatrix.Z_phase_gate
        H_dag = QuantumCircuitMatrix.H_dagger_gate()
        return np.dot(np.dot(H, Z_phase(a, b)), H_dag)

    @staticmethod
    def CX_gate():
        """
        The qutrit CX is the two-qutrit gate defined by
        :math:`CX |i, j⟩ = |i, i + j⟩`
        where the addition is taken modulo 3.\n
        :math:`CX = Λ(X_{+1})`

        :return: The qutrit CX gate
        :rtype: np.ndarray
        """
        return QuantumCircuitMatrix.c_gate(QuantumCircuitMatrix.X_gate("+1"))

    @staticmethod
    def two_ket_c_gate(U: np.ndarray):
        """
        Creates |2⟩-controlled gates where U is implemented on the last qutrits
        if and only if the first qutrit is in the |2⟩ state\n
        |0⟩ ⊗ |ψ⟩ ⟼ |0⟩ ⊗ |ψ⟩\n
        |1⟩ ⊗ |ψ⟩ ⟼ |1⟩ ⊗ |ψ⟩\n
        |2⟩ ⊗ |ψ⟩ ⟼ |2⟩ ⊗ U|ψ⟩

        :param U: A qutrit unitary
        :type U: np.ndarray
        :return: The |2⟩-U gate
        :rtype: np.ndarray
        """
        get_prod = QuantumCircuitMatrix.get_prod
        zero_prod = get_prod(0, 0)  # |0⟩⟨0|
        one_prod = get_prod(1, 1)   # |1⟩⟨1|
        two_prod = get_prod(2, 2)   # |2⟩⟨2|
        gate = np.kron(zero_prod, zero_prod)\
               + np.kron(zero_prod, one_prod)\
               + np.kron(zero_prod, two_prod)\
               + np.kron(one_prod, zero_prod)\
               + np.kron(one_prod, one_prod)\
               + np.kron(one_prod, two_prod)\
               + np.kron(two_prod, U)
        return gate

    @staticmethod
    def c_gate(U: np.ndarray):
        """
        Creates a controlled gate\n
        :math:`Λ(U)|c⟩|t⟩ := |c⟩ ⊗ (U^c|t⟩).`

        :param U: A qutrit unitary
        :type U: np.ndarray
        :return: The |2⟩-U gate
        :rtype: np.ndarray
        """
        get_prod = QuantumCircuitMatrix.get_prod
        zero_prod = get_prod(0, 0)  # |0⟩⟨0|
        one_prod = get_prod(1, 1)   # |1⟩⟨1|
        two_prod = get_prod(2, 2)   # |2⟩⟨2|
        gate = np.kron(zero_prod, zero_prod)\
               + np.kron(zero_prod, one_prod)\
               + np.kron(zero_prod, two_prod)\
               + np.kron(one_prod, U)\
               + np.kron(two_prod, np.dot(U, U))
        return gate

    @staticmethod
    def T_gate():
        """
        The qutrit T gate is the Z phase gate defined as\n
        :math:`T := Z(1/3,-1/3) = diag(1,e^{2πi/9},e^{-2πi/9})`

        :return: The qutrit T gate
        :rtype: np.ndarray
        """
        return QuantumCircuitMatrix.Z_phase_gate(1 / 3, -1 / 3)

    @staticmethod
    def R_gate():
        """
        The reflection gate\n
        :math:`R_{|2⟩} := Z(0,3/2) = diag(1,1,-1)`

        :return: The reflection gate
        :rtype: np.ndarray
        """
        return QuantumCircuitMatrix.Z_phase_gate(0, 3 / 2)

    @staticmethod
    def qutrits_to_bits(num_qutrits: int):
        """
        Converts the processing power of qutrits to bits

        :param num_qutrits: The number of qutrits
        :type num_qutrits: int
        :return: The equivalent number of bits
        :rtype: int
        """
        return 2 ** num_qutrits

    @staticmethod
    def bits_to_qutrits(num_bits: int):
        """
        Converts the processing power of bits to qutrits

        :param num_bits: The number of bits
        :type num_bits: int
        :return: The equivalent number of qutrits
        :rtype: int
        """
        return math.ceil(np.log2(num_bits))
    @staticmethod
    def get_qutrit_matrix(num_qutrits: int, *args: int):
        """
        creates a square matrix for qutrits

        :param num_qutrits: The number of entangled qutrits
        :type num_qutrits: int
        :param args: The qutrits to switch from 0 to 1, defaults to 0
        :type args: int
        :return: The square matrix for qutrits
        :rtype: np.ndarray
        """
        num_bits = QuantumCircuitMatrix.qutrits_to_bits(num_qutrits)
        qutrit_matrix = np.zeros([num_bits, num_bits])
        for argv in args:
            qutrit_matrix[argv, argv] = 1
        if len(args) == 0:
            qutrit_matrix[0, 0] = 1
        return qutrit_matrix

    @staticmethod
    def get_qutrit_vector(num_qutrits: int, *args: int):
        """
        creates a column vector for qutrits

        :param num_qutrits: The number of entangled qutrits
        :type num_qutrits: int
        :param args: The qutrits to switch from 0 to 1, defaults to 0
        :type args: int
        :return: The column vector for qutrits
        :rtype: np.ndarray
        """
        num_bits = QuantumCircuitMatrix.qutrits_to_bits(num_qutrits)
        qutrit_matrix = np.zeros([1, num_bits])
        for argv in args:
            qutrit_matrix[0, argv] = 1
        if len(args) == 0:
            qutrit_matrix[0, 0] = 1
        return qutrit_matrix.T

    @staticmethod
    def invert_matrix(matrix):
        """
        Calculates the inverse of a matrix

        :param matrix: A square matrix
        :type matrix: np.ndarray
        :return: The inverse of matrix
        :rtype np.ndarray:
        """
        from numpy.linalg import inv
        return inv(matrix)

    @staticmethod
    def convert_matrix_to_vector(qutrit_matrix: np.ndarray):
        """
        Converts a qutrit matrix to a qutrit vector

        :param qutrit_matrix: A qutrit matrix
        :type qutrit_matrix: np.ndarray
        :return: A qutrit vector
        :rtype: np.ndarray
        """
        if qutrit_matrix.shape[1] == 1:
            return qutrit_matrix
        qutrit_vector = qutrit_matrix.sum(axis=1)
        qutrit_vector = np.array([qutrit_vector])
        return qutrit_vector.T

    @staticmethod
    def convert_vector_to_matrix(qutrit_vector: np.ndarray):
        """
        Converts a qutrit vector to a qutrit matrix

        :param qutrit_vector: A qutrit vector
        :type qutrit_vector: np.ndarray
        :return: A qutrit matrix
        :rtype: np.ndarray
        """
        if qutrit_vector.shape[0] == qutrit_vector.shape[1]:
            return qutrit_vector
        qutrit_matrix = np.zeros([qutrit_vector.shape[0], qutrit_vector.shape[0]])
        for q in range(qutrit_vector.shape[0]):
            qutrit_matrix[q][q] += qutrit_vector[q][0]
        return qutrit_matrix

    @staticmethod
    def print_qutrits(*args: np.ndarray):
        """
        Prints the dimensions and matrices of qutrits

        :param args: The qutrit to print in order (starting at 0)
        :type args: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for argv in args:
            print("qutrit " + str(i) + " dimensions: " + str(argv.shape))
            print("qutrit " + str(i) + ":")
            print(argv)
            print()
            i += 1

    @staticmethod
    def print_trunc_qutrits(dec: int, *args: np.ndarray):
        """
        Prints the dimensions and truncated matrices of qutrits

        :param dec: The number of decimals to truncate to
        :param args: The qutrit to print in order (starting at 0)
        :type args: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for argv in args:
            print("qutrit " + str(i) + " dimensions: " + str(argv.shape))
            print("qutrit " + str(i) + ":")
            print(np.round(argv, dec))
            print()
            i += 1
