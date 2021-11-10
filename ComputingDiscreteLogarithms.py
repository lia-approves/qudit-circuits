"""
Computing Discrete Logarithms

Computes the discrete logarithm

Author: Alex Lim
Date of Initial Creation: November 1, 2021

"""

from MiscFunctions import FactoringFunctions as FactoringFunctions

__author__ = "Alex Lim"
__credits__ = "Alex Lim"
__maintainer__ = "Alex Lim"


class ComputingDiscreteLogarithms:
    """
    Computes the discrete logarithm.\n
    * The Discrete Logarithm Problem:
        Let g be a generator of the group G of prime order q.\n
        Let
    """
    @staticmethod
    def BruteForceDiscreteLog(generator: int, modulus: int, cipher: int,
                              maxPower: int = 1000):
        """
        Computes the power of the generator using brute force

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: The cipher
        :type cipher: int
        :param maxPower: The max power of a group G
        :type maxPower: int
        :return: The power the generator is raised to, or 0 if greater than
            maxPower
        :rtype: int
        """
        for k in range(maxPower):
            if (generator ** k) % modulus == cipher:
                return k
        return 0

    @staticmethod
    def BruteForcePrimeDiscreteLog(generator: int, modulus: int, cipher: int,
                                   maxPower: int = 1000):
        """
        Computes the prime power of the generator using brute force

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: The cipher
        :type cipher: int
        :param maxPower: The max power of a group G
        :type maxPower: int
        :return: The prime power the generator is raised to, or 0 if greater
            than maxPower
        :rtype: int
        """
        for k in range(1, maxPower):
            if (generator ** k) % modulus == cipher:
                if FactoringFunctions.isPrimeQuick(k):
                    return k
        return 0

    @staticmethod
    def BruteForcePrimeCycleDiscreteLog(generator: int, modulus: int,
                                        cipher: int, maxPower: int = 1000):
        """
        Computes the prime power of the generator using brute force

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: The cipher
        :type cipher: int
        :param maxPower: The max power of a group G
        :type maxPower: int
        :return: The prime power the generator is raised to, or 0 if greater
            than maxPower
        :rtype: int
        """
        cycle_list = list(range(1, generator))
        for k in range(maxPower):
            if (generator ** k) % modulus in cycle_list:
                cycle_list.remove((generator ** k) % modulus)
            if len(cycle_list) == 0:
                if (generator ** k) % modulus == cipher:
                    if FactoringFunctions.isPrimeQuick(k):
                        return k
        return 0

    @staticmethod
    def DiscreteLogQuantum(generator: int, modulus: int,
                           cipher: int, maxPower: int = 1000):
        """
        Computes the prime power of the generator using quantum subroutines

        :param generator: The generator of a group G
        :type generator: int
        :param modulus: The modulo
        :type modulus: int
        :param cipher: The cipher
        :type cipher: int
        :param maxPower: The max power of a group G
        :type maxPower: int
        :return: The prime power the generator is raised to, or 0 if greater
            than maxPower
        :rtype: int
        """
        cycle_list = 0


# print(ComputingDiscreteLogarithms.BruteForceDiscreteLog(3, 17, 12))
# print(ComputingDiscreteLogarithms.BruteForcePrimeDiscreteLog(3, 17, 12))
# print(ComputingDiscreteLogarithms.BruteForcePrimeCycleDiscreteLog(3, 17, 12))
# print(3**29 % 17)
# print(list(range(17)))
