"""
Computing Discrete Logarithms

Computes the discrete logarithm\n
* The Discrete Logarithm Problem:
        Let :math:`g` be a generator of the group :math:`G`.\n
        Let :math:`c` be the cipher.\n
        Let :math:`p` be the prime modulus.\n
        Given :math:`c=g^{k}` mod :math:`p\\in G`.\n
        Find the value of :math:`k`.\n
Further reading:\n
.. _Estimating Gauss Sums and Calculating Discrete Logarithms:
    https://sites.cs.ucsb.edu/~vandam/gausssumdlog.pdf
.. _Khan Academy: https://www.khanacademy.org/computing/computer-science/
    cryptography/modern-crypt/v/discrete-logarithm-problem
.. _Wikipedia: https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm
* `Estimating Gauss Sums and Calculating Discrete Logarithms`_
* `Khan Academy`_
* `Wikipedia`_

Author: Alex Lim

Date of Initial Creation: November 1, 2021

"""

from CompletedExamples.ShorFactoringAlgorithm\
    import ShorFactoringAlgorithm as ShorFA
from src.MiscFunctions import FactoringFunctions as FactorFuncs

__author__ = "Alex Lim"
__credits__ = "Alex Lim"
__maintainer__ = "Alex Lim"


class ComputingDiscreteLogarithms:
    """
    Computes the discrete logarithm.\n
    * The Discrete Logarithm Problem:
        Let :math:`g` be a generator of the group :math:`G`.\n
        Let :math:`c` be the cipher.\n
        Let :math:`p` be the prime modulus.\n
        Given :math:`c=g^{k}` mod :math:`p\\in G`.\n
        Find the value of :math:`k`.
    Further reading:\n
    .. _Estimating Gauss Sums and Calculating Discrete Logarithms:
        https://sites.cs.ucsb.edu/~vandam/gausssumdlog.pdf
    .. _Khan Academy: https://www.khanacademy.org/computing/computer-science/
        cryptography/modern-crypt/v/discrete-logarithm-problem
    .. _Wikipedia:
        https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm
    * `Estimating Gauss Sums and Calculating Discrete Logarithms`_
    * `Khan Academy`_
    * `Wikipedia`_
    """
    @staticmethod
    def group_order(generator: int, modulus: int, limit: int = 1000):
        """
        Calculates the order of cyclic group G

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param limit: The maximum number of attempts to find more factors,
            defaults to 1000 (the default for sys.getrecursionlimit())
        :type limit: int
        :return: The order of group G, or 0 if not found
        :rtype: int
        """
        elem_0 = (generator**0) % modulus
        current_elem = generator
        for i in range(1, limit+1):
            if current_elem % modulus == elem_0:
                return i
            current_elem *= generator
        return 0

    @staticmethod
    def bsgs(generator: int, cipher: int, group_order: int):
        """
        The baby-step giant-step algorithm

        :param generator: The generator of a group G
        :type generator: int
        :param cipher: The cipher
        :type cipher: int
        :param group_order: The order of cylic group G
        :type group_order: int
        :raises ValueError: Unable to compute the prime power
        :return: The prime power of the generator
        :rtype: int
        """
        phi = FactorFuncs.isqrt(cipher-1)
        tbl = {((generator**i) % cipher): i for i in range(phi)}
        c = (generator**(phi*(cipher-2))) % cipher
        for i in range(phi):
            h = (group_order*((c**i) % group_order)) % group_order
            if h in tbl:
                return i * phi + tbl[h]
        raise ValueError("Unable to compute the prime power")

    @staticmethod
    def sqm(a: int, b: int, modulus: int):
        """
        Squares and multiplies then applies modulus

        :param a: The number to multiply by
        :type a: int
        :param b: Whether to multiply a or only square
        :type b: int
        :param modulus: The modulo
        :type modulus: int
        :return: The squared and multiplied number modulo modulus
        :rtype: int
        """
        r = 1
        for i in [int(x) for x in bin(int(b))[2:]]:
            if i:
                r = ((r**2) * a) % modulus
            else:
                r = (r**2) % modulus
        return r

    @staticmethod
    def subgrp_cong(generator: int, prime_factor: int, modulus: int,
                    cipher: int,
                    group_order: int = None):
        """
        Calculates the subgroup congruence

        :param generator: The generator of a group G
        :type generator: int
        :param prime_factor: A prime factor of group_order
        :type prime_factor: int
        :param modulus: The original modulus
        :type modulus: int
        :param cipher: A cipher
        :type cipher: int
        :param group_order: The order of cylic group G
        :type group_order: int
        :raises ValueError: Unable to compute subgroup congruence
        :return: The subgroup congruence
        :rtype: int
        """
        if group_order is None:
            group_order = ComputingDiscreteLogarithms.group_order(generator,
                                                                  prime_factor)
        g = ComputingDiscreteLogarithms.\
            sqm(generator, group_order // prime_factor, modulus)
        h = ComputingDiscreteLogarithms.\
            sqm(cipher, group_order // prime_factor, modulus) % modulus
        for i in range(1, modulus):
            if ComputingDiscreteLogarithms.\
                    sqm(g, i, modulus) % modulus == h:
                return i
        raise ValueError("Unable to compute subgroup congruence")

    @staticmethod
    def BruteForceDiscreteLog(generator: int, modulus: int, cipher: int,
                              max_power: int = 1000):
        """
        Computes the power of the generator using brute force

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: The cipher
        :type cipher: int
        :param max_power: The max power of a group G
        :type max_power: int
        :return: The power the generator is raised to, or 0 if greater than
            maxPower
        :rtype: int
        """
        for k in range(max_power):
            if (generator ** k) % modulus == cipher:
                return k
        return 0

    @staticmethod
    def DiscreteLogQuantum(generator: int, modulus: int, cipher: int,
                           group_order: int = None, max_power: int = 1000):
        """
        Computes the prime power of the generator using quantum subroutines

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: A cipher
        :type cipher: int
        :param group_order: The order of cylic group G
        :type group_order: int
        :param max_power: The max power of a group G
        :type max_power: int
        :return: The prime power the generator is raised to, or 0 if greater
            than maxPower
        :rtype: int
        """
        if group_order is None:
            group_order = ComputingDiscreteLogarithms.group_order(generator,
                                                                  modulus)
        prime_factorization = ShorFA.qubitFactoringQuantum(group_order,
                                                           limit=max_power)
        remainders = list(ComputingDiscreteLogarithms.subgrp_cong(
            generator, prime_factor, modulus, cipher, group_order)
                          for prime_factor in prime_factorization)
        while 2 in prime_factorization:
            remainders.pop(prime_factorization.index(2))
            prime_factorization.pop(prime_factorization.index(2))
        return FactorFuncs.Chinese_remainder_theorem(remainders,
                                                     prime_factorization)
